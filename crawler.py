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
def fetch(url, encode):
    response = requests.get(url)
    response.encoding = encode
    #response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    return response

# 被擷取的網站
## 中華民國圍棋協會
url = 'http://www.weiqi.org.tw/class_list.asp'


resp = fetch(url, encode='big5-hkscs')


# html.parser
# Batteries included, Decent speed (不錯的速度), Lenient (寬容)
soup = BeautifulSoup(resp.text, "lxml")

# all topics
topics = soup.select("tr")
print(topics[0].find('a').text)

'''
# fetch needed href from index
for topic in topics:
    a_topic = topic.find("a")
    datetime_object = datetime.strptime(topic.find("div", class_="date").text.strip(), '%m/%d')

    # if the topic is not empty
    if a_topic and topic.find("span"):

        # push must bigger than push_number and catch today
        push = int(topic.find("span").text)
        if push < push_numbers:
            continue
        elif dateime_now.strftime("%m/%d") != datetime_object.strftime("%m/%d"):
            continue

        title = title + a_topic.text +'\n'
        # catch href (也可能不需要了)

        a_topic_href = a_topic.get("href")
        article_href.append("https://www.ptt.cc"+ a_topic_href)'''

        