import requests
from bs4 import BeautifulSoup
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

res = requests.get(url)
if res.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    location_tag = soup.find('location', attrs={'wl_ver':3})
    location_dict = {} #dict()

    location_dict['province'] = location_tag.find('province').text
    location_dict['city'] = location_tag.find('city').text

    data_tags = location_tag.find_all('data')
    data_list = []
    for data_tag in data_tags:
        data_dict = {}
        data_dict['mode'] = data_tag.find('mode').text
        data_dict['tmEf'] = data_tag.find('tmef').text
        data_dict['wf'] = data_tag.find('wf').text
        data_dict['tmn'] = data_tag.find('tmn').text
        data_dict['tmx'] = data_tag.find('tmx').text
        data_list.append(data_dict)

    location_dict['datas'] = data_list
    print(location_dict)