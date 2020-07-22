import requests
from bs4 import BeautifulSoup
import json
from .abstract_class.crawler import Crawler

class ChessCrawler(Crawler):
  # with encode='utf-8'
  chess_url_utf8 = {
    # 中華民國西洋棋協會
    "chess_news": "https://www.chinesetaipeichess.com.tw/Portal/" # 台灣西洋棋最新消息
  }
  
  def fetchHTML(self):
    url = self.chess_url_utf8['chess_news']
    # 考慮做 loop
    response = requests.get(url)
    response.encoding = 'utf-8'
    # html.parser
    # Batteries included, Decent speed (不錯的速度), Lenient (寬容)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

  # 分析中華民國西洋棋協會訊息
  def parseChessNews(self):
    # all topics
    soup = self.fetchHTML()
    topics = soup.select("div.pt-cv-wrapper div.pt-cv-ifield")
    data = {'ChessNews':[]}
    index = 1
    # 最新棋訊
    for topic in topics:
      # set range
      if index == 3: # catch first 2 index
        break
      # each row in tag (<tr>) is a dict
      temp_dic = {}
      temp_dic['id'] = str(index)
      temp_dic['title'] = '[Chess] (' + topic.find('time').text.strip() + ') ' + topic.find('a', class_='_self').text.strip()
      temp_dic['href'] = topic.find('a', class_='_self').get('href')
      # append to data dict (key:GoProInfo, value:array)
      data['ChessNews'].append(temp_dic)
      index = index + 1

    # return a dict
    return data