from selenium import webdriver
from Demo1.config import *

class WXArticleItem():
    def __init__(self, href, title, brief, gzh, browser):
        self.__href = href
        self.__title = title
        self.__brief = brief
        self.__gzh = gzh
        self.__browser = browser
        #print(href)
        self.__getDetail()

    def __getDetail(self):
        url = 'https://weixin.sogou.com' + self.__href
        self.__browser.get(url)
        while True:
            try:
                content = self.__browser.find_element_by_xpath('//*[@id="js_content"]')
                self.__details = content.text
                print(content.text)
                break
            except:
                continue

    def getInfo(self):
        data = [self.__title, self.__brief, self.__gzh, self.__details]
        return data

