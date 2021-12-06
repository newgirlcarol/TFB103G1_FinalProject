import pandas as pd
import re, time, requests
from urllib import parse
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import json
import random
from bs4 import BeautifulSoup
import pandas as pd
import Hotels_Scraper_PageDetails_V2d_1005
import  Hotels_Scroll2Bottom_V2a_1005


# HOTELs_TPE_DATA_Url  = 'https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2021-10-02&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
# HOTELs_TPE_DATA_Url             = 'https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
# HOTELs_TPE_DATA_Url  = 'https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2022-03-06&q-check-out=2022-03-11&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_TPE_DATA_Url  = 'https://tw.hotels.com/search.do?destination-id=1366745&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_NEW_TPE_DATA_Url = 'https://tw.hotels.com/search.do?destination-id=1728696&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
# HOTELs_NEW_TPE_DATA_Url = 'https://tw.hotels.com/search.do?destination-id=1728696&q-check-in=2022-03-06&q-check-out=2022-03-11&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'

HOTELs_NEW_YiLan_Couty_DATA_Url = 'https://tw.hotels.com/search.do?destination-id=1726364&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_NEW_YiLan_City_DATA_Url ='https://tw.hotels.com/search.do?destination-id=1636981&q-check-in=2021-12-12&q-check-out=2021-12-17&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&sort-order=BEST_SELLER'
HOTELs_MainPage_Url    = 'https://tw.hotels.com/ho479182/?q-check-in=2021-10-02&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
                #   ,'Cookie' : '_abck=C9C27062C41BC93B4EF5B32CF4E9A56A~0~YAAQRDArF5KbVyJ8AQAAe3ZgJQagTPaOZqKXW2fWTo6EvWz+iKdULOSxN/7zzlX1KdsxnMCcFS6at7rkR0dpJAT4NI+fUlJWARZ+bkmHLfhU9umGnRmlZOeC8XzB1ttZxFKRHOFBjGgYZ2IRbQC763k7i2d2owuD91P5gvwsxIb0coAqHMXfZYeQlTHpzRhLxj3jVL7OkxXMsnc9URTUqgl966kPXJl3GWGdg5NWbIAZxLTsdyECpMe5HtvHIaotHL7IAvC/5m0S1f6jqY8lPhQAWdmBAY19PZXbVRMbNh9EnJFy/xPDWT84/irUnvfCoxVIab/hJxQFZS6fXaMiIZS0qToIUbMUuQvCzjdfSCYkFbgVe6wFLdQBWcwkbI09MpnBvBLOBG7i30sY77uo2+4DVimtgCdJIg==~-1~-1~-1; bm_sz=8C6289387D9A037B92D458BD2BD73499~YAAQPBQgF0sfqw98AQAAW9dRJQ34A/lmTJZrXCnC/wnxKQ+yahk8yjrBLOMiF/aG6BAXr+70WsQJENuFPAmqvy5lJj3y0SbPM91JaKzMP+bzBED3X3cUtqNUaeQBuFqUkdXFjPZhwo+XlpHXkZ+O52CqUCAPGYL5GpEz+fBmrV/LAvaCNB/5RGhTAPq8n7jWcj6cqiTW1yPcmtXexLoodwAKCz4HDzHzIsMyJYHBsb1gUoIZiJO9XDRnkA56zlamhOV/JPxBGtId6XNWcycpXfRbPYBi5Iw5nrWlZvkDLMXRBvw=~4273203~3425349; asc=1; visitId=39bf0d6f-5d27-41c9-b997-205d7b264b1b; SESSID=v3Wf8L2AUelYawXwJiiM8GXaZ9.hpa-784555f78d-8gqn5; user=QSp6aF9UV3xIQ09NX1RX; guid=dd147de2-f697-4356-b082-360a5a350cf2; MC1=GUID=7f900f38ac94480f8092a9f10f53b99c; DUAID=7f900f38-ac94-480f-8092-a9f10f53b99c; mvthistory=eJwtjDkOwzAMBH9EiPfRpkkTuAmQ0rX%2F4MdHFtUNh7ubAQYDLsaSVPCHozBIJ40JjkCP9MIUW5JGZEsu4uBmLFLLDmjupLEAru88vC1cVEzuKyGIukGlh2Sy8ZY%2Bus8lJLvCA3vHS5SpA7OVsVr3%2B3V8zu%2FvD7ZZLqA%3D; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=-1330315163%7CMCIDTS%7C18898%7CMCMID%7C08914753079315382361366251052946567019%7CMCAID%7CNONE%7CMCOPTOUT-1632720909s%7CNONE; Session_Pageviews=2; _gcl_au=1.1.1402945074.1632713709; s_ecid=MCMID%7C08914753079315382361366251052946567019; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; s_cc=true; homepage_search_data=5paw5YyX5biCLCDlj7DngaM.%2F%2F2021-10-01%2F%2F2021-10-14%2F%2F2%2F%2Fyyyy-MM-dd%2F%2F1728696%2F%2F; dr=AAA~1632714645~828FA04A2F8F4A45B855D40B5BBEBA8C59CBA5B9BC7A45823F605A30E8B61F85; akacd_pr_20=1637898651~rv=54~id=ac5b822fa1552374dbaa5bba27456b62; xdid=b85776f5-7317-4208-951d-715dcf54b652|1632713708|zh.hotels.com; xdidp=b85776f5-7317-4208-951d-715dcf54b652|1632713708|zh.hotels.com; _uetsid=e8d9aff01f4311ec8a33e1b5b728869e; _uetvid=e8d9d4c01f4311ec9126336562b7e4be; aws=1; AFFLB=A'
                }
HOTELs_MainUrl_Head = 'https://tw.hotels.com'
BS = 'BEST_SELLER'
SRHF = 'STAR_RATING_HIGHEST_FIRST'
SRLF = 'STAR_RATING_LOWEST_FIRST'
GR = 'GUEST_RATING'
HOTELs_TAGs_ID_ResultList = '_3f26d2'
'''
# Start Get Web data 
ss = requests.session()
# res_landing_page = ss.get(HOTELs_TPE_DATA_Url, headers=headers)
res_landing_page = ss.get(HOTELs_NEW_TPE_DATA_Url, headers=headers)
soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')
'''
HOTELs_Details_Url =[]
soup_landing_page = Hotels_Scroll2Bottom_V2a_1005.ScrolltoGetWholeList(HOTELs_TPE_DATA_Url,450)
# soup_landing_page = Hotels_Scroll2Bottom_V2a_1005.ScrolltoGetWholeList(HOTELs_NEW_TPE_DATA_Url,3)
#  It looks like that we coun't get hotel data from a pre-saving html
# with open('D:\\Hotels.com  - NewTaipei City-1-1007.html','r',encoding='utf-8') as fp:
#     soup_landing_page = BeautifulSoup(fp)

#  Get the HOTELs ID List , Type = LIST
HOTELs_List_html = soup_landing_page.find_all('ul' , {'class' :HOTELs_TAGs_ID_ResultList})

# Get the Current Hotels Link
HOTELsName_InList ='_3zH0kn'
# HotelsList = soup.findAll('a',{'class':'js-job-link'})
print(' Current HOTELs List =  \n',len(HOTELs_List_html[0].contents) )
idx = 0 

HotelResultList = []
# Collect All Hotel url List 
# for each_hotel in HOTELs_List_html[0].contents:
for each_hotel in HOTELs_List_html[0].contents:
    if(each_hotel.has_attr('data-hotel-id')):
        # HOTELs_Details_Url.append(HOTELs_MainUrl_Head + each_hotel.a['href'])
        print('------------------------------------- \n', idx)
        print(each_hotel.a.text)
        HotelResultList.append(each_hotel.a['href'])
        print('HOTELs Url = \n',each_hotel.a['href'])
        
        # HOTELs_Details_Url = HOTELs_MainUrl_Head + each_hotel.a['href']

for eachUrl in HotelResultList:
    
    print(' \n ---> ', idx,' th   of      \n ',len(HotelResultList), '\n hotel url = ',eachUrl)
    time.sleep(random.randint(2,8))
    # Start  to Scape Hotel List 
    Hotels_Scraper_PageDetails_V2d_1005.MainPageData(eachUrl)
    idx+=1
    



