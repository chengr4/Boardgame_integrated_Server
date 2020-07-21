from Crawlers.GoCrawler import GoCrawler

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

if __name__ == "__main__":
  #resp_GoNews = fetchHTML(main_url['go_news'], encode='big5-hkscs')
  #parseGoNews(resp_GoNews)

  #resp_GoContest = fetchHTML(main_url['go_contest'], encode='big5-hkscs')
  # parseGoContest(resp_GoContest) -> 改直接傳整個網址

  goCrawler = GoCrawler()
  soup = goCrawler.fetchHTML()
  result = goCrawler.parseGoProInfo(soup)
  print(result)
  
  
  

        