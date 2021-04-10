from Demo1.PurchaseSpider.PurchaseItem import PurchaseItem
import re


class Page():
    url = "http://search.ccgp.gov.cn/bxsearch?"

    # 选项
    """
        bidType:    类型， 默认0
        0- 所有类型
        1- 公开招标
        2- 询价公告
        3- 竞争性谈判
        4- 单一来源
        5- 资格预审
        6- 邀请公告
        7- 中标公告
        8- 更正公告
        9- 其他公告
        10- 竞争性磋商
        11- 成交公告
        12- 终止公告
    """
    bidType = 0

    """
        bidSort:    类别， 默认0
            0- 所有类别
            1- 中央公告
            2- 地方公告
    """
    bidSort = 0

    """
        pinMu:  品目， 默认0
            0- 所哟品目
            1- 货物类
            2- 工程类
            3- 服务类
    """
    pinMu = 0

    timeType = 5  # 时间模式，1为今日，2为近三日，3为近一周，4为近一月。5为近三月，6为近半年

    """
        关键词
    """
    kw = ""

    """
        后续调节参数
    """
    searchtype = 1  # 无意义选项
    page_index = 1  # 页号
    start_time = 0  # 查找开始时间
    end_time = 0  # 查找结束时间

    """
        无意义的参数
    """
    searchparam = 0
    searchchannel = 0
    dbselect = "bidx"
    buyerName = ""
    projectId = 0
    displayZone = 0
    zoneId = 0
    agentName = ""

    '''
        每项采购条目
    '''
    Items = []

    '''
        页面HTML
    '''
    pageText = ''

    pageNumber = 1

    def __init__(self, pageNumber, keyword, html_fetcher):
        self.pageNumber = pageNumber
        self.keyword = keyword
        self.html_fetcher = html_fetcher
        self.Items = []
        print('爬取第 %d 页信息' % pageNumber, end='')

    def __buildUrl(self):
        self.url += "searchtype=" + str(self.searchtype)
        self.url += '&' + "kw=" + self.keyword
        self.url += '&' + "bidType=" + str(self.bidType)
        self.url += '&' + 'bitSort=' + str(self.bidSort)
        self.url += '&' + 'pinMu=' + str(self.pinMu)
        self.url += '&' + 'timeType=' + str(self.timeType)
        if (self.pageNumber > 1):
            self.url += '&' + 'page_index=' + str(self.pageNumber)
        print(' URL:' + self.url)

    def getUrl(self):
        return self.url

    """
        @brief: 设置参数接口
    """
    def setParam(self):
        pass

    def getPage(self):
        self.__buildUrl()
        self.pageText = self.html_fetcher.get_html(url=self.url, count=1, useProxy=False)
        return self.pageText

    def __getItemNum(self):
        pattern = '共找到.*>(\d+)<.*?条内容'
        # print(self.pageText)
        result = re.search(pattern, self.pageText, re.S).group(1)
        itemNum = int(result)
        return itemNum

    def __getEachItemText(self):
        pattern = '<ul\sclass="vT\-srch\-result\-list\-bid">(.*?)<div\sclass="vT\-srch\-result\-page\-con">'

        items_text = re.search(pattern, self.pageText, re.S).group(1)
        # item_text包含所有本页条目文本信息

        pattern_each = '<li>(.*?)</li>'

        itemsText = re.findall(pattern_each, items_text, re.S)

        return itemsText

    def analyseItem(self, last_page=False):
        itemNum = self.__getItemNum()
        itemsText = self.__getEachItemText()
        if itemNum <= 20:
            for i in range(1, itemNum + 1):
                item = PurchaseItem(itemsText[i - 1])
                item.analyseItem()
                self.Items.append(item)
        else:
            pageNum = 20 + 1
            if (last_page == True):
                pageNum = itemNum % 20 + 1
            for i in range(1, pageNum):
                item = PurchaseItem(itemsText[i - 1])
                item.analyseItem()
                self.Items.append(item)
        return itemNum