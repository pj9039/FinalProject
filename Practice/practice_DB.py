import pymysql
import mysqlinfo
from fastpip import pip

# Open database connection
myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute SQL query using execute() method.
sql = "SELECT * FROM stockprice WHERE shcode='000020'"
cursor.execute(sql)

# Fetch a single row using fetchone() method.
rows = cursor.fetchall()
# print(rows)       # total rows
# print(rows[0])    # first row
# print(rows[1])    # second row
i = -1
for row in rows:
    print(row)
    i = i + 1
    print(pip([i,int(row['closeprice'])], 5))

# disconnect from server
conn.close()