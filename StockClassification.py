import xlrd
import glob
import xlwt
from Classification.Classificate import Classi

File_List = glob.glob('../StockData/*).xls')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
sheet.write(0, 0, '기업명')
sheet.write(0, 1, '표준산업분류코드')
sheet.write(0, 2, '표준산업분류')
sheet.write(0, 3, '당기순이익') # 당기순이익
cnt = 1

for filelist in File_List:
    wb = xlrd.open_workbook(filelist)

    ws = wb.sheet_by_index(0)
    print(filelist)
    sheet_names = wb.sheet_names()
    #print('Sheet Names', sheet_names)
    for i in sheet_names:
        if('손익계산서' in i):
            IncomeStatement = i

    ws1 = wb.sheet_by_name(IncomeStatement)

    ncol = ws.ncols
    nlow = ws.nrows
    ncol1 = ws1.ncols
    nlow1 = ws1.nrows

    stockname = filelist.replace('.xls', '')
    stockname = stockname.replace('(2015)','')
    stockname = stockname.replace('(2014)','')
    stockname = stockname.replace('(2013)','')
    stockname = stockname.replace('(2012)','')
    stockname = stockname.replace('../StockData\\', '')

    sheet.write(cnt, 0, stockname)

    if (ws.row_values(1)[0] == '문서정보'):
        i = 0
        j = 0
        while i < nlow:

            if("표준산업분류코드" in ws.row_values(i)[0]):
                code = (ws.row_values(i)[0]).split()[2].strip()

                Classi(code,sheet,cnt)
                sheet.write(cnt, 1, code)
            i += 1
        i=0
        while i < nlow1:
            #if ("당기순이익" in ws1.row_values(i)[0] or "당기순손익" in ws1.row_values(i)[0] or "당기총포괄손익" in ws1.row_values(i)[
                #0] or "당기이익 및 기타 포괄손익" in ws1.row_values(i)[0] or "당기손익" in ws1.row_values(i)[0] or "당기순손실" in
                #ws1.row_values(i)[0]):
            if ("매출액" in ws1.row_values(i)[0]):
                NetIncome = ws1.row_values(i)[2]
                print(ws1.cell_value(1, 0))
                print(NetIncome)
                try:
                    sheet.write(cnt, 3, NetIncome)
                except:
                    pass
            i += 1


    if (ws.row_values(3)[0] == '기 본 정 보'):
        i = 0
        while i < nlow:
            if (ws.row_values(i)[0].strip() == '표준산업분류코드'):
                code = (ws.row_values(i)[1].strip())
                Classi(code, sheet, cnt)
                print(code)
                sheet.write(cnt, 1, code)
            i += 1

        i = 0
        while i < nlow1:
            #if ("당기순이익" in ws1.row_values(i)[0] or "당기순손익" in ws1.row_values(i)[0] or "당기총포괄손익" in ws1.row_values(i)[0] or "당기이익 및 기타 포괄손익" in ws1.row_values(i)[0] or "당기손익" in ws1.row_values(i)[0] or "당기순손실" in ws1.row_values(i)[0]):
            if ("매출액" in ws1.row_values(i)[0]):
                NetIncome = ws1.row_values(i)[2]
                print(NetIncome)
                try:
                    sheet.write(cnt, 3, NetIncome)
                except:
                    pass
            i += 1

    cnt = cnt+1

wbk.save('test.xls')