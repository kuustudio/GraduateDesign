"""
@brief:爬取政府采购网，需要输入关键字

"""
from PurchaseSpider.Page import Page
import time

class Purchase():
    pages = []

    def __init__(self):
        pass

    def getPageUrl(self, keyword):
        page = Page(1)
        page.buildUrl(keyword=keyword)
        page.getPage()
        itemNum = page.analyseItem()
        self.pages.append(page)

        if (itemNum > 20):
            '''
                有多页
            '''
            pageNum = int(itemNum / 20) + 1
            for index in range(2, pageNum + 1):
                time.sleep(3)
                page_next = Page(index)
                page_next.buildUrl(keyword=keyword, page_index=index)
                page_next.getPage()
                if (index == pageNum):
                    page_next.analyseItem(last_page=True)
                else:
                    page_next.analyseItem(last_page=False)
                self.pages.append(page_next)
        return page.url


if __name__ == '__main__':
    purchase = Purchase()
    keyword = '机'
    purchase.getPageUrl(keyword)
