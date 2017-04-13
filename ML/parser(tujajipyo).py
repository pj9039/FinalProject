import urllib.request

import pymysql
from bs4 import BeautifulSoup

import mysqlinfo
from ML import Allcode

myhost,myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost,port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)


code = Allcode.getcode()
for c in code:
    try:
        url="http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A"+c+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701%22"
        print(c)
        f = urllib.request.urlopen(url).read()
        soup=BeautifulSoup(f, 'html.parser')
        print('----------------------------------------------')

        cells = soup.find('tr').find_all('th')

        date = []
        for cell in cells:
            date.append(cell.string)
        print('----------------------------------------------')
        print('EPS')
        cells = soup.find('tr', {'id': "p_grid1_1"}).find_all('td')
        eps = []
        for cell in cells:
            eps.append(cell.string)

        for i in range(1,6):
            with conn.cursor() as curs:
                sql = "INSERT INTO eps(shcode, gsym,epsvalue) VALUES (%s, %s,%s)"
                curs.execute(sql, (c, date[i] + '/01', eps[i-1]))

            conn.commit()
    except:
        pass

conn.close()


