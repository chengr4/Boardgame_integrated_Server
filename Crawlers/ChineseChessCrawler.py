import requests
from bs4 import BeautifulSoup
import json

class ChineseChessCrawler():
  # with encode='utf-8'
  chinese_chess_url_utf8 = {
    # 海峰棋院
    "chinese_chess_news": "http://www.cccs.org.tw/front/bin/home.phtml" # 象棋最新消息
  }

  # 擷取網站 + response html format
  def fetchHTML(self):
    url = self.chinese_chess_url_utf8['chinese_chess_news']
    # 考慮做 loop
    response = requests.get(url)
    response.encoding = 'utf-8'
    # html.parser
    # Batteries included, Decent speed (不錯的速度), Lenient (寬容)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

  # 分析中華民國象棋文化協會訊息
  '''def parseGoProInfo(self, soup):
    # all topics
    topics = soup.select("div#index-news li")
    data = {'GoProInfo':[]}
    index = 1
    # 最新棋訊
    for topic in topics:
      # each row is a dict
      temp_dic = {}
      temp_dic['id'] = str(index)
      temp_dic['title'] = '[Go]'+topic.find('span').text.strip()
      temp_dic['source'] = topic.find('h3', class_='entry-title').find('a').text.strip()
      temp_dic['href'] = topic.find('h3', class_='entry-title').find('a').get('href')
      # append to data dict (key:GoProInfo, value:array)
      data['GoProInfo'].append(temp_dic)
      index = index + 1

    # convert to json format
    data_json = json.dumps(data, ensure_ascii=False)
    return data_json'''