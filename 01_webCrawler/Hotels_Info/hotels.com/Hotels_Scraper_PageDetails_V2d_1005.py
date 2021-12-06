import json
from bs4 import BeautifulSoup
import pandas as pd
import  requests
import time
import datetime
import json
import random

HOTELs_MainPage_Url    ='https://tw.hotels.com/ho545286/?q-check-in=2021-10-08&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&f-hotel-id=479182&sort-order=BEST_SELLER&WOD=6&WOE=6&MGT=7&ZSX=0&SYE=3&YGF=2'
HOTELs_Tail_Url =              '/ho545286/?q-check-in=2021-10-08&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&q-room-0-children=0&f-hotel-id=479182&sort-order=BEST_SELLER&WOD=6&WOE=6&MGT=7&ZSX=0&SYE=3&YGF=2'
HOTELs_Details_Main_Url ='https://tw.hotels.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
                #   ,'Cookie' : '_abck=C9C27062C41BC93B4EF5B32CF4E9A56A~0~YAAQRDArF5KbVyJ8AQAAe3ZgJQagTPaOZqKXW2fWTo6EvWz+iKdULOSxN/7zzlX1KdsxnMCcFS6at7rkR0dpJAT4NI+fUlJWARZ+bkmHLfhU9umGnRmlZOeC8XzB1ttZxFKRHOFBjGgYZ2IRbQC763k7i2d2owuD91P5gvwsxIb0coAqHMXfZYeQlTHpzRhLxj3jVL7OkxXMsnc9URTUqgl966kPXJl3GWGdg5NWbIAZxLTsdyECpMe5HtvHIaotHL7IAvC/5m0S1f6jqY8lPhQAWdmBAY19PZXbVRMbNh9EnJFy/xPDWT84/irUnvfCoxVIab/hJxQFZS6fXaMiIZS0qToIUbMUuQvCzjdfSCYkFbgVe6wFLdQBWcwkbI09MpnBvBLOBG7i30sY77uo2+4DVimtgCdJIg==~-1~-1~-1; bm_sz=8C6289387D9A037B92D458BD2BD73499~YAAQPBQgF0sfqw98AQAAW9dRJQ34A/lmTJZrXCnC/wnxKQ+yahk8yjrBLOMiF/aG6BAXr+70WsQJENuFPAmqvy5lJj3y0SbPM91JaKzMP+bzBED3X3cUtqNUaeQBuFqUkdXFjPZhwo+XlpHXkZ+O52CqUCAPGYL5GpEz+fBmrV/LAvaCNB/5RGhTAPq8n7jWcj6cqiTW1yPcmtXexLoodwAKCz4HDzHzIsMyJYHBsb1gUoIZiJO9XDRnkA56zlamhOV/JPxBGtId6XNWcycpXfRbPYBi5Iw5nrWlZvkDLMXRBvw=~4273203~3425349; asc=1; visitId=39bf0d6f-5d27-41c9-b997-205d7b264b1b; SESSID=v3Wf8L2AUelYawXwJiiM8GXaZ9.hpa-784555f78d-8gqn5; user=QSp6aF9UV3xIQ09NX1RX; guid=dd147de2-f697-4356-b082-360a5a350cf2; MC1=GUID=7f900f38ac94480f8092a9f10f53b99c; DUAID=7f900f38-ac94-480f-8092-a9f10f53b99c; mvthistory=eJwtjDkOwzAMBH9EiPfRpkkTuAmQ0rX%2F4MdHFtUNh7ubAQYDLsaSVPCHozBIJ40JjkCP9MIUW5JGZEsu4uBmLFLLDmjupLEAru88vC1cVEzuKyGIukGlh2Sy8ZY%2Bus8lJLvCA3vHS5SpA7OVsVr3%2B3V8zu%2FvD7ZZLqA%3D; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=-1330315163%7CMCIDTS%7C18898%7CMCMID%7C08914753079315382361366251052946567019%7CMCAID%7CNONE%7CMCOPTOUT-1632720909s%7CNONE; Session_Pageviews=2; _gcl_au=1.1.1402945074.1632713709; s_ecid=MCMID%7C08914753079315382361366251052946567019; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; s_cc=true; homepage_search_data=5paw5YyX5biCLCDlj7DngaM.%2F%2F2021-10-01%2F%2F2021-10-14%2F%2F2%2F%2Fyyyy-MM-dd%2F%2F1728696%2F%2F; dr=AAA~1632714645~828FA04A2F8F4A45B855D40B5BBEBA8C59CBA5B9BC7A45823F605A30E8B61F85; akacd_pr_20=1637898651~rv=54~id=ac5b822fa1552374dbaa5bba27456b62; xdid=b85776f5-7317-4208-951d-715dcf54b652|1632713708|zh.hotels.com; xdidp=b85776f5-7317-4208-951d-715dcf54b652|1632713708|zh.hotels.com; _uetsid=e8d9aff01f4311ec8a33e1b5b728869e; _uetvid=e8d9d4c01f4311ec9126336562b7e4be; aws=1; AFFLB=A'
                }
HOTELs_MainUrl_Head = 'https://tw.hotels.com'
# SubFunction
def MainPageData(hotel_url):

# region Key String /Header Declarison  
    BS = 'BEST_SELLER'
    SRHF = 'STAR_RATING_HIGHEST_FIRST'
    SRLF = 'STAR_RATING_LOWEST_FIRST'
    GR = 'GUEST_RATING'

    HOTEL_DETAILs_DATA = []
    HOTEL_DETAILs_DATA ={}
    #Hotels  Title/Tag String

    HOTELs_KEY_STRs_Review_WebLink  = 'hotel-review-link'
    HOTELs_KEY_STRs_FacilityList_1  = 'main-facilitiy'
    HOTELs_KEY_STRs_FacilityList_2  = 'family-tour'
    HOTELs_KEY_STRs_FacilityList_3  = 'nearby-sopt'
    HOTELs_KEY_STRs_RankingScores ='ranking-scores'
    HOTELs_KEY_STRs_ReviewQty = 'review-counts '
    HOTELs_KEY_STRs_KeyFacility  = ' key-facility'
    HOTELs_KEY_STRs_Infursture = 'Infurstrcture'
    HOTELs_KEY_STRs_Price= 'room-price'
    HOTELs_KEY_STRs_Name ='hotel-name' 
    HOTELs_KEY_STRs_ID = 'hotel-id'
    HOTELs_KEY_STRs_URL = 'hotel-url'
    
    HOTELs_KEY_STRs_Address = 'hotel-address'
    HOTELs_KEY_STRs_StarRank='hotel-star-rank'
    HOTELs_KEY_STRs_FeatureInfs='hotel-feature'
    HOTELs_KEY_STRs_LandMark='hotel-landmark'
    HOTELs_KEY_STRs_Airport='hotel-airport'
    HOTELs_KEY_STRs_Train='hotel-train'
    HOTELs_KEY_STRs_Shuttle='hotel-shuttle'
    HOTELs_KEY_STRs_MapUrl = 'hotel-map-url'
    HOTELs_KEY_STRs_ImgUrl = 'hotel-img-url'
    HOTELs_KEY_STRs_Review = 'hotel-review'
    HOTELs_KEY_STRs_ReviewRank = 'hotel-review-rank'
    HOTELs_KEY_STRs_ReviewContent ='hotel-review-content'
    HOTELs_KEY_STRs_Err = 'hotel-data-err'

    HOTELs_VAL_STRs_Name ='' 
    HOTELs_VAL_STRs_ID = ''
    #
    # Web  TAG  Data
    HOTELs_TAGs_Name =  '_2h6Jhd'
    HOTELs_TAGs_Stars   = '_2dOcxA'
    HOTELs_TAGs_Price = '_3XSqn6'   

    #  Address  TAG
    HOTELs_TAGs_Address = '_2lmU8j'
    HOTELs_TAGs_Address2 = 'aqrHQz'

    HOTELs_TAGs_KeyFacility = '_3pPyAT'  
    HOTELs_TAGs_FacilityList = '_2cVsY2'  

    HOTELs_TAGs_ServiceList = '_2cVsY2'
    HOTELs_TAGs_Lardmark = '_1MPDgr'
    HOTELs_TAGs_AirPort = 'airport'
    HOTELs_TAGs_Train ='train-station'
    HOTELs_TAGs_Shuttle ='shuttle'
    HOTELs_TAGs_Map = '_3tLX98'
    HOTELs_TAGs_Img = '_3hkrim'

    HOTELs_TAGs_Review1='_3eVx_d'
    HOTELs_TAGs_Review1_RankPoint = '_1biq31 _11XjrQ _1Zann2'
    HOTELs_TAGs_Review2 = 'uwecAH'

    HOTELs_TAGs_MainScores1='_1biq31 _11XjrQ _2cKo4b'
    HOTELs_TAGs_MainScores2='_1biq31 _2APCnh _2cKo4b'
    HOTELs_TAGs_Review_Counts = '_3zLN_v Y_8VbY b3TRQ'
    HOTELs_TAGs_Review_Content_Block=  '_7JZ1Di'
    HOTELs_TAGs_Review_Counts= 'k3LKyj'

    HOTELsFileTailName ='DataDict'
    HOTELs_TAGs_Review_List = 'brand-reviews-listing'
    HOTELs_TAGs_Review_Card =  'review-card'
    HOTELs_TAGs_RatingScore  = 'rating-score'
    HOTELs_TAGs_RatingBadge =  'rating-badge '
    HOTELs_TAGs_Date = 'date'
    HOTELs_TAGs_ReviewContent =  'expandable-content description'
#endregion 
    # Get the Hotels UNI ID
    Segments = hotel_url.rpartition('/')
    for item in Segments:
            if 'ho' in item:
                    if '/' in item:
                        print('\n',type(item))
                        print('\n',type(HOTELs_VAL_STRs_ID))
                        HOTELs_VAL_STRs_ID = item.replace('/','')                       
                        print('\n',type(HOTELs_VAL_STRs_ID))

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_ID:HOTELs_VAL_STRs_ID})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_ID] = HOTELs_VAL_STRs_ID
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_URL] = HOTELs_MainUrl_Head+hotel_url
    # Program Start
    print()
    time.sleep(random.randint(2,8))
    # Init Session
    ss = requests.session()
  
    try:
        # Get the Hotels HTML data
        res_landing_page = ss.get(HOTELs_MainUrl_Head+hotel_url, headers=headers)
        soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Err] = 'requests.exceptions.ConnectionError.  Max retries exceeded '
        todaydate_time = datetime.datetime.now()
        date_time = todaydate_time.strftime("%m_%d_%H_%M") 
        # Write Hotel Details dictionary  to file
        with open('d:\\'+HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_ID]+'_'+HOTELsFileTailName+'_'+date_time+'.json', 'w', encoding="utf-8") as file_handler:
            json.dump(HOTEL_DETAILs_DATA, file_handler, ensure_ascii=False )    
        return



    ''' 
    '''
    # Get Hotel Name
    HOTELs_Details_Url =[]
    # Get the HOTELs ID List , Type = LIST
    # Get the HotelsName  & Star Level
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Name})
    if(HOTELs_List_html != None):
            print('HOTEL Name=', HOTELs_List_html.find('h1').text 
                                            ,'\n Stars = \n '
                                            ,HOTELs_List_html.find('span').text)
            # Collect HOTELs Data
            # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Name:HOTELs_List_html.find('h1').text})
            HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Name] = HOTELs_List_html.find('h1').text

                                            # .find('span',{'class':HOTELs_TAGs_Stars }).text)
    else:
            print('No Info Available! \n')


    # Get Hotels Star
    HOTELs_List_html = soup_landing_page.find('span' , {'class' :HOTELs_TAGs_Stars})        
    if(HOTELs_List_html != None):
            # Collect HOTELs Data
            # HOTEL_DETAILs_DATA.append({OTELs_KEY_STRs_StarRank: HOTELs_List_html.text})        
            HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_StarRank] =  HOTELs_List_html.text
            print('HOTEL Stars', HOTELs_List_html.text)
    else:
            print('No Info Available! \n')


    # Get Hotel Prices
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Price})
    if(HOTELs_List_html != None):
            print('HOTEL Price\n', HOTELs_List_html.text)
            # Collect HOTELs  Data 
            # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Price:HOTELs_List_html.text})
            HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Price] = HOTELs_List_html.text
    else:
            print('No Info Available! \n')

    
    # Get HOTELs_TAGs_Address
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Address})
    if(HOTELs_List_html != None):
            print('HOTELs_TAGs_Address\n', HOTELs_List_html.text)
    else:
            print('No Info Available! \n')

    # Get  HOTELs_TAGs_Address2
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Address2})
    if(HOTELs_List_html != None):
            print('HOTELs_TAGs_Address2 \n', HOTELs_List_html.text)
    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Address:})
    if(HOTELs_List_html != None):
            if(HOTELs_List_html.text != None):
                if(HOTELs_List_html.text != ''):
                        HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Address] =HOTELs_List_html.text.replace('\ue98d','')
    else:   
        print('Not Hotel Address found!')  

    loop =[]
    # Get HOTELs_TAGs_KeyFacility
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_KeyFacility})
    if(HOTELs_List_html != None ):
        if( len(HOTELs_List_html.contents) >=1 ):
            for item in HOTELs_List_html.contents[0]: 
                    print('HOTELs_TAGs_KeyFacility\n', item.text)
                    loop.append(item.text)
    else:
            print('No Info Available! \n')
    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_KeyFacility:loop})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_KeyFacility] = loop

    loop1=[]
    loop2 =[]
    loop3=[]
    # Get Hotels  HOTELs_TAGs_FacilityList
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_FacilityList})
    if(HOTELs_List_html != None):          
            FacTitle = HOTELs_List_html.find_all('h3')
            HeadLimit  =  len(HOTELs_List_html.find_all('h3'))
            HeadCnt = 0
            for ultag in HOTELs_List_html.find_all('ul', {'class': 'FWXvlZ _2WrGNz'}):
                    if(HeadCnt <=  HeadLimit ):
                            print('Type= \n' , str.strip(FacTitle[HeadCnt].text) )
                    for litag in ultag.find_all('li'):
                            print('\n', litag.text)
                            if(HeadCnt ==0):
                                    loop1.append(litag.text)
                            if(HeadCnt ==1):       
                                    loop2.append(litag.text)
                    HeadCnt = HeadCnt+1        

            for ultag in HOTELs_List_html.find_all('ul', {'class': '_2sHYiJ'}):
                    if(HeadCnt <=  HeadLimit ):
                            print('Type= \n' , str.strip(FacTitle[HeadCnt].text) )
                    for litag in ultag.find_all('li'):
                            loop3.append(litag.text)
                            print('\n', litag.text)
                    HeadCnt = HeadCnt+1                

    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_FeatureInfs:[loop1,loop2,loop3]})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_FeatureInfs] =[loop1,loop2,loop3]

    # ReSet
    loop1 =[]
    loop2 =[]
    loop3 =[]
    loop4=[]
    # Get Hotels HOTELs_TAGs_Lardmark 
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Lardmark})
    if(HOTELs_List_html != None):
            HeadCnt =0 
            FacTitle = HOTELs_List_html.find_all('h3')
            HeadLimit  =  len(HOTELs_List_html.find_all('h3'))

            for ultag in HOTELs_List_html.find_all('ul'):
                    if(HeadCnt < HeadLimit ):
                            print('Type= \n' , str.strip(FacTitle[HeadCnt].text) )
                    for litag in ultag.find_all('li'):
                            if HeadCnt == 0:
                                    loop1.append(litag.text)
                            if HeadCnt == 1:
                                    loop2.append(litag.text)

                            print('\n', litag.text)
                    HeadCnt = HeadCnt+1        
            HeadCnt = 0
            for ultag in HOTELs_List_html.find_all('ul', {'class': HOTELs_TAGs_Shuttle}):
                    if(HeadCnt <=  HeadLimit ):
                            print('Type= \n' , str.strip(FacTitle[HeadCnt].text) )
                    for litag in ultag.find_all('li'):
                            if HeadCnt == 0:
                                    loop3.append(litag.text)
                            if HeadCnt == 1:
                                    loop4.append(litag.text)
                            print('\n', litag.text)
                    HeadCnt = HeadCnt+1                

    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_LandMark:[loop1,loop2,loop3,loop4]})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_LandMark]=[loop1,loop2,loop3,loop4]

    loop1 =[]
    # Get Hotels HOTELs_TAGs_AirPort 
    HOTELs_List_html = soup_landing_page.find('ul' , {'class' :HOTELs_TAGs_AirPort})
    if(HOTELs_List_html != None): 
            for item in HOTELs_List_html.contents: 
                    loop1.append(item.text)
                    print('HOTELs_TAGs_AirPort\n', item.text)
    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Airport:loop1})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Airport]=loop1
    loop2= []
    # Get  HOTELs_TAGs_Train 
    HOTELs_List_html = soup_landing_page.find('ul' , {'class' :HOTELs_TAGs_Train})
    if(HOTELs_List_html != None):
            for item in HOTELs_List_html.contents: 
                    loop2.append(item.text)
                    print('HOTELs_TAGs_Train\n', item.text)
    else:
            print('No Info Available! \n')
    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Train:loop2})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Train]=loop2

    loop3 =[]
    # Get  HOTELs_TAGs_Shuttle 
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Shuttle})
    if(HOTELs_List_html != None):
            for item in HOTELs_List_html.contents: 
                    loop3.append(item.text)
                    print('HOTELs_TAGs_Lardmark\n', item.text)
    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_Shuttle:loop3})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Shuttle]= loop3

    # 
    # Get  HOTELs_TAGs_Map 
    loop1 = []
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Map})
    if(HOTELs_List_html != None):
            images = HOTELs_List_html.findAll('img')
            for image in images:
                    if (image.has_attr('src')):
                            print('\n Map Data= ', image['src'])
                            loop1.append(image['src'])
                    elif(image.has_attr('data-src')):
                                    print('\n  Map Data= ', image['data-src'])        
                                    loop1.append(image['data-src'])
    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_MapUrl:loop1})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_MapUrl] = loop1

    loop2  =[]
    # Get  HOTELs_TAGs_Img --->GetImage
    HOTELs_List_html = soup_landing_page.find('button' , {'class' :HOTELs_TAGs_Img})
    if(HOTELs_List_html != None):
            images = HOTELs_List_html.findAll('img')
            for image in images:
                    if (image.has_attr('src')):
                            print('\n HOTELs_TAGs_Img Data= ', image['src'])
                            loop2.append( image['src'])
                    elif(image.has_attr('data-src')):
                                    print('\n  HOTELs_TAGs_Img Data= ', image['data-src'])        
                                    loop2.append( image['data-src'])

    else:
            print('No Info Available! \n')

    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_ImgUrl:loop2})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_ImgUrl] =loop2

    loop3 =[]
    # Get  HOTELs_TAGs_Review1 Star & Count
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Review_Content_Block})
    if(HOTELs_List_html != None):        
            # print('\nTheHotels Scores = ', HOTELs_List_html.contents[0].text)
            # print('\nTheHotels Review Count = ',HOTELs_List_html.contents[1].text)
            HotelsStar = HOTELs_List_html.find('span',{'class':HOTELs_TAGs_MainScores1})        
            if(HotelsStar == None): 
                HotelsStar = HOTELs_List_html.find('span',{'class':HOTELs_TAGs_MainScores2})

            if(HotelsStar!=None):    
                print('\n Star= ', HotelsStar.text)
                loop3.append( HotelsStar.text)

            HotelsReviewCount = HOTELs_List_html.find('span',{'class':HOTELs_TAGs_Review_Counts})        
            print('\n ReviewCount= ', HotelsReviewCount.text)
            loop3.append( HotelsReviewCount.text)
    else:
            print('No Info Available! \n')
    # Collect HOTELs Data
    # HOTEL_DETAILs_DATA.append({HOTELs_KEY_STRs_ReviewRank:loop3})
    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_ReviewRank]= loop3

    ### Here start to get  review link  ================================

    HotelReviewMainPageUrl =''
    ReviewDataContent = []
    CommentReview = []

    #0
    DicTitle_RanknDate = 'RankAndDate'
    #1 
    DicTitle_Content = 'ReviewContent'
    #3
    DicTitle_NameNLong = 'NameAndDate'
    loop1 =[]
    loop2 =[]
    loop3 =[]
    #  HOTELs_TAGs_Review Web Url
    HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Review_Content_Block})
    if(HOTELs_List_html != None):        
            HotelsReviewLink = HOTELs_List_html.find('a',href = True)           
            if ( HotelsReviewLink != None):
                    print('\n Link = ', HotelsReviewLink['href'] )
                    HotelReviewMainPageUrl = HOTELs_MainUrl_Head +HotelsReviewLink['href']
                    HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Review_WebLink] = HotelReviewMainPageUrl
            else:
                    print('None Found!!')        
    else:
            print('No Info Available! \n')
    # ReviewPageUrl = 'https://tw.hotels.com/ho545286-tr/?q-check-in=2021-10-08&q-check-out=2021-10-16&q-rooms=1&q-room-0-adults=2&applyEmbargo=false&reviewTab=brand-reviews&f-amid=' 

    if(HotelReviewMainPageUrl != None):    
        if(HotelReviewMainPageUrl != ' '):            
            try:   
                res_landing_page = ss.get(HotelReviewMainPageUrl, headers=headers)
                soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')
                HOTELs_List_html = soup_landing_page.find('div' , {'class' :HOTELs_TAGs_Review_List})
                if(HOTELs_List_html != None):
                        # limit = HOTELs_List_html.contents.count()
                        review_limit = len(HOTELs_List_html)
                        print('\n Type =', type(HOTELs_List_html))
                        review_limit = len(HOTELs_List_html.contents)
                        print('\n limit = ', review_limit)
                        for review in HOTELs_List_html.find_all('div' , {'class' :HOTELs_TAGs_Review_Card}):                
                                print('All- review item : \n',review)   
                                print('\n Data Length= ',len(review))
                                cnt = 0   
                                for i in review:
                                        print('\n type = ', type(i))
                                        print('\n # cnt ', cnt ,' \nText= ',i.text )        
                                        if(cnt == 0 ):
                                                loop1.append(i.text)
                                                CommentReview.append({DicTitle_RanknDate:i.text})
                                        if(cnt ==1 ):
                                                loop1.append(i.text)
                                                CommentReview.append({DicTitle_Content:i.text})
                                        if(cnt ==2 ):        
                                                loop1.append(i.text)
                                                CommentReview.append({DicTitle_NameNLong:i.text})
                                        cnt = cnt+1
                                
                                loop2.append(loop1)       
                                loop1=[]
                else:           
                        print('No Info Available! \n')
            except:
                print(' Review Page  Details! NotFound !')                                
        else:
               print('No Info Available! \n')

        # Collect HOTELs Data
        HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_Review] =loop2
    
    else:
        print('No Info Available! \n')
    todaydate_time = datetime.datetime.now()
    date_time = todaydate_time.strftime("%m_%d_%H_%M") 
    # Write Hotel Details dictionary  to file
    with open('d:\\'+HOTEL_DETAILs_DATA[HOTELs_KEY_STRs_ID]+'_'+HOTELsFileTailName+'_'+date_time+'.json', 'w', encoding="utf-8") as file_handler:
        json.dump(HOTEL_DETAILs_DATA, file_handler, ensure_ascii=False )

     # with open('d:\\'+CommentFileName+date_time,'w', encoding='utf-8')  as fout:
                #         # fout.write(CommentReview)
                #         json.dump(CommentReview, fout, ensure_ascii=False )
        
    print()
    print()
