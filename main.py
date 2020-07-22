from crawlers.go_crawler import GoCrawler
from crawlers.chinese_chess_crawler import ChineseChessCrawler
from crawlers.chess_crawler import ChessCrawler
import json

# call by server
def run_result():
  # crawl Go
  goCrawler = GoCrawler()
  resultGo = goCrawler.parseGoProInfo()

  # crawl Chinese chess
  chineseChessCrawler = ChineseChessCrawler()
  resultCC = chineseChessCrawler.parseChineseChessNews()

  # crawl Chess
  chessCrawler = ChessCrawler()
  resultChess = chessCrawler.parseChessNews()
  
  data = {}
  data.update(resultGo)
  data.update(resultCC)
  data.update(resultChess)

  # convert to json format
  data_json = json.dumps(data, ensure_ascii=False)

  return data_json


if __name__ == "__main__":
  #resp_GoNews = fetchHTML(main_url['go_news'], encode='big5-hkscs')
  #parseGoNews(resp_GoNews)

  #resp_GoContest = fetchHTML(main_url['go_contest'], encode='big5-hkscs')
  # parseGoContest(resp_GoContest) -> 改直接傳整個網址

  # crawl Go
  goCrawler = GoCrawler()
  resultGo = goCrawler.parseGoProInfo()

  # crawl Chinese chess
  chineseChessCrawler = ChineseChessCrawler()
  resultCC = chineseChessCrawler.parseChineseChessNews()

  # crawl Chess
  chessCrawler = ChessCrawler()
  resultChess = chessCrawler.parseChessNews()
  
  data = {}
  data.update(resultGo)
  data.update(resultCC)
  data.update(resultChess)

  # convert to json format
  data_json = json.dumps(data, ensure_ascii=False)
  print(data)

        