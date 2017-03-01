import xlrd
import glob
import xlwt
import os
from Classificate import Classi

myfile = "test.xls"
if os.path.isfile(myfile):
    os.remove(myfile)
else:    ## Show an error ##
    print("Error: %s file not found" % myfile)

File_List = glob.glob('StockData/*).xls')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
sheet.write(0, 0, '기업명')
sheet.write(0, 1, '표준산업분류코드')
sheet.write(0, 2, '표준산업분류')
sheet.write(0, 3, '영업활동현금흐름') # 영업활동현금흐름
sheet.write(0, 4, '투자활동현금흐름') # 투자활동현금흐름
sheet.write(0, 5, '재무활동현금흐름') # 재무활동현금흐름
sheet.write(0, 6, '현금및현금성자산의순증가')
sheet.write(0, 7, '상장폐지여부')

cnt = 1
for filelist in File_List:
    wb = xlrd.open_workbook(filelist) # 엑셀 파일 오픈
    ws = wb.sheet_by_index(0)
    print(filelist)
    sheet_names = wb.sheet_names()
    for i in sheet_names:
        if('현금흐름표' in i):
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
    stockname = stockname.replace('StockData\\', '')
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

            tmp = ws1.row_values(i)[0].replace(" ", "")
            print("tmp: ", tmp)

            if ("영업활동현금흐름" in tmp or "영업활동으로인한현금흐름" in tmp or "영업에서창출된현금흐름" in tmp):
                NetIncome = ws1.row_values(i)[2]

                try:
                    sheet.write(cnt, 3, NetIncome)
                except:
                    pass
            elif ("투자활동현금흐름" in tmp or "투자활동으로인한현금흐름" in tmp or "투자에서창출된현금흐름" in tmp):

                NetIncome = ws1.row_values(i)[2]

                try:
                    sheet.write(cnt, 4, NetIncome)
                except:
                    pass
            elif ("재무활동현금흐름" in tmp or "재무활동으로인한현금흐름" in tmp or "재무에서창출된현금흐름" in tmp):
                NetIncome = ws1.row_values(i)[2]
                try:
                    sheet.write(cnt, 5, NetIncome)
                except:
                    pass
            elif ("현금및현금성자산의순증가" in tmp or "현금및현금성자산의순증감" in tmp or "현금의증가" in tmp or "현금및현금성자산의증가" in tmp or "현금및현금성자산의증감" in tmp or "현금및현금성자산순증가" in tmp or "현금및현금성자산의감소" in tmp or "현금의감소" in tmp or "현금및현금성자산의순증가" in tmp or "현금의증가(감소)" in tmp or "현금및현금성자산의순증가(감소)" in tmp):
                NetIncome = ws1.row_values(i)[2]
                try:
                    sheet.write(cnt, 6, NetIncome)
                except:
                    pass


            i += 1

    if (ws.row_values(3)[0] == '기 본 정 보'):
        i = 0
        while i < nlow:
            if (ws.row_values(i)[0].strip() == '표준산업분류코드'):
                code = (ws.row_values(i)[1].strip())
                Classi(code, sheet, cnt)
                sheet.write(cnt, 1, code)
            i += 1
        i = 0
        while i < nlow1:
            tmp = ws1.row_values(i)[0].replace(" ", "")
            print("tmp: ", tmp)

            if ("영업활동현금흐름" in tmp or "영업활동으로인한현금흐름" in tmp or "영업에서창출된현금흐름" in tmp):
                NetIncome = ws1.row_values(i)[2]

                try:
                    sheet.write(cnt, 3, NetIncome)
                except:
                    pass
            elif ("투자활동현금흐름" in tmp or "투자활동으로인한현금흐름" in tmp or "투자에서창출된현금흐름" in tmp):

                NetIncome = ws1.row_values(i)[2]

                try:
                    sheet.write(cnt, 4, NetIncome)
                except:
                    pass
            elif ("재무활동현금흐름" in tmp or "재무활동으로인한현금흐름" in tmp or "재무에서창출된현금흐름" in tmp):
                NetIncome = ws1.row_values(i)[2]
                try:
                    sheet.write(cnt, 5, NetIncome)
                except:
                    pass

            elif ("현금및현금성자산의순증가" in tmp or "현금및현금성자산의순증감" in tmp or "현금의증가" in tmp or "현금및현금성자산의증가" in tmp or "현금및현금성자산의증감" in tmp or "현금및현금성자산순증가" in tmp or "현금및현금성자산의감소" in tmp or "현금의감소" in tmp or "현금및현금성자산의순증가" in tmp or "현금의증가(감소)" in tmp or "현금및현금성자산의순증가(감소)" in tmp):
                NetIncome = ws1.row_values(i)[2]
                try:
                    sheet.write(cnt, 6, NetIncome)
                except:
                    pass




            i += 1
    try:
        sheet.write(cnt, 7, "1")
    except:
        pass
    cnt = cnt+1

wbk.save('test.xls')