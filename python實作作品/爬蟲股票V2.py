import requests
from bs4 import BeautifulSoup
#以上為導入requests 及 BeautifulSoup的套件
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#使用者輸入yahoo股市個股的網址，並利用"lxml"解譯利用requests.get得到的html以利於BeautifulSoup進行後續的select和find
infos = soup.find('div',{'class':"D(f) Ai(fe) Mb(4px)"}).find_all('span')
#註1
price= infos[0].text
#這邊的做法是不管是漲跌或是漲停板都可以抓到數值
name=soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
num=soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
time=soup.select('span[class="C(#6e7780) Fz(12px) Fw(b)"]')[0].text
print('為',time)
print('該標的為',name,num)
print('目前價位為',price)
 #指定時間、個股名稱、個股代碼、目前價位，並print出來
try:
    
    down = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-down)"]')[0].text
    #指定跌幅、漲跌的百分比，並print出來
    print('跌',down,'元',percents)
    
except:
    up = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)"]')[0].text
    print('漲',up,'元',percents)
    #指定跌幅、漲跌的百分比，並print出來
#####東山高中三年信班朱晨愷v2#####
