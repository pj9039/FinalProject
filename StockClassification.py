import xlrd # 엑셀 파일을 읽기 위한 모듈
import glob # 경로에 대응되는 모든 파일을 쓰기위한 모듈
import xlwt # 엘셀 파일을 쓰기 위한 모듈
import os # 파일을 다루기 위한 모듈
from Classificate import Classi # 표준산업분류코드 분류를 위한 모듈

myfile = "BankruptcyStock.xls" # 결과적으로 나올파일
if os.path.isfile(myfile): # 기존에 파일이 있으면
    os.remove(myfile) # 삭제
else:
    print("Error: %s file not found" % myfile) # 없으면 없다고 표시

File_List = glob.glob('StockData/*).xls') # StockData 폴더에 있는 모든 엑셀 데이터불러오기
wbk = xlwt.Workbook() # 엑셀파일을 쓸 변수
sheet = wbk.add_sheet('sheet 1') # 시트이름을 sheet 1
## 엑셀 1행에 쓰기 단위는 원, 상장폐지된 종목은 1 안된 종목은 0 ##
sheet.write(0, 0, '기업명')
sheet.write(0, 1, '표준산업분류코드')
sheet.write(0, 2, '표준산업분류')
sheet.write(0, 3, '영업활동현금흐름')
sheet.write(0, 4, '투자활동현금흐름')
sheet.write(0, 5, '재무활동현금흐름')
sheet.write(0, 6, '현금및현금성자산의순증가')
sheet.write(0, 7, '상장폐지여부')
cnt = 1 # 행
for filelist in File_List:
    wb = xlrd.open_workbook(filelist) # 엑셀 파일 오픈
    ws = wb.sheet_by_index(0) # 불러온 엑셀 파일의 첫번째 시트
    print(filelist)
    sheet_names = wb.sheet_names()
    # 시트이름이 현금흐름표인것을 찾는다
    for i in sheet_names:
        if('현금흐름표' in i):
            IncomeStatement = i
    ws1 = wb.sheet_by_name(IncomeStatement) # 현금흐름표시트를 저장하는 변수
    # 첫번째 시트(기본정보)의 최대 행과 열
    ncol = ws.ncols
    nlow = ws.nrows
    # 선택 시트(현금흐름표)의 최대 행과 열
    ncol1 = ws1.ncols
    nlow1 = ws1.nrows
    # 종목명을 입력하기위해 파일이름을 쓰는데 확장자와 년도를 빼는 작업
    stockname = filelist.replace('.xls', '')
    stockname = stockname.replace('(2015)','')
    stockname = stockname.replace('(2014)','')
    stockname = stockname.replace('(2013)','')
    stockname = stockname.replace('(2012)','')
    stockname = stockname.replace('StockData\\', '')
    sheet.write(cnt, 0, stockname) # 종목명을 1열에 입력한다.

    # 엑셀파일마다 형식이 달라서 2행1열의 부분이 '문서정보'인 것과 '기 본 정 보'인 파일을 나누어서 표준산업분류코드를 찾는다.
    if (ws.row_values(1)[0] == '문서정보'):
        i = 0
        j = 0
        # 최대 행길이 까지 루프
        while i < nlow:
            if("표준산업분류코드" in ws.row_values(i)[0]):
                code = (ws.row_values(i)[0]).split()[2].strip()
                Classi(code,sheet,cnt)
                sheet.write(cnt, 1, code)
            i += 1
    if (ws.row_values(3)[0] == '기 본 정 보'):
        i = 0
        while i < nlow:
            if (ws.row_values(i)[0].strip() == '표준산업분류코드'):
                code = (ws.row_values(i)[1].strip())
                Classi(code, sheet, cnt)
                sheet.write(cnt, 1, code)
            i += 1
    i=0
    # 현금흐름표의 최대 행까지 루프
    while i < nlow1:
        tmp = ws1.row_values(i)[0].replace(" ", "") # 영업활동 현금 흐름 처럼 띄어쓰기되어있는것을 띄어쓰기 제거
        print("tmp: ", tmp)
        # 영업활동현금흐름 부분을 찾고 기록
        if ("영업활동현금흐름" in tmp or "영업활동으로인한현금흐름" in tmp or "영업에서창출된현금흐름" in tmp):
            NetIncome = ws1.row_values(i)[2]
            try:
                sheet.write(cnt, 3, NetIncome)
            except:
                pass
        # 투자활동현금흐름 부분을 찾고 기록
        elif ("투자활동현금흐름" in tmp or "투자활동으로인한현금흐름" in tmp or "투자에서창출된현금흐름" in tmp):
            NetIncome = ws1.row_values(i)[2]
            try:
                sheet.write(cnt, 4, NetIncome)
            except:
                pass
        # 재무활동현금흐름 부분을 찾고 기록
        elif ("재무활동현금흐름" in tmp or "재무활동으로인한현금흐름" in tmp or "재무에서창출된현금흐름" in tmp):
            NetIncome = ws1.row_values(i)[2]
            try:
                sheet.write(cnt, 5, NetIncome)
            except:
                pass
        # 현금및현금성자산의순증가 부분을 찾고 기록
        elif ("현금및현금성자산의순증가" in tmp or "현금및현금성자산의순증감" in tmp or "현금의증가" in tmp or "현금및현금성자산의증가" in tmp or "현금및현금성자산의증감" in tmp or "현금및현금성자산순증가" in tmp or "현금및현금성자산의감소" in tmp or "현금의감소" in tmp or "현금및현금성자산의순증가" in tmp or "현금의증가(감소)" in tmp or "현금및현금성자산의순증가(감소)" in tmp):
            NetIncome = ws1.row_values(i)[2]
            try:
                sheet.write(cnt, 6, NetIncome)
            except:
                pass
        i += 1
    try:
        sheet.write(cnt, 7, "1") # StockData폴더에 있는 종목들은 다 상장폐지된 종목이기 때문에 상장폐지가 되었다는 의미로 1를 입력
    except:
        pass
    cnt = cnt+1
wbk.save('BankruptcyStock.xls') # 지금까지 쓴 엑셀데이터 저장