import requests
from bs4 import BeautifulSoup
import re
import pymongo
import time

client = pymongo.MongoClient("mongodb://tfb1031:qwe123456@10.2.16.174/raw_data_for_project?ssl_cert_reqs=CERT_NONE")
db = client.raw_data_for_project
# 賦予 collection 一個變數，才可以呼叫 pymongo method
collection = db.ptt


headers ={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

location = input("Where do you want to go? ")
url = f"https://www.ptt.cc/bbs/Hotel/search?q={location}"
page = requests.get(url, headers = headers).text
doc = BeautifulSoup(page, "html.parser")

# 找出總頁數
total_pages = doc.find(class_ = "btn wide")["href"].split("?")[-1].split("&")[0].split("=")[-1]
total_pages = int(total_pages)
print(f"找尋{location}的遊記，共{total_pages}頁")
ptt_hotel_data = []
countArticle = 0
finish_page = 1
for page in range(1, total_pages + 1):
    url = f"https://www.ptt.cc/bbs/Hotel/search?page={page}&q={location}"
    page = requests.get(url, headers=headers).text
    doc = BeautifulSoup(page, "html.parser")

    lists = doc.find_all(class_ = "title")
    for i in lists :
        title = i.text #每篇文章標題
        link = "https://www.ptt.cc" + i.a["href"] #每篇文章連結

        articleRes = requests.get(link, headers= headers)
        articleSoup = BeautifulSoup(articleRes.text, "html.parser")
        parent = articleSoup.find(id="main-content")
        article = parent.text.split("※ 發信站: ")[0].strip() #文章內容


        #爬取的標題,內容,連結存成dict
        info = {"title" : title, "content" : article, "link" : link}
        ptt_hotel_data.append(info)
        countArticle += 1
        ###
        while countArticle == 50:
            collection.insert_many(ptt_hotel_data)
            countArticle = 0
            ptt_hotel_data = []
    time.sleep(7)

    print("finish Page: " + str(finish_page))
    finish_page += 1