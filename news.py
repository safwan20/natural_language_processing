import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests_html import HTML,HTMLSession
import pandas


#Extracted the news
arr = []
for i in range(20) :
    with requests.Session() as s :
        session = HTMLSession()
        href = "https://www.livemint.com/latest-news/page-" + str(i+1)
        r = session.get(href)
        soup = BeautifulSoup(r.content, 'html.parser')  
    
    listview = soup.find_all('div',{'class':'listing'})
    for i in listview :
        link = "https://www.livemint.com/" +  i.a['href']
        print(link)
        lis = []
        try : 
            with requests.Session() as s :
                session = HTMLSession()
                href1 = link
                r = session.get(href1)
                soup = BeautifulSoup(r.content, 'html.parser')  
            headline  = soup.find_all('h1',{'class' : 'headline'})
            body = soup.find_all('div',{'class':'mainArea'})
            body = body[0].text.replace('Topics','')
            body = body.replace('Share Via','')
            body = body.split('\n\n\n\n\n\n')[0]
            if body :
                lis.append(headline[0].text)
                lis.append(body.replace('\n',''))
                arr.append(lis)
            else :
                continue
        except :
            print("hello")
datas = pandas.DataFrame(arr,columns=["headline","body"])
datas.to_csv("n.csv",index=True)

    