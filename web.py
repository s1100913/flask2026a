from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	link = "歡迎進入許允蓁的首頁"
	link += "<a href='/mis>"
	link += "<a href='/about>課程</a><br>"
	link += "<a href='/about>今天日期</a><br>"
	link += "<a href='/about>關於允蓁</a><br>"
	return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now   = datetime.now()
    year  = str(now.year)  #取得年份
    month = str(now.month) #取得月份
    day   = str(now.day)   #取得日期
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime = now)

@app.route("/mis")
def about():
    return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)



