import pymysql
import mysqlinfo


# Get stockprice from Database
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
