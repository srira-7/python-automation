#! python3
import bs4, requests
#from numpy import find_common_type
from win10toast import ToastNotifier

#download page
#getPage = requests.get('https://www.tickertape.in/indices/nifty-50-index-.NSEI')
getPage = requests.get('https://www.moneycontrol.com/indian-indices/nifty-50-9.html')
getPage.raise_for_status #stops program if error occurs

#parse text for nifty50 value
tickerTape = bs4.BeautifulSoup(getPage.text, 'html.parser')
#nifty = tickerTape.select_one('.inprice1 span')
nifty = tickerTape.find("span", {"id": "sp_val"})
castedStr = str(nifty)
exactNum = castedStr[18:27]

#windows toast notifications
notification = ToastNotifier()
notification.show_toast("NIFTY 50", exactNum, duration=10)