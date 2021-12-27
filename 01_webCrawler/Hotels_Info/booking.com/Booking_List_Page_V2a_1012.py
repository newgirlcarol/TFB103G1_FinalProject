import requests
from bs4 import BeautifulSoup
import  Booking_Main_Page_V3a_1014
import datetime
import time
import random
import re
# information for session
# Web Agent not for
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
headers = {'User-Agent' : userAgent}

# TPE city start up Url
url_landing_page_TPE_P1  = 'https://www.booking.com/searchresults.zh-tw.html?label=gog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAKGw6iLBsACAdICJDYxNmU1ZTU1LTZiMjAtNGQwYi1iMWIxLWNlN2M4ZTkzY2E5MNgCBOACAQ&sid=42ea0faf82d3ec67b895b6ab0ce75d98&aid=397594&lang=zh-tw&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.zh-tw.html%3Faid%3D397594%3Blabel%3Dgog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAKGw6iLBsACAdICJDYxNmU1ZTU1LTZiMjAtNGQwYi1iMWIxLWNlN2M4ZTkzY2E5MNgCBOACAQ%3Bsid%3D42ea0faf82d3ec67b895b6ab0ce75d98%3Bsb_price_type%3Dtotal%26%3B&ss=%E5%8F%B0%E5%8C%97&is_ski_area=0&ssne=%E5%8F%B0%E5%8C%97&ssne_untouched=%E5%8F%B0%E5%8C%97&dest_id=-2637882&dest_type=city&checkin_year=2021&checkin_month=12&checkin_monthday=12&checkout_year=2021&checkout_month=12&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&offset='

# New TPE city start up Url\
url_landing_page_NEW_TPE_P1= 'https://www.booking.com/searchresults.zh-tw.html?label=gog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAKYwaiLBsACAdICJDRjZDdjNTM4LTNlYzQtNDJlZS04Mjk4LWQ5NTY3NGI4Y2Y3M9gCBOACAQ&sid=42ea0faf82d3ec67b895b6ab0ce75d98&aid=397594&lang=zh-tw&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.zh-tw.html%3Faid%3D397594%3Blabel%3Dgog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAKYwaiLBsACAdICJDRjZDdjNTM4LTNlYzQtNDJlZS04Mjk4LWQ5NTY3NGI4Y2Y3M9gCBOACAQ%3Bsid%3D42ea0faf82d3ec67b895b6ab0ce75d98%3Bsb_price_type%3Dtotal%26%3B&ss=%E6%96%B0%E5%8C%97%E5%B8%82%2C+%E8%87%BA%E7%81%A3&is_ski_area=0&ssne=%E5%8F%B0%E5%8C%97&ssne_untouched=%E5%8F%B0%E5%8C%97&checkin_year=2021&checkin_month=12&checkin_monthday=12&checkout_year=2021&checkout_month=12&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ac_position=0&ac_langcode=xt&ac_click_type=b&dest_id=5245&dest_type=region&place_id_lat=25.081503&place_id_lon=121.668814&search_pageview_id=0fd0054c51e90108&search_selected=true&region_type=province&ss_raw=%E6%96%B0%E5%8C%97%E5%B8%82&offset='

# YILAN city start up Url
url_landing_page_YILAN_CITY_P1  = 'https://www.booking.com/searchresults.zh-tw.html?label=gog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAK1xKiLBsACAdICJDhjN2YzM2I2LThjMDQtNDFkNS1hMDNjLWVmMzNmMzM2ODgzOdgCBOACAQ&sid=42ea0faf82d3ec67b895b6ab0ce75d98&aid=397594&lang=zh-tw&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.zh-tw.html%3Faid%3D397594%3Blabel%3Dgog235jc-1DCAEoggI46AdIMFgDaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuAK1xKiLBsACAdICJDhjN2YzM2I2LThjMDQtNDFkNS1hMDNjLWVmMzNmMzM2ODgzOdgCBOACAQ%3Bsid%3D42ea0faf82d3ec67b895b6ab0ce75d98%3Bsb_price_type%3Dtotal%26%3B&ss=%E5%AE%9C%E8%98%AD%E5%B8%82&is_ski_area=0&ssne=%E5%8F%B0%E5%8C%97&ssne_untouched=%E5%8F%B0%E5%8C%97&checkin_year=2021&checkin_month=12&checkin_monthday=12&checkout_year=2021&checkout_month=12&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=%E5%AE%9C%E8%98%AD%E5%B8%82&search_pageview_id=4bff061a6c75001b&search_pageview_id=4bff061a6c75001b&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&offset='
url_landing_page_YILAN_COUNTY_P1  = 'https://www.booking.com/searchresults.zh-tw.html?label=gen173nr-1DCAEoggI46AdIMFgEaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuALixaiLBsACAdICJGQxMTc2MTc2LWQ4NDktNGUzYy1iMTNhLWRlMWFkOWY4NDIwM9gCBOACAQ&sid=42ea0faf82d3ec67b895b6ab0ce75d98&aid=304142&lang=zh-tw&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.zh-tw.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIMFgEaOcBiAEBmAEwuAEXyAEM2AED6AEB-AECiAIBqAIDuALixaiLBsACAdICJGQxMTc2MTc2LWQ4NDktNGUzYy1iMTNhLWRlMWFkOWY4NDIwM9gCBOACAQ%3Bsid%3D42ea0faf82d3ec67b895b6ab0ce75d98%3Bsb_price_type%3Dtotal%26%3B&ss=%E5%AE%9C%E8%98%AD%E7%B8%A3&is_ski_area=0&ssne=%E5%AE%9C%E8%98%AD%E5%B8%82&ssne_untouched=%E5%AE%9C%E8%98%AD%E5%B8%82&checkin_year=2021&checkin_month=12&checkin_monthday=12&checkout_year=2021&checkout_month=12&checkout_monthday=17&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&search_pageview_id=00c5067129bb0063&ss_raw=%E5%AE%9C%E8%98%AD%E7%B8%A3&offset='
#  Initial Start value, Just a trigger value
hotel_page_count = 0
hotel_total_counts=20

# Start Url Session
ss = requests.session()

# while hotel_page_count < hotel_total_counts:
while True:
        print('\n start loop')
        # just a break
        time.sleep(random.randint(1,4))

        # Combine hotel url  then  get the soup
        # Modify start page here        
        nexturl =url_landing_page_YILAN_CITY_P1+str(hotel_page_count)        
        # Get the hotel list from page data
        res_landing_page = ss.get(nexturl, headers=headers)
        soup_landing_page = BeautifulSoup(res_landing_page.text, 'html.parser')
        print('\n get soup data  on the HOTEL LIST page= ',  hotel_page_count)

        #  Get how many  hotels  at first
        total_hotel_found = soup_landing_page.find('div', class_ = 'results-meta sr_results_footer__container')           
        if total_hotel_found != None:
            found_txt= total_hotel_found.text.replace('：','').replace(' ','_').replace('\n','')
            hotel_total_counts = int( ''.join(filter(str.isdigit, total_hotel_found.text)))
            print ('\n  Total found #  ',hotel_total_counts )
            # Get time variables
            todaydate_time = datetime.datetime.now()
            date_time = todaydate_time.strftime("%m_%d_%H_%M") 
            with open('d:\\ '+str(found_txt)+ str(hotel_total_counts) +'_'+date_time+'.txt', 'w',encoding='utf-8') as f:
                data = ' \n hotel total found # =  '+ str(hotel_total_counts) +'\n'+str(found_txt)
                f.write("%s\n" % data)

        # Get Hotel Link List   ==============
        # Hotel_List_Block = soup_landing_page.find('div',class_='_8d5a9180d4') 
        Hotel_List_Block = soup_landing_page.find('div',class_='_814193827') 
               
        # Get the Url link
        Hotel_List =  Hotel_List_Block.find_all('a', href=True)
        hotel_url_list = []
        all_page_url_list = []
        for item in Hotel_List:
                print('\n hotel web link  == ', item.get('href'))
                detail_url = item.get('href')
                # Save hotel url but not 
                all_page_url_list.append(detail_url)
                if 'from_sr_card=1' in detail_url:
                        hotel_url_list.append(detail_url)
        # Get time variables
        todaydate_time = datetime.datetime.now()
        date_time = todaydate_time.strftime("%m_%d_%H_%M") 

        # Save Hotel url  only to text file    ==========================================================================               
        print('\n hotel lsit link = ',hotel_url_list)        
        with open('d:\\hotel_url_list_hotelonly_p'+ str(hotel_page_count) +'_'+date_time+'.txt', 'w',encoding='utf-8') as f:
                for item in hotel_url_list:
                        f.write("%s\n" % item)
        # Save url data   ==================================================================================
        with open('d:\\hotel_all_url_list_p'+ str(hotel_page_count) +'_'+date_time+'.txt', 'w',encoding='utf-8') as f:
                for link in all_page_url_list:
                        f.write("%s\n" % link)

        # Get the Hotel deital 
        for url in hotel_url_list:
                # Just a break
                time.sleep(random.randint(2,8))
                # Get into hotel details @ main page
                Booking_Main_Page_V3a_1014.ScrapeHotelDetails(url)
                #Check if its the last page or not
        if  len(hotel_url_list) >= 25:
                hotel_page_count +=len(hotel_url_list)
                # Just a break
                time.sleep(random.randint(2,5))
                print('\n current hotel counts = ',hotel_page_count,'\n Now go to next' )
        else:
                # Just a break
                time.sleep(random.randint(2,8))
                hotel_page_count +=  len(hotel_url_list)
                print('current hotel count = \n ',hotel_page_count )
                # if hotel_page_count >= hotel_total_counts:
                if  len(hotel_url_list) < 25:
                        with open('d:\\ TheEnd_hotel count_'+ str(hotel_page_count) +'_'+date_time+'.txt', 'w',encoding='utf-8') as f:
                                data = ' \n Parsing hotel total count =  '+ str(hotel_page_count)
                                f.write("%s\n" % data)
                        print('\n ==End of Page ==\n')
                        break


print('')
print('')

