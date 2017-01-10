import win32com.client
import pythoncom
import time
import logininfo
import pymysql
import mysqlinfo
myhost,myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost,port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

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

class XAQueryEvents:
    queryState = 0
    def OnReceiveData(self, szTrCode):
        print("ReceiveData")
        XAQueryEvents.queryState = 1
    def OnReceiveMessage(self, systemError, mesageCode, message):
        print("ReceiveMessage")


if __name__ == "__main__":
    server_addr,server_port, server_type , user_id,user_pass,user_certificate_pass = logininfo.getlogin()

    #--------------------------------------------------------------------------
    # Login Session
    #--------------------------------------------------------------------------
    inXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
    inXASession.ConnectServer(server_addr, server_port)
    inXASession.Login(user_id, user_pass, user_certificate_pass, server_type, 0)

    while XASessionEvents.logInState == 0:
        pythoncom.PumpWaitingMessages()



    #--------------------------------------------------------------------------
    # Get single data
    #--------------------------------------------------------------------------
    inXAQuery = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)

    inXAQuery.LoadFromResFile("Res\\t8430.res")
    inXAQuery.SetFieldData('t8430InBlock', 'gubun', 0, 0)
    inXAQuery.Request(0)

    while XAQueryEvents.queryState == 0:
        pythoncom.PumpWaitingMessages()


    # Get FieldData
    nCount = inXAQuery.GetBlockCount('t8430OutBlock')
    shcodelist = []
    for i in range(nCount):
        #print(i, ":", inXAQuery.GetFieldData('t8430OutBlock', 'hname', i))
        shcodelist.append(inXAQuery.GetFieldData('t8430OutBlock', 'shcode', i))
    print(shcodelist)
    XAQueryEvents.queryState = 0
    totalnum = len(shcodelist)
    count = 0
    try:
        for code in shcodelist:
            time.sleep(1)
            print(code)

            inXAQuery.LoadFromResFile("Res\\t8413.res")
            inXAQuery.SetFieldData('t8413InBlock', 'shcode', 0, code)
            inXAQuery.SetFieldData('t8413InBlock', 'gubun', 0, '2')
            inXAQuery.SetFieldData('t8413InBlock', 'sdate', 0, '20130101')
            inXAQuery.SetFieldData('t8413InBlock', 'edate', 0, '20170110')
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
                #print(inXAQuery.GetFieldData('t8413OutBlock1', 'date', i), ":", inXAQuery.GetFieldData('t8413OutBlock1', 'close', i), ":", inXAQuery.GetFieldData('t8413OutBlock1', 'open', i), ":", inXAQuery.GetFieldData('t8413OutBlock1', 'high', i), ":", inXAQuery.GetFieldData('t8413OutBlock1', 'low', i))
            XAQueryEvents.queryState = 0
            for i in range(0, len(date)):
                with conn.cursor() as curs:
                    sql = "INSERT INTO stockprice(shcode, marketdate,closeprice,openprice,highprice,lowprice) VALUES (%s, %s, %s, %s, %s, %s)"
                    curs.execute(sql, (code, date[i], close[i], open[i], high[i], low[i]))
            print("총 코드수: ",totalnum,"현재진행결과: ",count)
            count = count + 1
            conn.commit()


    except:
        pass

conn.close()














