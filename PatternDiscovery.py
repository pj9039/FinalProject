import pymysql
import mysqlinfo
import matplotlib.pyplot as plt
from fastpip import pip


# Open database connection
myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)


# create Dictionary Cursor from connection
cursor = conn.cursor(pymysql.cursors.DictCursor)


# Execute SQL
sql = "SELECT * FROM stockprice WHERE shcode=%s"
shcode = "000020"     #동화약품(000020)
cursor.execute(sql, shcode)


# Fetch
rows = cursor.fetchall()
i = -1
array = []
graph = []
for row in rows:
    #print(row)
    i = i + 1
    #print(pip([i, int(row['closeprice'])], 5))
    #print([i, int(row['closeprice'])])
    array.append([i,int(row['closeprice'])])
    graph.append(int(row['closeprice']))
#print(array)


# Perceptually Important Points
result = pip(array,6)
print(result)
plt.plot(graph)


# Perceptually Important Points
index = []
data = []
for idx in result:
    i = i + 1
    index.append(idx[0])
    data.append(idx[1])
#index = [0,43,101,174,339,456,499]
#data = [5500, 6470, 9870, 7080, 10800, 7280, 7950]
plt.plot(index, data)
plt.grid(True)
plt.show()


# disconnect
conn.close()
