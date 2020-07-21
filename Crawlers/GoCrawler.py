import requests
from bs4 import BeautifulSoup
import json

class GoCrawler():

  # with encode='utf-8'
  go_url_utf8 = {
    # 海峰棋院
    "go_proinfo": "https://www.haifong.org/" # 比賽成績 + 比賽資訊
  }

  # with encode='big5-hkscs'
  go_url_big5 = {
    # 中華民國圍棋協會
    "go_news": "http://www.weiqi.org.tw/class_list.asp", #最新動態
    "go_contest": "http://www.weiqi.org.tw/f_m-inc.asp", # 比賽成績 + 比賽資訊
  }
  

  # 擷取網站 + response html format
  def fetchHTML(self):
    url = self.go_url_utf8['go_proinfo']
    # 考慮做 loop
    response = requests.get(url)
    response.encoding = 'utf-8'
    # html.parser
    # Batteries included, Decent speed (不錯的速度), Lenient (寬容)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


  # 分析海峰棋院訊息
  def parseGoProInfo(self, soup):
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
    return data_json