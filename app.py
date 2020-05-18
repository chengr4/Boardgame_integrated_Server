from flask import Flask

app = Flask(__name__) # __name__ = 目前執行模組




@app.route("/") # 以下面函式為基礎，提供附加功能
def home():
  return "Crawler Server" 


if __name__ == "__main__": #if以主程式執行
  
  app.run() #立刻啟動伺服器



