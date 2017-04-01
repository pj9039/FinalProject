import matplotlib.pyplot as plt
import pymysql
from fastpip import pip
import mysqlinfo

# Open database connection
myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

# create Dictionary Cursor from connection
cursor = conn.cursor(pymysql.cursors.DictCursor)

# Execute SQL
sql = "SELECT * FROM stockprice WHERE shcode=%s"# AND marketdate BETWEEN '2015-01-01' AND '2015-03-29'"
shcode = "000020"     #동화약품(000020)
cursor.execute(sql, shcode)

# disconnect
conn.close()



# Fetch
rows = cursor.fetchall()
i = -1
array = []
graph = []
for row in rows:
    i = i + 1
    array.append([i,int(row['closeprice'])])
    graph.append(int(row['closeprice']))



# Perceptually Important Points & Stock Market Graph
result = pip(array, 7)
print(result)
plt.plot(graph)
plt.grid(True)



# Perceptually Important Points Graph
index = []
data = []
for idx in result:
    i += 1
    index.append(idx[0])
    data.append(idx[1])
#index = [0,43,101,174,339,456,499]
#data = [5500, 6470, 9870, 7080, 10800, 7280, 7950]
plt.plot(index, data)
plt.show()
