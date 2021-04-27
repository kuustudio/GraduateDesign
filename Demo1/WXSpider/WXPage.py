from bs4 import BeautifulSoup
from Demo1.WXSpider.WXArticleItem import *
import pandas as pd

class WXPage():

    def __init__(self, html, num, dataframe):
        self.__html = html
        self.__items = []
        self.__pageNum = num
        self.__dataframe = dataframe

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='news-box')

        items = div.find_all('li')

        browser = webdriver.Chrome()
        browser.get('https://weixin.sogou.com')
        for cookie in Cookie_init_wx_list:
            browser.add_cookie(cookie)

        for i in items:
            href = i.find('h3').find('a')['href']
            info = i.text.strip().split('\n\n')
            title = info[0]
            brief = info[1]
            gzh = info[2][0 : info[2].find('document.write')]
            #print(gzh)
            article = WXArticleItem(href, title, brief, gzh, browser)
            self.__items.append(article)
        browser.close()
        self.__info2csv()

    def __info2csv(self):

        for item in self.__items:
            info = item.getInfo()
            self.__dataframe.loc[self.__dataframe.index.size] = info