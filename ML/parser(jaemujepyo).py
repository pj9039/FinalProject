import urllib.request

import pymysql
from bs4 import BeautifulSoup

from ML import Allcode
from ML.NoUpload import mysqlinfo

myhost,myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
code = Allcode.getcode()
conn = pymysql.connect(host=myhost,port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

for c in code:
    url="http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A"+c+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"
    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')
    try:
        print('----------------------------------------------')
        print(c)
        cells = soup.find('tr').find_all('th')
        date = []
        for cell in cells:
            date.append(cell.string)
        for i in range(1,5):
            print(date[i])
        cells = soup.find('div', {'id': "divDaechaY"})
        jmst = []
        for i in range(0,3):
            for cell in cells.findAll('tr', {'class': "rwf rowBold"})[i].find_all('div'):
                jmst.append(cell.string)
            for cell in cells.findAll('tr', {'class': "rwf rowBold"})[i].find_all('td'):
                jmst.append(cell.string)
        print(jmst)
        print(len(jmst))
        cells = soup.find('div', {'id': "divCashY"})
        moneyflow = []
        for i in range(0, 4):
            for cell in cells.findAll('tr', {'class': "rwf rowBold"})[i].find_all('div'):
                moneyflow.append(cell.string)
            for cell in cells.findAll('tr', {'class': "rwf rowBold"})[i].find_all('td'):
                moneyflow.append(cell.string)
        print(moneyflow)
        print(len(moneyflow))
        for i in range(0, 4):
            with conn.cursor() as curs:
                sql = "INSERT INTO jmst(shcode, gsym,jasan,buchae,jabon) VALUES (%s,%s,%s,%s,%s)"
                curs.execute(sql, (c, date[i+1] + '/01', jmst[i + 1], jmst[i + 6], jmst[i + 11] ))
        for i in range(0, 4):
            with conn.cursor() as curs:
                sql = "INSERT INTO moneyflow(shcode, gsym,selling,tooja,jaemoo,money) VALUES (%s,%s,%s,%s,%s,%s)"
                curs.execute(sql, (c, date[i+1] + '/01', moneyflow[i + 1], moneyflow[i + 6], moneyflow[i + 11], moneyflow[i + 16]))

        conn.commit()

    except:
        pass

conn.close()
