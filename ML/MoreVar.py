import xlrd
from operator import truediv
from numpy import array
import pandas as pd
'''
wb = xlrd.open_workbook("BankruptcyStock.xls")  # 엑셀 파일 오픈
ws = wb.sheet_by_index(0)
ncol = ws.ncols
nlow = ws.nrows

print ("-------- Sheet1 --------")
print ("Number of col: " + str(ncol))
print ("Number of low: " + str(nlow))

print ("-------- Values of low --------")
i = 0
print(ws.row_values(0))
print("------------------")
print(ws.col_values(4)[1:])
print(ws.col_values(5)[1:])

a = array(ws.col_values(4)[1:])
b = array(ws.col_values(5)[1:])
print(a/b)
'''
df = pd.read_excel('BankruptcyStock.xls')
df1 = pd.read_excel('BankruptcyStock.xls', header=None)
xy = df.as_matrix().transpose()


VarList = xy[4:-1]
Bankruptcy = xy[-1]
print(VarList[6])
print(len(VarList))