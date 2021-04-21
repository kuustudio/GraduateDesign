import json
from Demo1.CreditSpider.CreditItem import *

class CreditPage():
    def __init__(self, html, keyWord):
        self.__html = html
        self.keyWord = keyWord

        json1 = json.loads(self.__html)
        data = json1['data']
        self.__totalItemNum = data['total']
        self.totalPageNum = data['totalSize']
        self.__itemsInfolist = data['list']
        self.__items = []

        self.__analyseItems()

    def __analyseItems(self):
        for itemInfo in self.__itemsInfolist:
            item = CreditItem(itemInfo)
            self.__items.append(item)