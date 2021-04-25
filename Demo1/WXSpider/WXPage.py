from bs4 import BeautifulSoup
from Demo1.WXSpider.WXArticleItem import *

class WXPage():

    def __init__(self, html, num):
        self.__html = html
        self.__items = []

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_='news-box')

        items = div.find_all('li')

        for i in items:
            href = i.find('h3').find('a')['href']
            info = i.text.strip().split('\n\n')
            title = info[0]
            brief = info[1]
            gzh = info[2][0 : info[2].find('document.write')]
            #print(gzh)
            article = WXArticleItem(href, title, brief, gzh)
            self.__items.append(article)