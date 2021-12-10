import requests
from bs4 import BeautifulSoup
import re
import time
import random
import datetime

# if not os.path.exists('./backpacker'):
#     os.mkdir('./backpacker')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# Collecting URL from each page.
def get_url(location, type):
    main = f'https://www.backpackers.com.tw/forum/forumdisplay.php?f={location}&prefixid={type}&order=desc&page=1'

    res = requests.get(main, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')  # Get webpage HTML
    total_pages = soup.select('td[class="vbmenu_control"]')[0].text.split('，')[1]
    total_pages = int(re.findall('\d+', total_pages)[0])
    print('總頁數= '+ str(total_pages))
    run_page = 10
    for page in range(10, 14):
        url = f'https://www.backpackers.com.tw/forum/forumdisplay.php?f={location}&prefixid={type}&order=desc&page={page}'
        web_crawler(url)
        run_page +=1
        print(f'Lets start page: {run_page}')

        time.sleep(random.randint(1,10))


# Get details from each article.
def web_crawler(url):
    import pymongo
    client = pymongo.MongoClient(
        "mongodb://tfb1031:qwe123456@10.2.16.174/raw_data_for_project")
    db = client.raw_data_for_project
    collection = db.backpackers_hotel

    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # All article lists on each page.
    titles = soup.select('a[class="threadtitle"]')

    backpacker_datas = []
    count_article = 0
    for titlesoup in titles:
        time.sleep(random.randint(1,5))
        # 作者、作者ID、發文日期、發文內容(文字)、發文照片url、文章連結以key / value方式存在dict中
        info = {}
        title = titlesoup.text
        articleID = titlesoup['href'].split('&')[-1]
        #進入文章內開始爬取需要的資訊
        articleUrl = 'https://www.backpackers.com.tw/forum/showthread.php?'+articleID #從文章標題進入討論區
        res = requests.get(articleUrl, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        article = soup.select('div[class="tborder alt1"]')[0]

        try:
            post = article.select('div[class="smallfont"] span')
            author = article.select('a[class="bigusername"]')
            authorID = re.findall('u=\d*', str(author[0]))[0].split('=')[1]
            contents = article.select('div[class="vb_postbit"]')
            mainArticle = str(contents[0])  # 文章內容
            mainArticle = re.findall('[\u4e00-\u9fa5]+\d*[\u4e00-\u9fa5]+', mainArticle)
            imgUrl = re.findall('https://sa1?.*[\d+|\.jpg?]', str(contents[0])) #文章內的照片

            info['author'] = post[0].text
            info['author_ID'] = authorID
            info['post'] = title
            info['article_url'] = articleUrl
            info['time'] = post[2].text
            info['article'] = mainArticle
        except IndexError:
            print(title)
            time.sleep(10)

        #不是每篇文章都有提供照片
        if len(imgUrl) != 0:
            info['imgURL'] = imgUrl
        else:
            info['imgURL'] = '無'

        # 回復貼文
        articleAll = soup.select('div[id="posts"]')[0]
        post = articleAll.select('div[class="smallfont"] span')[3:]
        contents = articleAll.select('div[class="vb_postbit"]')
        reply = str(contents[1:])  # 內文
        reply = re.findall('[\u4e00-\u9fa5]+\d*[\u4e00-\u9fa5]+', reply)  # results are list type

        if len(reply) != 0:
            info['reply'] = reply
        else:
            info['reply'] = '無'

        # print(info)
        backpacker_datas.append(info)
        count_article += 1
        while count_article == 50:
            collection.insert_many(backpacker_datas)
            count_article = 0
            backpacker_datas = []


    collection.insert_many(backpacker_datas)
    # count = collection.count_documents({})
    # print(f'total insert: {count}')


if __name__ == "__main__":
    '''
    Location= {北部: 60, 宜蘭: 257}
    type = {住宿: hotel, 遊記: voyage}
    '''
    start_time = datetime.datetime.now()
    get_url('257','hotel')
    end_time = datetime.datetime.now()
    print("spend: ", (end_time - start_time))
    print(datetime.datetime.now())