def img_download():
    import requests
    from bs4 import BeautifulSoup
    import os
    import shutil

    base_url = 'https://comic.naver.com/webtoon/list?titleId=783054'
    url = 'https://comic.naver.com'

    res_chap = requests.get(base_url)

    chaplist = []

    if res_chap.ok:
        soup = BeautifulSoup(res_chap.text, 'lxml')
        chap_tags = soup.select("td.title")
        # print(chap_tags)

        for chap_tag in chap_tags:
            # print(chap_tag)
            a = chap_tag.select_one('a')
            chap_link = a.get('href')
            title = chap_tag.text.strip().lstrip()
            chaplist.append((title, chap_link))

    print(chaplist)

    # for item in chaplist:
    #     title = item[0]
    #     link = item[1]
    #
    #     chapter_url = 'https://comic.naver.com' + link
    #     res = requests.get(chapter_url)
    #
    #     # print(title, chapter_url)
    #     dir_path = 'img\\쇼미더럭키짱\\' + title + '\\'
    #     print(dir_path)
    #
    #     if not os.path.exists(dir_path):
    #         os.makedirs(dir_path)
    #
    #     if os.path.exists(dir_path):
    #         shutil.rmtree(dir_path)
    #
    #     if res.ok:
    #         soup = BeautifulSoup(res.text, 'lxml')
    #         img_tags = soup.select("img[src$='.jpg']")  # ^ = start, * = contain, $ = end, ~ = text
    #         # print(len(img_tags), type(img_tags))
    #
    #         req_header = {'referer':chapter_url}
    #
    #         img_cnt = 0
    #
    #         for img_tag in img_tags:
    #             # print(type(img_tag), img_tag)
    #             img_url = img_tag['src']
    #
    #             res_img = requests.get(img_url, headers=req_header)
    #             # print(res_img.ok)
    #
    #             if res_img.ok:
    #                 img_cnt += 1
    #                 img_title = dir_path + str(img_cnt) + '.jpg'
    #                 img_data = res_img.content
    #                 with open(img_title, 'wb') as file:
    #                     file.write(img_data)

img_download()