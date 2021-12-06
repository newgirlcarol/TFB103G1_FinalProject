import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema


# information for session
headers = {
    "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    "Referer": 'https://taiwanstay.net.tw/'
}
record = 0
url = f'https://taiwanstay.net.tw/legal-hotel-list?offset=20&search_keyword=&hoci_city=%E5%85%A8%E9%83%A8&start={record}'
stay_list = list()


for page in range(1, 676):
    try:
        ss = requests.session()
        res_taiwanStay = ss.get(url, headers=headers)
        taiwanStay_html = BeautifulSoup(res_taiwanStay.text, 'html.parser')

        for data in taiwanStay_html.select('div[class="news-v3-in-sm no-padding"]'):
            title = data.select('a')[0].text
            stay_list.append(title + ' 100' + ' n' + '\n')
    except (KeyError, IndexError, MissingSchema):
        pass

    record += 20
    url = f'https://taiwanstay.net.tw/legal-hotel-list?offset=20&search_keyword=&hoci_city=%E5%85%A8%E9%83%A8&start={record}'
    print("finish page {}".format(page))

    if (page % 15 == 0):
        time.sleep(7)

with open('./jiebaDict_stay.txt', "w", encoding="utf-8") as f:
    f.write('stay 100 n')

for i in stay_list:
    with open('./jiebaDict_stay.txt',  "a", encoding="utf-8") as f:
        f.write(i)