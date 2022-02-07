import requests
from bs4 import BeautifulSoup
import urllib.request as req


def print_news_info():

    url = 'https://news.daum.net/'

    res = req.urlopen(url)

    # print(url)

    soup = BeautifulSoup(res, 'html.parser')
    atag_list = soup.select("div.cont_thumb > strong.tit_g")
    # print(atag_list)

    output = []

    for atag in atag_list:
        a = atag.select_one('a')
        news_link = a.get('href')
        title = a.string
        output.append(title.strip() + '  ' + news_link.strip() + '\n\n')

    with open('daum_news.txt', 'w', encoding='utf-8') as f:
        for line in output:
            f.write(line)


print_news_info()
