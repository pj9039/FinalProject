import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.dates import DateFormatter, WeekdayLocator,DayLocator, MONDAY
from matplotlib.finance import candlestick_ohlc
import pymysql
from pandas import DataFrame
import mysqlinfo

# Open database connection
myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

# create Dictionary Cursor from connection
cursor = conn.cursor(pymysql.cursors.DictCursor)

# Execute SQL
sql = "SELECT * FROM stockprice WHERE shcode=%s"# AND marketdate BETWEEN '2015-02-01' AND '2015-04-12'"
shcode = "000020"     #동화약품(000020)
cursor.execute(sql, shcode)

# disconnect
conn.close()



# Fetch
rows = cursor.fetchall()
i = -1

# create List type array
marketdate, openprice, closeprice, highprice, lowprice = [], [], [], [], []
for row in rows:
    i += 1
    marketdate.append(dates.date2num(row['marketdate']))
    openprice.append(int(row['openprice']))
    closeprice.append(int(row['closeprice']))
    highprice.append(int(row['highprice']))
    lowprice.append(int(row['lowprice']))

# create DataFrame
graph = {'marketdate' :  marketdate,
         'openprice'  :  openprice,
         'closeprice' :  closeprice,
         'highprice'  :  highprice,
         'lowprice'   :  lowprice}
graph = DataFrame(graph)
print(graph)



# Graph Drawing
mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()                  # minor ticks on the days
# weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
weekFormatter = DateFormatter('%b %d, %Y')  # e.g., Jan 12, 2014

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis_date()
ax.autoscale_view()
ax.grid(True)

candlestick_ohlc(ax, zip(graph['marketdate'].index, graph['openprice'], graph['highprice'], graph['lowprice'], graph['closeprice']), colorup="red", colordown="blue", width=0.6)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
#plt.xticks(rotation=45)
plt.show()