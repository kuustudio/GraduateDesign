"""
@brief:爬取政府采购网，需要输入关键字

"""
from Demo1.PurchaseSpider.PurchasePage import Page
from Demo1.HTML_Fetcher import HTML_Fetcher
from Demo1.config import *

class Purchase():
    def __init__(self, keyword):
        self.__html_fetcher = HTML_Fetcher(name = '政府采购网',
                                         headers = headers_purchase)
        self.__pages = []
        self.__keyword = keyword

    def getAllPages(self):
        page = Page(1, self.__keyword, self.__html_fetcher)
        page.getPage()
        itemNum = page.analyseItem()
        self.__pages.append(page)

        if (itemNum > 20):
            '''
                有多页
            '''
            pageNum = int(itemNum / 20) + 1
            for index in range(2, pageNum + 1):
                time.sleep(2)
                page_next = Page(index, self.__keyword, self.__html_fetcher)
                page_next.getPage()
                if (index == pageNum):
                    page_next.analyseItem(last_page=True)
                else:
                    page_next.analyseItem(last_page=False)
                self.__pages.append(page_next)

# if __name__ == '__main__':
#     purchase = Purchase('机')
#     purchase.getAllPages()