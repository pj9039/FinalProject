import matplotlib.pyplot as plt
import numpy
import time
from scipy.stats import pearsonr
from fastpip import pip
import Pattern.QueryStockdata as shquery
import Pattern.PatternType as pttype


# Pattern Finder
def findpattern(p_type, p_low, p_high, period):
    # p_type : pattern type index
    # p_low : low price; it's used to search shcode
    # p_high : high price; it's used to search shcode
    # period : pattern period
    start_time = time.time()

    compare, n = pttype.patterntype(p_type)         # choose pattern by p_type
    rows = shquery.makequerylist(p_low, p_high)     # stock filtering
    print("p_low=", p_low, "와 p_high=", p_high, " 조건에 부합한 종목코드 : ", rows)
    data_array = []
    for row in rows:                           # each stock
        tmps = shquery.getstockprice(row)       # get stock data from DB
        temp_array = []     # stock price data
        pip_array = []      # list of found index
        i = -1
        for tmp in tmps:   # append data for PIP
            i += 1
            temp_array.append([i, int(tmp['closeprice'])])

        for k in range(0, len(temp_array) - period):    # find relevant index
            result = pip(temp_array[k:k + period], n)
            r_row, p_value = pearsonr(numpy.array(result)[:, 1], numpy.array(compare)[:, 1])
            if r_row > 0.7:
                print("종목코드 ", row, "에서 index가 ", k, "일 때, 피어슨상관계수 : ", r_row)
                pip_array.append(k)  # k is index

        # fill data
        data_array.append(row)
        data_array.append(pip_array)

    print("┌기간=", period, "에서 패턴발견 알고리즘 적용결과 리스트 구현")
    print(data_array)
    # measure of running-time
    print("--- processing time : %s seconds ---" % (time.time() - start_time))

    return data_array
