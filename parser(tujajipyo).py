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
    print('EPS')
    cells = soup.find('tr', {'id': "p_grid1_1"}).find_all('td')
    print(cells)
    for cell in cells:
        print (cell.string)
    print('----------------------------------------------')
    print('EBITDAPS')
    cells = soup.find('tr', {'id': "p_grid1_2"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('CFPS')
    cells = soup.find('tr', {'id': "p_grid1_3"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('SPS')
    cells = soup.find('tr', {'id': "p_grid1_4"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('BPS')
    cells = soup.find('tr', {'id': "p_grid1_5"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)

    print('----------------------------------------------')
    print('DPS')
    cells = soup.find('tr', {'id': "p_grid1_6"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)

    print('----------------------------------------------')
    print('배당성향')
    cells = soup.find('tr', {'id': "p_grid1_8"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('PER')
    cells = soup.find('tr', {'id': "p_grid1_9"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('PCR')
    cells = soup.find('tr', {'id': "p_grid1_10"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('PSR')
    cells = soup.find('tr', {'id': "p_grid1_11"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)

    print('----------------------------------------------')
    print('PBR')
    cells = soup.find('tr', {'id': "p_grid1_12"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)
    print('----------------------------------------------')
    print('EV/EBITDA')
    cells = soup.find('tr', {'id': "p_grid1_14"}).find_all('td')
    print(cells)
    for cell in cells:
        print(cell.string)


