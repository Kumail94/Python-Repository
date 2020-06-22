from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title , message):
	notification.notify(
		title=title,
		message=message,
		app_icon = "C:\\Users\\DR\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\coro.ico",
		timeout=14
		)
def getData(url):
	return requests.get(url).text

if __name__ == "__main__":
	while True:
		notifyme("COVID 19" , "Let's stop to spread this virus")
		myHtmlData = getData('https://www.worldometers.info/coronavirus/#countries') 
		#print(myHtmlData)
		soup = BeautifulSoup(myHtmlData ,'html.parser')
		myDataStr = ""
		for tr in soup.find_all('tbody')[1].find_all('tr'):
			myDataStr += tr.get_text()
		myDataStr = myDataStr[1:]
		itemlist = myDataStr.split("\n\n")
		print(itemlist)

		#states = ["Chandigarh" , "Telengana" , "Utar Pradesh"]
		# for item in itemlist[0:22]:
		# 	dataList = item.split('\n')
		# 	#if dataList[1] in states:
		# 		#print(dataList)
		# 	nTitle = "COVID 19"
		# 	nText = f"State: {dataList[1]}\nCountry: {dataList[2]} & Foreign: {dataList[3]}\nCured: {dataList[4]}\nDeaths: {dataList[5]}"
		# 	time.sleep(2)
		# 	notifyme(nTitle , nText)
		# time.sleep(30)		




