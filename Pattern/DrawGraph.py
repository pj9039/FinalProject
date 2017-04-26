from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.patches as patches
from pandas import DataFrame
from datetime import datetime
import os
import Pattern.QueryStockdata as shquery
import sys


# Draw real candlestick chart
def drawgraph(shcode, startdate=0, period=0):
    # 1st parameter, shcode is stock code.  # e.g., shcode = "000020"     #동화약품(000020)
    # 2nd parameter, startdate is an index of DB data.
    # 3rd parameter, period is a number of DB data from startdate. default 0 means all period.

    # Fetch
    rows = shquery.getstockprice(shcode)

    # exception of function
    if len(rows)-1 < startdate + period:
        return -1

    # create List type array
    marketdate, openprice, closeprice, highprice, lowprice = [], [], [], [], []
    for row in rows:
        marketdate.append(dates.date2num(row['marketdate']))
        openprice.append(int(row['openprice']))
        closeprice.append(int(row['closeprice']))
        highprice.append(int(row['highprice']))
        lowprice.append(int(row['lowprice']))
    j = period if period != 0 else len(rows)-1 - startdate      # set period

    # create DataFrame
    k = startdate
    graph = {'marketdate' :  marketdate[k:k+j],
             'openprice'  :  openprice[k:k+j],
             'closeprice' :  closeprice[k:k+j],
             'highprice'  :  highprice[k:k+j],
             'lowprice'   :  lowprice[k:k+j]}
    graph = DataFrame(graph)
    quotes = zip(graph['marketdate'], graph['openprice'], graph['highprice'], graph['lowprice'], graph['closeprice'])
    # print(graph)


    # Graph Drawing
    mondays = WeekdayLocator(MONDAY)            # major ticks on the mondays
    alldays = DayLocator()                      # minor ticks on the days
    weekFormatter = DateFormatter('%b %d, %Y')  # e.g., Jan 12, 2014

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.xaxis_date()
    ax.autoscale_view()
    ax.grid(True)
    
    
    ##############################################
    # 사각형그리기 연습
    # fig2 = plt.figure()
    # ax2 = fig.add_subplot(111, aspect='equal')
    ax.add_patch(
        patches.Rectangle(
            (735700, 5000),     # (x,y)
            400,            # width
            4000,            # height
            fill=False,      # remove background
            linewidth=3
        )
    )
    ##############################################
    

    candlestick_ohlc(ax, quotes, colorup="red", colordown="blue", width=0.6)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right', size=10)

    # Save graph
    filename = datetime.today().strftime("%Y%m%d_")+str(shcode)+"_"+str(startdate)+"_"+str(period)+"_"+"temp.png"    # e.g., 19931004_000020_0_0_temp.png
    filepath = "temp/"+filename
    if not os.path.isfile(filepath):
        plt.savefig(filepath, format='png')
        print("검색결과를 다음의 경로로 저장합니다. ", filename)
    else:
        print("기존의 검색결과가 존재하므로, 저장하지 않습니다. ", filename)
    plt.show()

    # End of function
    return filename

