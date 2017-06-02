import scipy
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import time

import pymysql
import mysqlinfo
import numpy
from fastpip import pip

# # Pearson correlation coefficient example (how to use it)
# x = scipy.array([-0.65499887,  2.34644428, 3.0])
# y = scipy.array([-1.46049758,  3.86537321, 21.0])
#
# r_row, p_value = pearsonr(x, y)
# print("r_row = ", r_row)
# print("p_value = ", p_value)

# # 동화약품(000020)
# index = [0,43,101,174,339,456,499]
# data = [8000, 5000, 5000, 8000, 5000, 5000, 8000] # [5500, 6470, 9870, 7080, 10800, 7280, 7950]
# index2 = [0,50,200,250,300,450,499] # [0, 43, 101, 174, 339, 456, 499]
# data2 = [8000, 4000, 4000, 7000, 4000, 4000, 8000]
#
# r_row, p_value = pearsonr(data, data2)
# print("r_row = ", r_row)
# print("p_value = ", p_value)


# measure of running-time
start_time = time.time()



# open database connection
myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

# create Dictionary Cursor from connection
cursor = conn.cursor(pymysql.cursors.DictCursor)

# Execute SQL
sql = "SELECT * FROM stockprice WHERE shcode=%s"
shcode = "000020"     #동화약품(000020)
cursor.execute(sql, shcode)

# disconnect
conn.close()



# Fetch & Append data
rows = cursor.fetchall()
i = -1
graph_array = []
sample_array = [[0, 8000], [1, 4000], [2, 4000], [3, 8000], [4, 4000], [5, 4000], [6, 8000]]    # Double Bottom graph
#sample_array = [[0, 8000], [1, 5500], [2, 6500], [3, 5500], [4, 6000], [5, 5000], [6, 4000]]    # Triangles,Descending, up breakout (6)
#sample_array = [[0, 6000], [1, 5500], [2, 6500], [3, 6000], [4, 7000], [5, 6500], [6, 8000]]    # Three Rising Valleys, up breakout (4)
#sample_array = [[0, 8000], [1, 6000], [2, 6500], [3, 5000], [4, 6500], [5, 6000], [6, 8000]]    # Rounding Bottoms, up breakout (5) 그림이 좀 이상...

for row in rows:
    i += 1
    graph_array.append([i, int(row['closeprice'])])     # append data for PIP


# Find Pattern using pearson correlation coefficient
sample = pip(sample_array, 7)
plt.plot(numpy.array(sample)[:, 0], numpy.array(sample)[:, 1])      # plot result of sample pip
# plt.show()

pip_array = []  # list of found index
for k in range(0, len(graph_array) - 30):
    result = pip(graph_array[k:k+30], 7)
    a = numpy.array(result)     # print(a[:, 1])
    r_row, p_value = pearsonr(numpy.array(result)[:, 1], numpy.array(sample)[:, 1])
    if r_row > 0.7:
        print("종목코드 ", shcode, "에서 index가 ", k, "일 때, 피어슨상관계수 : ", r_row)
        print(rows[k])
        pip_array.append(k)

# print(pip_array)
# for idx in pip_array:
#     print(rows[idx])



# measure of running-time
print("--- %s seconds ---" % (time.time() - start_time))
