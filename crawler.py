import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

# today's date
dateime_now = datetime.now()

# main list to crawl
main_url = {
  # 中華民國圍棋協會
  "go_news": "http://www.weiqi.org.tw/class_list.asp", #最新動態
  "go_contest": "http://www.weiqi.org.tw/f_m-inc.asp", # 比賽成績 + 比賽資訊
  # 海峰棋院
  "go_proinfo": "https://www.haifong.org/" # 比賽成績 + 比賽資訊
}

# push numbers setting
push_numbers = 10

# 擷取網站
def fetchHTML(url, encode='utf-8'):
  response = requests.get(url)
  response.encoding = encode
  # html.parser
  # Batteries included, Decent speed (不錯的速度), Lenient (寬容)
  soup = BeautifulSoup(response.text, "html.parser")
  return soup





# 分析海峰棋院訊息
def parseGoProInfo(soup):
  # all topics
  topics = soup.select("div#index-news li")
  data = {'GoProInfo':[]}
  
  # 最新棋訊
  for topic in topics:
    # each row is a dict
    temp_dic = {}
    temp_dic[topic.find('span').text.strip()]= topic.find('h3', class_='entry-title').find('a').text.strip()
    # append to data dict (key:GoProInfo, value:array)
    data['GoProInfo'].append(temp_dic)

  # convert to json format
  data_json = json.dumps(data, ensure_ascii=False)
  return data_json

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

# convert generator to list
'''class StreamArray(list):
  def __iter__(self):
    resp_GoProInfo = fetchHTML(main_url["go_proinfo"])
    return parseGoProInfo(resp_GoProInfo)
  
  def __len__(self):
    return 1'''

# run result of what I crawl
def run_result():
  #info_list = StreamArray()
  #result = json.dumps(info_list)
  resp_GoProInfo = fetchHTML(main_url["go_proinfo"])
  result = parseGoProInfo(resp_GoProInfo)
  
  return result

if __name__ == "__main__":
  #resp_GoNews = fetchHTML(main_url['go_news'], encode='big5-hkscs')
  #parseGoNews(resp_GoNews)

  #resp_GoContest = fetchHTML(main_url['go_contest'], encode='big5-hkscs')
  # parseGoContest(resp_GoContest) -> 改直接傳整個網址

  print(run_result())
  
  
  

        