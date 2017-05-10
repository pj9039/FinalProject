from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.patches as patches
from pandas import DataFrame
from datetime import datetime
import os
import Pattern.QueryStockdata as shquery


# Draw real candlestick chart
def drawgraph(shcode, startdate=0, period=0, discover=None, pearson=None):
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
    # ax.xaxis.set_major_locator(mondays)
    # ax.xaxis.set_minor_locator(alldays)
    # ax.xaxis.set_major_formatter(weekFormatter)
    ax.xaxis_date()
    ax.autoscale_view()
    ax.grid(True)

    # print(graph['marketdate'][396])
    if discover is not None:
        if len(discover) != len(pearson):
            return -1;

        j = -1
        for i in discover:
            j += 1

            ymin, ymax = graph['highprice'][i], graph['lowprice'][i]    # initialize
            for n in range(i, i+30):
                ymin = min(ymin, graph['lowprice'][n])                  # min value
                ymax = max(ymax, graph['highprice'][n])                 # max value

            ax.set_title("Stock Code: "+shcode)                         # set graph title
            ax.text(graph['marketdate'][i], ymax, str(float("{0:.2f}".format(pearson[j]*100)))+"%", fontsize=8)    # print similarity percent (limiting floats to four decimal points)
            if i+(30*2) < len(rows)-1:
                earning = ((int(graph['closeprice'][i+50]) - int(graph['closeprice'][i+30])) / int(graph['closeprice'][i+30])) * 100     # calculate earning ratio
                earning = round(earning, 2)
                ax.text(graph['marketdate'][i+50], graph['highprice'][i+50]+250, str(earning)+"%",color='green', fontsize=8)  # print earning ratio

            # Draw Rectangle
            # ax.text(graph['marketdate'][i], ymax - ymin, str(pearson[j])+"%")  # print earning ratio
            ax.add_patch(
                patches.Rectangle(
                    (graph['marketdate'][i], ymin),                      # (x,y)
                    graph['marketdate'][i+30] - graph['marketdate'][i],  # width
                    ymax - ymin,                                         # height
                    fill=False,                                         # remove background
                    linewidth=1
                )
            )

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


# execute as main
if __name__ == "__main__":
    drawgraph('200050', 0, 0, [103, 177, 265, 294, 296, 319, 320, 431, 447],
              [0.7858, 0.7068, 0.7511, 0.7452, 0.822, 0.7396, 0.7363, 0.7014, 0.7139])
    # drawgraph('200050')
# ['200050', [103, 177, 265, 294, 296, 319, 320, 431, 447], [0.7858, 0.7068, 0.7511, 0.7452, 0.822, 0.7396, 0.7363, 0.7014, 0.7139]]
