# -*- coding: utf-8 -*-

from flask import Flask
from flask import redirect


app = Flask(__name__)

@app.route('/jump',methods=['GET','POST'])
def Redirect():
    lUrl = "https://www.bing.com/search?q=%s"%GetLastday(0)
    return  redirect(lUrl)

	
	
@app.route('/',methods=['GET','POST'])
def Index():
	lStr = u"hello world"
	return lStr
	

def GetLastday(tDays= 1):
    import datetime
    today = datetime.date.today()
    oneday = datetime.timedelta(days=tDays)
    iLastday = today - oneday
    return  iLastday.strftime("%Y-%m-%d")

	
	

if __name__ == '__main__':
    app.run(host="127.0.0.1",debug=True,port=8080)
