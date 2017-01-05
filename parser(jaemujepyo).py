import urllib.request
from bs4 import BeautifulSoup
code =['005930']
for c in code:
    url="http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A"+c+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"

    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')
    print('----------------------------------------------')
    cells = soup.find('tr').find_all('th')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('EPS')
    cells = soup.find('tr', {'id': "p_grid1_6"}).find_all('td')
    print(cells)
    for cell in cells:
        print (cell.string)

