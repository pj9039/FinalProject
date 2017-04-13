import datetime
import time

import pymysql
import pythoncom
import win32com.client

import logininfo
from ML import mysqlinfo

myhost,myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost,port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

## 이트레이드증권 API에 로그인하기위한 클래스
class XASessionEvents:
    logInState = 0
    def OnLogin(self, code, msg):
        print("OnLogin method is called")
        print(str(code))
        print(str(msg))
        if str(code) == '0000':
            XASessionEvents.logInState = 1

    def OnLogout(self):
        print("OnLogout method is called")

    def OnDisconnect(self):
        print("OnDisconnect method is called")

## 이트레이드증권에 데이터를 요청하는 쿼리를 보내는 클래스
class XAQueryEvents:
    queryState = 0
    def OnReceiveData(self, szTrCode):
        print("ReceiveData")
        XAQueryEvents.queryState = 1
    def OnReceiveMessage(self, systemError, mesageCode, message):
        print("ReceiveMessage")

if __name__ == "__main__":
    server_addr,server_port, server_type , user_id,user_pass,user_certificate_pass = logininfo.getlogin() # 증권사API접속을 위한 로그인 정보
    ## 증권사API에 로그인
    inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
    inXASession.ConnectServer(server_addr, server_port)
    inXASession.Login(user_id, user_pass, user_certificate_pass, server_type, 0)

    while XASessionEvents.logInState == 0:
        pythoncom.PumpWaitingMessages()

    ## 모든 종목코드를 얻기위한 쿼리
    inXAQuery = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
    inXAQuery.LoadFromResFile("Res\\t8430.res")
    inXAQuery.SetFieldData('t8430InBlock', 'gubun', 0, 0)
    inXAQuery.Request(0)
    while XAQueryEvents.queryState == 0:
        pythoncom.PumpWaitingMessages()
    nCount = inXAQuery.GetBlockCount('t8430OutBlock')
    shcodelist = []
    ## 모든종목코드를 리스트에 넣음
    for i in range(nCount):
        shcodelist.append(inXAQuery.GetFieldData('t8430OutBlock', 'shcode', i))
    print(shcodelist)
    XAQueryEvents.queryState = 0
    totalnum = len(shcodelist)
    count = 0
    cur = conn.cursor()
    todaydate = time.strftime("%Y%m%d") # 오늘 날짜
    cur.execute("select marketdate from stockprice order by marketdate desc limit 1") # DB안에있는 최신데이터 날짜를 얻기 위한 쿼리
    for row in cur:
        dbrecentdate = (row[0] + datetime.timedelta(days=1)).strftime("%Y%m%d") # DB안에있는 최신데이터 날짜

    print("dbrecentdate: ", dbrecentdate)
    print("todaydate: ", todaydate)

    if (todaydate != dbrecentdate): # 만약 DB최신데이터가 최신이 아니면
        try:
            for code in shcodelist:
                time.sleep(3.1) # 증권사API 10분당 200개이상 조회를 하면 멈추므로 시간제한
                print(code)
                ## 종목코드에 대한 거래일, 종가, 시가, 고가, 저가를 얻기
                inXAQuery.LoadFromResFile("Res\\t8413.res")
                inXAQuery.SetFieldData('t8413InBlock', 'shcode', 0, code)
                inXAQuery.SetFieldData('t8413InBlock', 'gubun', 0, '2')
                inXAQuery.SetFieldData('t8413InBlock', 'sdate', 0, dbrecentdate)
                inXAQuery.SetFieldData('t8413InBlock', 'edate', 0, todaydate)
                inXAQuery.SetFieldData('t8413InBlock', 'comp_yn', 0, 'N')
                inXAQuery.Request(0)
                while XAQueryEvents.queryState == 0:
                    pythoncom.PumpWaitingMessages()
                # Get FieldData
                nCount = inXAQuery.GetBlockCount('t8413OutBlock1')
                date = []
                close = []
                open = []
                high = []
                low = []
                for i in range(nCount):
                    date.append(inXAQuery.GetFieldData('t8413OutBlock1', 'date', i))
                    close.append(inXAQuery.GetFieldData('t8413OutBlock1', 'close', i))
                    open.append(inXAQuery.GetFieldData('t8413OutBlock1', 'open', i))
                    high.append(inXAQuery.GetFieldData('t8413OutBlock1', 'high', i))
                    low.append(inXAQuery.GetFieldData('t8413OutBlock1', 'low', i))
                XAQueryEvents.queryState = 0
                ## 종목코드에 대한 거래일, 종가, 시가, 고가, 저가를 DB에 보내기
                for i in range(0, len(date)):
                    with conn.cursor() as curs:
                        sql = "INSERT INTO stockprice(shcode, marketdate,closeprice,openprice,highprice,lowprice) VALUES (%s, %s, %s, %s, %s, %s)"
                        curs.execute(sql, (code, date[i], close[i], open[i], high[i], low[i]))
                print("총 코드수: ",totalnum,"현재진행결과: ",count)
                count = count + 1
                conn.commit()
        except:
            pass
    else:
        print("최신데이터")

conn.close()














