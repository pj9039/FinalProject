import urllib.request
from bs4 import BeautifulSoup
import DataDeclare
code =['005930']
for c in code:
    url="http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A"+c+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"
    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')
    '''
    print('----------------------------------------------')
    cells = soup.find('tr').find_all('th')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('EPS')
    cells = soup.find('tr', {'id': "p_grid1_4"}).find_all('td')
    print(cells)
    for cell in cells:
        print (cell.string)
    '''
    print('----------------------------------------------')
    cells = soup.find('div', {'id': "divSonikY"}).find_all('td')
    #print(cells)
    a = []
    for cell in cells:
        #print (cell.string)
        a.append(cell.string)
    print(a)
    print(len(a))
    matrix = DataDeclare.setmatrix()
    k=0
    for i in range(0,74):
        for j in range(1,7):
            if a[(j-1)+k]!="\xa0":
                matrix[i][j] = a[(j-1)+k]
            if a[(j-1)+k]=="\xa0":
                matrix[i][j] = 0
        if k!=422:
            k=k+6
    for row in matrix:
        print(row)




