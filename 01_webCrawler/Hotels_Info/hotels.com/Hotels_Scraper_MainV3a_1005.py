import pandas as pd
import re, time, requests
from urllib import parse
import json
import random
from bs4 import BeautifulSoup
import pandas as pd
import Hotels_Scraper_PageDetails_V2d_1005
import  Hotels_Scroll2Bottom_V2a_1005


HOTELs_TPE_DATA_Url  = 'https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_NEW_TPE_DATA_Url = 'https://tw.hotels.com/search.do?destination-id=1728696&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_NEW_YiLan_Couty_DATA_Url = 'https://tw.hotels.com/search.do?destination-id=1726364&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_NEW_YiLan_City_DATA_Url ='https://tw.hotels.com/search.do?destination-id=1636981&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_MainPage_Url    = 'https://tw.hotels.com/ho479182/?q-check-in=2021-10-02&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
HOTELs_MainUrl_Head = 'https://tw.hotels.com'
BS = 'BEST_SELLER'
SRHF = 'STAR_RATING_HIGHEST_FIRST'
SRLF = 'STAR_RATING_LOWEST_FIRST'
GR = 'GUEST_RATING'
HOTELs_TAGs_ID_ResultList = '_3f26d2'
HOTELs_Details_Url =[]
soup_landing_page = Hotels_Scroll2Bottom_V2a_1005.ScrolltoGetWholeList(HOTELs_TPE_DATA_Url,450)

#  Get the HOTELs ID List , Type = LIST
HOTELs_List_html = soup_landing_page.find_all('ul' , {'class' :HOTELs_TAGs_ID_ResultList})

# Get the Current Hotels Link
HOTELsName_InList ='_3zH0kn'
print(' Current HOTELs List =  \n',len(HOTELs_List_html[0].contents) )
idx = 0 

HotelResultList = []
# Collect All Hotel url List 
for each_hotel in HOTELs_List_html[0].contents:
    if(each_hotel.has_attr('data-hotel-id')):
        print('------------------------------------- \n', idx)
        print(each_hotel.a.text)
        HotelResultList.append(each_hotel.a['href'])
        print('HOTELs Url = \n',each_hotel.a['href'])

for eachUrl in HotelResultList:    
    print(' \n ---> ', idx,' th   of      \n ',len(HotelResultList), '\n hotel url = ',eachUrl)
    time.sleep(random.randint(2,8))
    # Start  to Scape Hotel List 
    Hotels_Scraper_PageDetails_V2d_1005.MainPageData(eachUrl)
    idx+=1
    



