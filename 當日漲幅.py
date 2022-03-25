import requests
from bs4 import BeautifulSoup
r = requests.get('https://tw.stock.yahoo.com/rank/change-up/')
soup = BeautifulSoup(r.text, 'lxml')
name = soup.select('li[class="List(n)"]')
for i in name:
    print(i.text)
    print(' ')
####當日漲幅排行 