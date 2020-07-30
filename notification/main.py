from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/Dell/PycharmProjects/project 1/notification/icon.ico",
        timeout = 5
    )

def getData(url):
    r= requests.get(url)
    return r.text 


if __name__ == "__main__":
    while True:

        #notifyMe("Swapnil Sakhre" ,"lets stop this corona virus")
        myHtmlData = getData("https://www.mohfw.gov.in/")
        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())
        myDataStr=""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]

        print(myDataStr.split("\n\n"))
        itemList = (myDataStr.split("\n\n"))

        states = ['Maharashtra','Gujarat']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = "cases of COVID-19"
                nText =  f"STATE {dataList[1]}:\n Indian: {dataList[2]} foreign: {dataList[3]}\n Cured: {dataList[4]}\n Death: {dataList[5]} "
                notifyMe(nTitle,nText)
                time.sleep(2)
        #print(tr.get_text())
        time.sleep(60)        

