import urllib.request
from bs4 import BeautifulSoup
code =['005930']
for c in code:
    url="http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A"+c+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701%22"

    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')
    print('----------------------------------------------')
    cells = soup.find('tr').find_all('th')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    cells = soup.find('tr', {'id': "p_grid1_1"}).find_all('td')
    print(cells)
    for cell in cells:
        print (cell.string)
    print('----------------------------------------------')
    cells = soup.find_all('tbody')[0].find_all('div')
    print(cells)
    for cell in cells:
        print (cell.string)
    print('----------------------------------------------')
    cells = soup.find('tbody').find_all('td')
    print(cells)
    print(len(cells))
    a=[]
    for cell in cells:
        print(cell.string)
        a.append(cell.string)
    print(a)
    print(len(a))
    juga=[]
    sichong=[]
    per=[]
    pbr=[]
    for i in range(0,10):
        juga.append(a[i])
    print(juga)
    print(len(juga))
