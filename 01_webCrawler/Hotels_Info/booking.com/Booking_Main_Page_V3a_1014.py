from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import datetime
import json

''' 

Booking Hotels TAG  Define ====================================================================

'''

BOOKing_TAG_Str_Hotel_List_Data = 'a233d9c18f'
BOOKing_TAG_Str_Hotel_List_Data = 'eafde27db6'
BOOKing_TAG_Str_Hotel_Url_Head= 'https://www.booking.com'
BOOKing_TAG_Str_ReviewScores = 'eb2161f400 e5a32fd86b'
BOOKing_TAG_Str_ReviewCounts = '_79b2b046b0 b33b89e42f _5586935da5 _6a1b6ff88e'

BOOKing_TAG_Str_StarCounts = 'cf18357eee cf1a1ba763 _698592d8e6'

BOOKing_TAG_Str_StarCountsPath = '0 0 24 24'

''' 
Booking Hotels data  Dictionary  Define =============================================================

'''
BOOKing_HOTELs_DETAILs_DATA = {}

BOOKing_HOTELs_KEY_STRs_Hotels_Id = 'hotel-id'
BOOKing_HOTELs_KEY_STRs_Hotels_Name = 'hotel-name'
BOOKing_HOTELs_KEY_STRs_Hotels_Url = 'hotel-url'
BOOKing_HOTELs_KEY_STRs_Hotels_MapUrl = 'hotel-map-url'
BOOKing_HOTELs_KEY_STRs_Hotels_RoomPrice = 'room-price'

BOOKing_HOTELs_KEY_STRs_Hotels_Address = 'hotel-address'
BOOKing_HOTELs_KEY_STRs_Hotels_StarRank = 'hotel-star-rank'
BOOKing_HOTELs_KEY_STRs_Hotels_ReviewScores = 'hotel-review-scores'
BOOKing_HOTELs_KEY_STRs_Hotels_ReviewCounts = 'hotel-review-counts '
BOOKing_HOTELs_KEY_STRs_Hotels_ReviewBlocks = 'hotel-review-blocks '
BOOKing_HOTELs_KEY_STRs_Hotels_KeyFacility  = 'hotel-feature-facility'
BOOKing_HOTELs_KEY_STRs_Hotels_FacilityList  = 'hotel-feature-list'
BOOKing_HOTELs_KEY_STRs_Hotels_ReviewScrollBar  = 'hotel-review-scroll-bar'
BOOKing_HOTELs_KEY_STRs_Hotels_ImgList  = 'hotel-img-list'

BOOKing_HOTELs_KEY_STRs_Hotels_NearBy= 'hotel-nearby'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByNatural= 'hotel-nearby-natural'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByHotSpot= 'hotel-nearby-hot-spot'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByCaffeRestaurant= 'hotel-nearby-caffe-restaurant'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByTrain= 'hotel-nearby-train'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByAirport= 'hotel-nearby-airport'
BOOKing_HOTELs_KEY_STRs_Hotels_NearByWebLink= 'hotel-img-link'



headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}



#  Sub Function start here 
#  Sub function call   ==  Get  details data on Hotels Main Page
#  Get Hotel main page detail data
def ScrapeHotelDetails(HotelDetailUrl):

        ss = requests.session()        
        # check HTML line # 3700 -start for html tag structure  for reference
        # 
        res_landing_page = ss.get(HotelDetailUrl, headers=headers)
        soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')


        # Can not find hotel
        # hotel_map_url =  soup_landing_page.find(id="hotel_header")
        # # # hotel_map_url = soup_landing_page.select('a[href*="#map_opened-hotel_header"]')
        # # hotel_map_url = json.loads(hotel_map_url)
        # print('\n page_data = ' , hotel_map_url )
        
        #0 Get Hotels ID
        UrlResult = urlparse(HotelDetailUrl)
        print('\n',UrlResult.path )
        itemslist = UrlResult.path.split('/')
        for i in itemslist:
                print('\n item = ', i)
                if '.html' in i:
                        hotel_id= i.replace('.html','')
                        if '.zh-tw' in hotel_id:
                                hotel_id = hotel_id.replace('.zh-tw','')
                                break
                if '.htm' in i:
                        hotel_id= i.replace('.htm','')
                        if '.zh-tw' in hotel_id:
                                hotel_id = hotel_id.replace('.zh-tw','')
                                break
        # Collect Hotel ID data
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_Id] = str(hotel_id)
        
        #1 Get Hotels Name         
        hotel_name= soup_landing_page.find(id='hp_hotel_name')
        if  hotel_name == None:
                hotel_name = soup_landing_page.find('div', class_='hp__hotel-title')

        for item in hotel_name:
                print('\n name= ',item, '\nLength=', len(item) )
                if( len(item) >4 ):
                        print('\n hotel name = ', str(item) )
                        # Collect Hotel delail data
                        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_Name] = str(item)
        
        # 1 Get Hotels Url:
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_Url] = HotelDetailUrl

         #3  Get Hotels Stars
        # hotel_star =  soup_landing_page.select(f'span[class="{BOOKing_TAG_Str_StarCounts}"]>svg[viewBox="{BOOKing_TAG_Str_StarCountsPath}"] >path')
        # <div data-testid="quality-rating" class="bce6e31203">
        # hp__hotel_ratings__stars nowrap
        # hotel_star = soup_landing_page.find('div', class_='bd891cfe38' )
        hotel_star = soup_landing_page.find('span', class_='hp__hotel_ratings__stars nowrap' )
        if  hotel_star != None:      
                star =  hotel_star.find_all('span',class_='cf18357eee cf1a1ba763 _698592d8e6')              
                print('\n star count  = ',len(star)  )
                hotel_star =len(star) 

        else:
                hotel_star  = 0 
        # Collect Hotel delail data
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_StarRank] = str(hotel_star)       

        #2-2 Get Hotel  room prices ----------------------------------------------------------------------------
        hotel_room_prices =   soup_landing_page.find('div',  class_ = 'bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading')    
        for item in  hotel_room_prices:
                if item != None and item !='\n' and item !='':
                        price =  item.text.replace('\n','').replace('TWD','').replace('\xa0', '').replace(',','')
                        avg_price  = int(int(price)/6)
                        # .str[1].str.replace(',', '', regex=True).str.replace('$', '', regex=True)
                        # .replace(r'[^\x00-\x7F]+', '', regex=True).split('NT')
                        # '\nTWD\xa07,020\n'
                        print('\n avg  price = ',avg_price )
                        break
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_RoomPrice] =avg_price

        #2-3 Get Hotel  room prices ----------------------------------------------------------------------------


        #2-1 Get Hotels Address         
        hotel_address= soup_landing_page.find('p',  class_ = 'address address_clean')
        # locate correct data
        for data in hotel_address:
                if  'hp_address_subtitle'  in  data:
                        print('\n Get Address = ', data)
                        print('\n hotel address= ',data.text)
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_Address] = hotel_address.text               

    #5 Get Key/Important facility
        loop1 =[]  # Initial a list  for collect data             
        key_facility = soup_landing_page.find_all('div', class_='important_facility')
        print('\n Key / Important facility   ', key_facility)
        for item in key_facility:
                print('\n   fac = ',item.text)
                if item.text.strip() not in loop1:
                        loop1.append(item.text.strip())
        # Collect hotel data
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_KeyFacility] =loop1

        #4 Get a. Review Scores /Points -  b. review counts-----------------------------------------------
        hotel_review_scores = soup_landing_page.find('div', class_='eb2161f400 e5a32fd86b')
 
        if hotel_review_scores != None:
            print('\n Review Scores  ', hotel_review_scores.text)
            BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewScores] =  hotel_review_scores.text
        else:
            BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewScores] =  'empty'            

        hotel_review_counts = soup_landing_page.find('div', class_='_79b2b046b0 b33b89e42f _5586935da5 _6a1b6ff88e')
        if hotel_review_counts != None:
            print('\n Review Counts  ', hotel_review_counts.text)
            BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewCounts] =  hotel_review_counts.text
        else:
            BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewCounts] =  'empty'            
        
        #8 Get Hotel Img Link / Img List -----------------------------------------------------------------------------------------
        loop1 =[]
        img_block = soup_landing_page.find('div', class_='clearfix bh-photo-grid bh-photo-grid--space-down fix-score-hover-opacity')
        if  img_block == None:                        
                        img_block = soup_landing_page.find('div', class_=' gallery-side-reviews-wrapper js-no-close ')
        
        if img_block != None:
            for block in img_block:                
                    print('\n block = ', block )

            img_list = img_block.find_all('img')
            cnt= 0
            for img in img_list:
                print('\n # ' , cnt,'th img data' )
                if 'https://cf.bstatic.com/xdata/' in img['src']:
                    print('\n img  = ', img['src'] )
                    print('\n alt  = ', img['alt'] )
                    loop1.append(img['src'])
                cnt+=1
        # Collect Hotel delail data
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ImgList] = loop1

    #6 Get Review Content Block   -----------------------------------------------------------------------------------------------------
        loop1 =[]  # Initial a list  for collect data             
        # review_block = soup_landing_page.find_all('span', class_='c-review__body')
        review_block = soup_landing_page.find_all('div', class_='c-review-snippet')
        nation =''
        title=''
        content =''
        print('\n Key / Important facility   ', review_block)
        for item in review_block:
              data = item.find('span',class_ ='bui-avatar-block__title')
              if data != None: 
                      title = item.find('span',class_ ='bui-avatar-block__title').text.strip()
                      print('\n   tile = ',title)         
              data = item.find('span',class_ ='bui-avatar-block__subtitle')
              if data != None: 
                        nation = item.find('span',class_ ='bui-avatar-block__subtitle').text.strip()
                        print('\n   nation = ',nation)
              data  = item.find('span',class_ ='c-review__body')              
              if data != None: 
                        content = item.find('span',class_ ='c-review__body').text.strip()
                        print('\n   content = ',content)
              loop1.append([title,nation,content])          
        # Collect hotel  review data   
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewBlocks] =loop1
        
        #7 Get  Review Score Bar ------------------------------------------------------------------------------------------------------
        loop1 =[]  # Initial a list  for collect data    
        # <span class="c-score-bar__title">住宿地點</span>         
        # <span class="c-score-bar__score">9.0</span>
        # review_score_bar= soup_landing_page.find_all('li', class_='v2_review-scores__subscore hp_subscore_explanation_item_desktop')
        review_score_bar= soup_landing_page.find_all('ul', class_='v2_review-scores__subscore__inner v2_review-scores__subscore__inner-compared_to_average')
        if review_score_bar == None:
                review_score_bar= soup_landing_page.find_all('ul', class_=' v2_review-scores__subscore__inner v2_review-scores__subscore__inner-compared_to_average v2_review-scores__subscore__inner-single_column  hp_subscore_explanation_view ')
        print('\n review score bar   ', review_score_bar)
        for item in review_score_bar:
                if item != None :
                        if  item !='\n' :
                                if item !='\n\n': 
                                        print('\n i = ', item.find('span', class_='c-score-bar__title').text)
                                        print('\n j = ', item.find('span', class_='c-score-bar__value')['data-value'])
                                        print('\n item = ', item)
                                        i = item.find('span', class_='c-score-bar__title').text
                                        j = item.find('span', class_='c-score-bar__value')['data-value']
                                        loop1.append([i,j])
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_ReviewScrollBar] =  loop1


        #7 Get nearby landmark & hot spot
        loop1 =[]  # Initial a list  for collect data    
        nearbylandmark = soup_landing_page.find_all('div', class_='hp_location_block__section_container')        
        for item in nearbylandmark:
                print('\n landmark = ',item ) 
                try: 
                        titletxt  = item.find('span', class_= 'bui-title__text').text.strip()
                except:
                        titletxt  = item.text

                loop1=[]
                if '附近有什麼' in titletxt:  
                        print('\n nearby = ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n nearby  = ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearBy] =  loop1
                loop1=[]
                if '餐廳 & 咖啡店' in titletxt:                  
                        print('\n coffee or restaruant= ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n shop = ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearByCaffeRestaurant] =  loop1
                loop1=[]
                if '熱門景點' in titletxt:                  
                        print('\ntitle= ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n hot spot = ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearByHotSpot] =  loop1
                loop1=[]                                
                if '自然美景' in titletxt:  
                        print('\n nature = ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n spot = ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearByNatural] =  loop1
                loop1=[]
                if '大眾運輸' in titletxt:  
                        print('\n Transport = ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n bus or train= ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearByTrain] =  loop1
                loop1=[]                
                if '機場' in titletxt:  
                        print('\n AirPort = ',titletxt )
                        nearbylist =  item.find_all('li',class_='bui-list__item')
                        for i in nearbylist:
                                print('\n airport = ', i.text )
                                loop1.append(i.text)
                        if loop1 != None:
                                BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_NearByAirport] =  loop1

        #9 Get Hotel Facility List
        FaicilityList = soup_landing_page.find('div', class_='hotel-facilities__list')
        FaicilityBlock= FaicilityList.find_all('div', class_ ='hotel-facilities-group')
        loop1 =[]
        
        if FaicilityBlock != None:
            for block in FaicilityBlock:                
                    print('\n block = ', block )
                    if block !=  None:                        
                            print('\n text = ', block.text )
                            print('\n title = ', block.title )
                            loop1.append(block.text)
        BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_FacilityList] = loop1

        # Save Josn data   ==========================================================================
        todaydate_time = datetime.datetime.now()
        date_time = todaydate_time.strftime("%m_%d_%H_%M") 
        # Write Hotel Details dictionary  to file
        with open('d:\\'+BOOKing_HOTELs_DETAILs_DATA[BOOKing_HOTELs_KEY_STRs_Hotels_Id]+'_'+date_time+'.json', 'w', encoding="utf-8") as file_handler:
            json.dump(BOOKing_HOTELs_DETAILs_DATA, file_handler, ensure_ascii=False )
                     
        print('\n')
        print('\n')

