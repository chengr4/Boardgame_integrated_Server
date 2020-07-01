import requests
from bs4 import BeautifulSoup
from datetime import datetime

# today's date
dateime_now = datetime.now()

# main list to crawl
main_url = []
article_href = []

# push numbers setting
push_numbers = 10

# title adn content
title = ""
## 還沒決定用途，之後可能刪除或更新
content = "\n"

# 擷取網站
def fetchHTML(url, encode='utf-8'):
  response = requests.get(url)
  response.encoding = encode
  #response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
  # html.parser
  # Batteries included, Decent speed (不錯的速度), Lenient (寬容)
  soup = BeautifulSoup(response.text, "html.parser")
  return soup

# 被擷取的網站
## 中華民國圍棋協會
url_go_news = 'http://www.weiqi.org.tw/class_list.asp' #最新動態
url_go_contest= 'http://www.weiqi.org.tw/f_m-inc.asp' # 比賽成績 + 比賽資訊
# 海峰棋院
url_go_proinfo= 'https://www.haifong.org/' # 比賽成績 + 比賽資訊



# 分析海峰棋院訊息
def parseGoProInfo(soup):
  # all topics
  topics = soup.select("div#index-news li")
  for topic in topics:
    print(topic.find('span').text.strip() + "\t"
    + topic.find('a').text.strip())

# not finish 預訂回傳整個網址
def parseGoContest(soup):
  pass
  # all topics
  #topics = soup.select(".base01")
  #return topics

# 分析中華圍棋協會
def parseGoNews(soup):
    # all topics
    topics = soup.select("tr")
    # the first and the second important messages
    print(topics[1].text)  
    print(topics[2].text)

def run_result():
  resp_GoProInfo = fetchHTML(url_go_proinfo)
  parseGoProInfo(resp_GoProInfo)

if __name__ == "__main__":
  resp_GoNews = fetchHTML(url_go_news, encode='big5-hkscs')
  resp_GoContest = fetchHTML(url_go_contest, encode='big5-hkscs')
  resp_GoProInfo = fetchHTML(url_go_proinfo)
  #parseGoNews(resp_GoNews)
  parseGoProInfo(resp_GoProInfo)
  # parseGoContest(resp_GoContest) -> 改直接傳整個網址

        