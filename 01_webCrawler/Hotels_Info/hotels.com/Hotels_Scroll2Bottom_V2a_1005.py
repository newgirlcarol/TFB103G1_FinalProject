import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import random
url ='https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2021-10-06&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
url2 ='https://tw.hotels.com/search.do?destination-id=1728696&q-check-in=2021-10-06&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'


def ScrolltoGetWholeList(Url,PageCnt):
    FFbrowser = webdriver.Firefox(executable_path=r'D:\\SW_Dev\\MainProject\\Crawlers\\Driver\\geckodriver.exe')
    FFbrowser.get(Url)
    count = 0
    while(count !=PageCnt):        
        print("\n Currently  you  are in  page  = \n",count)
        FFbrowser.execute_script("window.scrollTo(0,document.body.scrollWidth)")
        idle= random.randint(2,5)
        time.sleep(idle)        
        
        FFbrowser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        idle= random.randint(3,5)
        time.sleep(idle)

        FFbrowser.execute_script("window.scrollTo(0, document.body.scrollHeight/2)")
        idle= random.randint(2,6)
        time.sleep(idle)

        FFbrowser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        idle= random.randint(3,7)
        time.sleep(idle)
        count += 1

    soup = BeautifulSoup(FFbrowser.page_source, 'html.parser')
    
    print(soup.prettify())

    todaydate_time = datetime.datetime.now()
    date_time = todaydate_time.strftime("%m_%d_%H_%M") 

    with open("D:\\Hotels_"+date_time+'_'+".html", "w", encoding='utf-8') as file:
        file.write(str(soup))
    FFbrowser.close()
    return soup