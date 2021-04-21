"""
    Main Class of CreditSpider
"""
from Demo1.config import *
from Demo1.HTML_Fetcher import HTML_Fetcher
from Demo1.CreditSpider.CreditPage import CreditPage

class CreditSpider():

    def __init__(self, keyWord):
        self.__keyword = keyWord
        self.__basicUrl = 'https://public.creditchina.gov.cn/private-api/catalogSearchHome'
        self.__htmlFetcher = HTML_Fetcher(name='信用中国', headers = headers_credit)
        self.__pages = []

    def __searchEachPage(self, pageNum):
        self.__param['page'] = str(pageNum)
        html = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                           useProxy = False,
                                           data = self.__param)
        self.__pages.append(CreditPage(html, self.__keyword))

    def getFirstPage(self):
        self.__param = {
            'keyword': self.__keyword,
            'scenes': 'defaultScenario',
            'tableName': 'credit_xyzx_tyshxydm',
            'searchState': '2',
            'entityType': '1, 2, 4, 5, 6, 7, 8',
            'templateId': '',
            'page': '1',
            'pageSize': '10'
        }
        first_html = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                           useProxy = False,
                                           data = self.__param)

        firstPage = CreditPage(first_html, self.__keyword)
        self.__pages.append(firstPage)

        for i in range(2, firstPage.totalPageNum + 1):
            self.__searchEachPage(i)


if __name__ == '__main__':
    spider = CreditSpider('腾讯')
    spider.getFirstPage()

