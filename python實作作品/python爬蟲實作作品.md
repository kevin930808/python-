私立東山高中資訊科 實作作品:python爬蟲實作
==

三年信班 36號 朱晨愷
---


若要直接到研究成果[點我](https://reurl.cc/jkA2Dm)<br>



研究動機:
---
  結合數學科的數據分析及股票分析之探討應用，想自己藉由網路自學和老師的指導，<br>
試著寫出具有簡單功能的python股票爬蟲程式，並在github上發布，與更多的進行交流，<br>
我相信學完這個之後對於大學的相關資料處理課程具有非常大的幫助。<br>

研究方法:
----
  在網路上即github搜尋相關的教材，並到Beautiful Soup 和 Requests的官網學習(本報告中使用的兩個python套件)，<br>
雖然自己沒有學過html相關的語法，但在查閱範例(官方範例及其他人的作品)的時候也大概的知道要<br>
如何使用soup.select和soup.find的語法使用，於是自己不斷的修正錯誤，在過程之中也出現了很多的bug，<br>
但也都逐一修正並且優化程式碼。<br>

研究工具:
-----
  我個人在學習python之初，有問過家教老師及網路爬文有那些較好的python編譯器，<br>
發現蠻有豐富經驗或一些相關科系的大學生，都推薦使用anaconda的jupyterLab，<br>
在簡單的網路爬文過後，也在自己的電腦安裝了此工具，我認為Anaconda的好處是本身就自帶了很多套件<br>
例如numpy、pandas、matplotlib等常用的套件，都不須另外用pip install進行安裝，<br>
另外一個優點是jupythr lab很好debug，可以分段編輯程式碼，可以分成多個部分，以增加效率。<br>

  利用網路上的資源，我查詢了很多python爬蟲的教學，但幾乎都是大同小異，有些甚至是搬運網站<br>
在不同的網站，但內容卻都相同，最後選擇了也是github上其他人分享的教學資料，也到了Beautiful Soup的官方文檔<br>
查閱相關的語法。

 這次的實作作品所爬蟲的網站是yahoo股市，簡單的利用右鍵檢查抓取股票的名字、代碼、價錢、漲幅，並顯示出來。

研究過程:
-----
在學習soup.select和soup.find時，我不太懂要怎麼讓程式知道我要抓的tag是什麼。<br>
第一個問題是在使用select時，會出錯錯誤。<br>
原本的使用方法如下:<br>
```html
s1 = """
<body>

<h1>哈囉！HTML！</h1>

<div class="class1">
    <p>這是第一個p標籤內容！</p>
    <p>這是第二個p標籤內容！</p>
</div>

<div class="class2">
    <p>這是第三個p標籤內容！</p>
    <p>這是第四個p標籤內容！</p>
</div>
</body>
```
我需要抓取class="class1"的tag
所以是
```python
soup1 = BeautifulSoup(s1)
soup1.select('div.class1 p')
```
但如果class="我是class" 的"我是class"當中有"("時就會出現錯誤。<br>
我自己摸索出來的解決方法是 改成如下<br>
```python
soup1 = BeautifulSoup(s1)
soup1.select('div[class="class1"] p')
```
這樣的方法不管是class裡面是什麼都可以使用<br>

第二個問題為都是抓取同一個資料的tag但卻有不同的時候<br>
從yahoo股市的網頁碼來看<br>
(此為擷取一小段)<br>
```html
<div class="D(f) Ai(fe) Mb(4px)">
  <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">597</span>
  <span class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)">
    <span class="Mend(4px) Bds(s)" style="border-color:transparent transparent #ff333a transparent;border-width:0 6.5px 9px 6.5px"></span>
    "8"
  </span>
  <span class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)">(1.36%)</span>
</div>
```
我需要抓取的部分為價錢也就是<br>
```html
<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">597</span>
```
我使用select<br>
```python
price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"]')[0].text
#text為擷取純文字 tag裡的內容
```
但如果股票不是漲而是跌會變成
```html
<div class="D(f) Ai(fe) Mb(4px)">
  <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)">597</span>
  <span class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)">
    <span class="Mend(4px) Bds(s)" style="border-color:transparent transparent #ff333a transparent;border-width:0 6.5px 9px 6.5px"></span>
    "8"
  </span>
  <span class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-down)">(1.36%)</span>
</div>
#其中的trend-up會因跌而變成trend-down
```
以至於不能當使用者輸入的標的為跌時，程式無法輸出而是顯示錯誤<br>
我的解決辦法是利用try except去解決報錯的問題<br>
方法如下(簡化):<br>
```python
try:
    price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"]')[0].text
    print(price)
except:
    price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    print(price) 
```

於是第一版自製爬蟲程式就成功製作出來了!!!!<br>
研究成果:
------
第一版爬蟲程式(簡稱V1)<br>
```python
import requests
from bs4 import BeautifulSoup
#以上為導入requests 及 BeautifulSoup的套件
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
#使用者輸入yahoo股市個股的網址，並利用"lxml"解譯利用requests.get得到的html以利於BeautifulSoup進行後續的select
try:
    name = soup.select('h1[class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)"]')[0].text
    num = soup.select('span[class="C($c-icon) Fz(24px) Mend(20px)"]')[0].text
    price = soup.select('span[class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    down = soup.select('span[class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)"]')[0].text
    percents= soup.select('span[class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-down)"]')[0].text
    #指定個股名稱、股票代碼、價格、跌幅、漲跌的百分比，並print出來
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
    #指定個股名稱、股票代碼、價格、漲幅、漲跌的百分比，並print出來
#####東山高中三年信班朱晨愷v1#####
```
輸出範例如下:<br>
![](https://github.com/kevin930808/python-/blob/main/%E5%9C%96%E7%89%87%E6%AA%94/v1%E8%BC%B8%E5%87%BA%E7%AF%84%E4%BE%8B.png)<br>
但此程式還是有一些BUG，當個股是在漲停板或是跌停板時，其中的價錢的tag如下:<br>
```html
<div class="D(f) Ai(fe) Mb(4px)">
  <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) C(#fff) Px(6px) Py(2px) Bdrs(4px) Bgc($c-trend-up)">162.5</span>
  <span class="Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"><span class="Mend(4px) Bds(s)" style="border-color:transparent transparent #ff333a transparent;border-width:0 6.5px 9px 6.5px"></span>14.5
  </span>
  <span class="Jc(fe) Fz(20px) Lh(1.2) Fw(b) D(f) Ai(c) C($c-trend-up)">(9.80%)</span></div>
```
可以觀察到其中價錢的部分:<br>
```html
<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) C(#fff) Px(6px) Py(2px) Bdrs(4px) Bgc($c-trend-up)">162.5</span>
#多了 C(#fff) 
#我認為應該是在漲停或跌停時，價錢的顯示方式不同
```
所以V1程式在使用者輸入的個股為漲廷或跌停時是顯示不出來的(會出現錯誤)<br>
若要修正此錯誤，就需要再另外新增一個try except去除錯，但我覺得有點太複雜了，<br>
所以在價格的部分我用了find來取代select。<br>
第二版爬蟲程式(簡稱V2)<br>
```python
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
print('目前價位為',price,'元')
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
```
註1:
```python
infos = soup.find('div',{'class':"D(f) Ai(fe) Mb(4px)"}).find_all('span')
#指定infos為div class="D(f) Ai(fe) Mb(4px)"裡所有tag為<span>的項目
```
V2輸出如下圖:<br>
![](https://github.com/kevin930808/python-/blob/main/%E5%9C%96%E7%89%87%E6%AA%94/V2%E8%BC%B8%E5%87%BANEW.png)<br>
這次的v2版本不論漲停或跌停，都可以輸出給使用需要的者個股資訊。<br>

結果反思:
---
<br>
  我認為我所製作的爬蟲程式可以再做得更多功能，可以讓使用者知道更多的資訊，如成交量、最高價、最低價等，<br>
可以製作一個迴圈讓使用者可以一次輸入更多筆的網址，來得到更多的個股資訊。<br>
我認為還有一個缺點就是可以去學習如何讓輸入和輸出的介面可以圖形化，而不是一般的輸入方法，<br>
可以試著打包成exe檔，有一個互動的程式出來。<br>
  <br>
  此作品也有跟fb及其他社群媒體的程式社團交流，也知道這個作品的實際效用可能不大，<br>
因為有些網站有提供api可以使用，但我還不太瞭解如鶴調用api以抓取我想要的數據<br>
希望在大學時能學到更多的語法及理論，來提升自己的實力。<br>

參考資料:
---
[Beautiful Soup官方文檔](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)<br>
[github上的教學](https://github.com/victorgau/python_crawler)<br>

