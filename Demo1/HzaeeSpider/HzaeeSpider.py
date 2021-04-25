from Demo1.HTML_Fetcher import HTML_Fetcher
from Demo1.HzaeeSpider.HzaeeItem import *
from Demo1.config import *
import json
import math

class HzaeeSpider():
    def __init__(self):
        self.__htmlFetcher = HTML_Fetcher(name='杭州产权', headers=headers_hzaee)

        self.__params = {
            'page': '1',
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': '国有项目',
            'subjectType': '产权转让',
            'subjectDetailType': '正式披露'
        }

        self.__estate = ['房产','机动车','设备物资','罚没物资','债权','其他']

        self.__basicUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/page'
        self.__CQZRs_formal = []
        self.__CQZRs_informal = []
        self.__ZCZRs = []
        self.__QYZZs = []
        self.__FWZLs = []
        self.__ZSs = []
        self.__ELSEs = []

        self.__dataFrame = None

    def startDownload(self):
        print('产权转让：披露， 国有')
        self.__getCQZR_formal(guoyou=True)
        print('产权转让：非披露， 国有')
        self.__getCQZR_informal(guoyou=True)
        for type in self.__estate:
            print('资产转让：' + type + '， 国有')
            self.__getZCZR(guoyou=True, Type=type)
        #self.__getQYZZ(guoyou=True)
        #self.__getZS(True)
        print('房屋租赁， 国有')
        self.__getFWZL(True)
        #self.__getELSE(True)

        print('产权转让：披露， 非国有')
        self.__getCQZR_formal(guoyou=False)
        print('产权转让：非披露， 非国有')
        self.__getCQZR_informal(guoyou=False)
        for type in self.__estate:
            print('资产转让：' + type + '， 非国有')
            self.__getZCZR(guoyou=False, Type=type)
        #self.__getQYZZ(guoyou=False)
        #self.__getZS(False)
        print('房屋租赁， 非国有')
        self.__getFWZL(False)
        #self.__getELSE(False)

        self.__dataFrame.to_csv('result.csv', encoding = 'utf-8-sig')


    def __text2dict(self, txt):
        json1 = json.loads(txt)
        return json1['data']

    """
        Itemtype : 1 
        产权转让
            正式披露
    """
    def __getCQZR_formal(self, guoyou, pageNum = 1):
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'subjectType': '产权转让',
            'subjectDetailType': '正式披露'
        }
        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                                 useProxy=False,
                                                 data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__CQZRs_formal.append(hzaeeItem)

        if info['totalPage'] > 1:
            if pageNum == info['totalPage']:
                return
            self.__getCQZR_formal(guoyou, pageNum=pageNum + 1)
        else:
            return

    """
        Itemtype : 2
        产权转让
            预批露
    """
    def __getCQZR_informal(self, guoyou, pageNum = 1):
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'subjectType': '产权转让',
            'subjectDetailType': '预披露'
        }
        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy = False,
                                          data = self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=2, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__CQZRs_informal.append(hzaeeItem)

        if info['totalPage'] > 1:
            if pageNum == info['totalPage']:
                return
            self.__getCQZR_informal(guoyou, pageNum=pageNum + 1)
        else:
            return

    """
        Itemtype : 3
        资产转让
        :param Type 范围：(房产，机动车，设备物资，罚没物资，债权，其他)            
    """
    def __getZCZR(self, guoyou, pageNum = 1, Type = '房产'):
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'subjectType': '资产转让',
            'subjectDetailType': Type
        }
        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy=False,
                                          data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=3, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__ZCZRs.append(hzaeeItem)

        if info['totalPage'] > 1:
            if pageNum == info['totalPage']:
                return
            self.__getZCZR(guoyou, pageNum=pageNum + 1, Type = Type)
        else:
            return

    """
        Itemtype : 4
        企业增资
    """
    def __getQYZZ(self, guoyou, pageNum = 1):
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'subjectType': '企业增资'
        }
        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy=False,
                                          data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=4, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__QYZZs.append(hzaeeItem)

        if info['totalPage'] > 1:
            if pageNum == info['totalPage']:
                return
            self.__getQYZZ(guoyou, pageNum=pageNum + 1)
        else:
            return

    """
        Itemtype : 5
        房屋租赁
    """
    def __getFWZL(self, guoyou, pageNum = 1):
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'subjectType': '房屋租赁'
        }
        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy=False,
                                          data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=5, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__FWZLs.append(hzaeeItem)

        if info['totalPage'] > 1:
            if pageNum == info['totalPage']:
                return
            self.__getFWZL(guoyou, pageNum=pageNum + 1)
        else:
            return

    """
        Itemtype : 6
        招商信息
    """
    def __getZS(self, guoyou, pageNum = 1):
        self.__basicUrl = 'https://www.hzaee.com/api/api/project/page'
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'status': '已发布',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'projectCategory': '招商'
        }

        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy=False,
                                          data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=6, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__ZSs.append(hzaeeItem)

        if info['total'] > 15:
            wholePageNum = math.ceil(info['total'] / 15)
            if pageNum == wholePageNum:
                self.__basicUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/page'
                return
            self.__getZS(guoyou, pageNum=pageNum + 1)
        else:
            self.__basicUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/page'
            return

    """
        Itemtype : 7
        其他信息
    """
    def __getELSE(self, guoyou, pageNum = 1):
        self.__basicUrl = 'https://www.hzaee.com/api/api/project/page'
        self.__params = {
            'page': str(pageNum),
            'limit': '15',
            'order': 'desc',
            'orderField': 'release_time',
            'status': '已发布',
            'projectType': ('国有项目' if guoyou else '非国有项目'),
            'projectCategory': '其他'
        }

        txt = self.__htmlFetcher.get_html(self.__basicUrl, 1,
                                          useProxy=False,
                                          data=self.__params)
        info = self.__text2dict(txt)

        currentPageInfo = info['list']
        for item in currentPageInfo:
            hzaeeItem = HzaeeItem(guoyou, item, ItemType=7, htmlFetcher=self.__htmlFetcher)
            self.__dataFrame = hzaeeItem.item2csv(self.__dataFrame)
            self.__ELSEs.append(hzaeeItem)

        if info['total'] > 15:
            wholePageNum = math.ceil(info['total'] / 15)
            if pageNum == wholePageNum:
                self.__basicUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/page'
                return
            self.__getELSE(guoyou, pageNum=pageNum + 1)
        else:
            self.__basicUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/page'
            return

if __name__ == '__main__':
    spider = HzaeeSpider()
    spider.startDownload()
