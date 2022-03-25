import requests
from bs4 import BeautifulSoup
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
try:
    name = soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
    num = soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
    price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    down = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-down)"]')[0].text
    print('該標的為')
    print(name,num)
    print('價錢為')
    print(price,'跌',down,percents)
    
except:
    name = soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
    num = soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
    price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"]')[0].text
    up = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)"]')[0].text
    print('該標的為')
    print(name,num)
    print('價錢為')
    print(price,'漲',up,percents)
#####東山高中三年信班朱晨愷v1
