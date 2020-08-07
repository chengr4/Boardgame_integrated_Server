import requests
from bs4 import BeautifulSoup
import json
from .abstract_class.crawler import Crawler
import uuid

class ChineseChessCrawler(Crawler):
  # with encode='utf-8'
  chinese_chess_url_utf8 = {
    # 中華民國象棋文化協會d
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
  def parseChineseChessNews(self):
    # all topics
    soup = self.fetchHTML()
    topics = soup.select("table.user_3 tr")
    data = {'ChineseChessNews':[]}
    position = 0
    # 最新棋訊
    for topic in topics:
      # set range
      if position == 3: # catch first 2 index
        break
      # each row in tag (<tr>) is a dict
      temp_dic = {}
      temp_dic['id'] = str(uuid.uuid4())
      temp_dic['title'] = '[Chinese chess] ' + topic.find('a').text.strip()
      temp_dic['href'] = 'http://www.cccs.org.tw/front/bin/' + topic.find('a', class_='special-link').get('href')
      # append to data dict (key:GoProInfo, value:array)
      data['ChineseChessNews'].append(temp_dic)
      position = position + 1

    # return a dict
    return data