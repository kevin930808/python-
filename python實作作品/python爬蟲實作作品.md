私立東山高中資訊科 實作作品:python爬蟲實作
==

三年信班 36號 朱晨愷
---


<br>

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
在簡單的網路爬文過後，也在自己的電腦安裝了此工具，我認文Anaconda的好處是本身就自帶了很多套件<br>
例如numpy、pandas、matplotlib等常用的套件，都不須另外用pip install進行安裝，<br>
另外一個優點是很好debug，可以分段編輯程式碼，可以分成多個部分，以增加效率。<br>

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

```
