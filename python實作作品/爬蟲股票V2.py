import requests
from bs4 import BeautifulSoup
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#使用者輸入yahoo股市個股的網址，並利用"lxml"解譯利用requests.get得到的html以利於BeautifulSoup進行後續的select和find
infos = soup.find('div',{'class':"D(f) Ai(fe) Mb(4px)"}).find_all('span')
#註1
price= infos[0].text
try:
    name = soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
    num = soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
    down = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-down)"]')[0].text
    print('該標的為')
    print(name,num)
    print('價錢為')
    print(price,'跌',down,percents)
    #指定個股名稱、股票代碼、跌幅、漲跌的百分比，並print出來
except:
    name = soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
    num = soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
    up = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)"]')[0].text
    print('該標的為')
    print(name,num)
    print('價錢為')
    print(price,'漲',up,percents)
    #指定個股名稱、股票代碼、漲幅、漲跌的百分比，並print出來
 #####東山高中三年信班朱晨愷v2
