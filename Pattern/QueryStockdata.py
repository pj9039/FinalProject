import pymysql
import mysqlinfo


# Get stockprice from Database by stock code
def getstockprice(shcode):
    # Open database connection
    myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
    conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

    # create Dictionary Cursor from connection
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # Execute SQL
    sql = "SELECT * FROM stockprice WHERE shcode=%s"  # AND marketdate BETWEEN '2015-02-01' AND '2015-04-12'"
    cursor.execute(sql, shcode)

    # disconnect
    conn.close()

    # Fetch
    rows = cursor.fetchall()

    # End of function
    return rows


# Get stockprice from Database by prices
def makequerylist(p_low, p_high):
    # Open database connection
    myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
    conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

    # create Dictionary Cursor from connection
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # Execute SQL
    sql = "SELECT DISTINCT(shcode) FROM stockprice WHERE  %s < closeprice AND closeprice < %s AND marketdate=%s"
    cursor.execute(sql, p_low, p_high, getlastestdate())

    # disconnect
    conn.close()

    # Fetch & cleansing
    rows = cursor.fetchall()
    array = []
    for row in rows:
      array.append(row['shcode'])

    # End of function
    return array


# Get lastest date from Database
def getlastestdate():
    # Open database connection
    myhost, myport, myuser, mypassword, mydb, mycharset = mysqlinfo.getmysqlinfo()
    conn = pymysql.connect(host=myhost, port=myport, user=myuser, password=mypassword, db=mydb, charset=mycharset)

    # create Dictionary Cursor from connection
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # Execute SQL
    sql = "SELECT marketdate from stockprice order by marketdate desc limit 1"
    cursor.execute(sql)

    # disconnect
    conn.close()

    # Fetch & cleansing
    row = cursor.fetchall()

    # End of function
    return row