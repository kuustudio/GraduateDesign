from Demo1.ZXGKSpider.detail_Item import *
import json
from bs4 import BeautifulSoup
import time

class PeopleInfo():
    def __init__(self, infoDict, captchaId, verifyCode, htmlFetcher, dataFrame, useProxy = False):
        self.__infoDict= infoDict
        self.__caseCode = infoDict['caseCode']
        self.__name = infoDict['pname']
        self.__captchaId = captchaId
        self.__verifyCode = verifyCode
        self.__detailItems = []
        self.__useProxy = useProxy

        json1 = json.loads(infoDict['jsonObject'])
        self.__caseCreateTime = json1['caseCreateTime'] if infoDict['caseCreateTime'] is not None else None

        # print((self.__name, self.__caseCode, self.__caseCreateTime))

        self.__htmlFetcher = htmlFetcher

        self.__dataFrame = dataFrame

        if not self.__getDetailPage():
            print('获取新Item出现错误')
            time.sleep(5)
            raise SyntaxError

    def isNameEqual(self, name):
        return self.__name == name

    def __getDetailPage(self):
        self.__url = 'http://zxgk.court.gov.cn/zhzxgk/detailZhcx.do'

        self.__detailHeaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            #'Content-Length': '191',
            'Content-Type': 'application/x-www-form-urlencoded',
            #'Cookie': 'JSESSIONID=52777EDFD9A63F76F524E2336D53B5C6; UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; _gscu_15322769=18972572ixmhz018; _gscbrs_15322769=1; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619357881,1619358020,1619537171,1619665618; SESSION=5c8df22c-e0b6-4aee-86e4-942a9cd56a9a; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619690914; _gscs_15322769=t19690623akyq2e18|pv:4',
            'Host': 'zxgk.court.gov.cn',
            'Origin': 'http://zxgk.court.gov.cn',
            'Referer': 'http://zxgk.court.gov.cn/zhzxgk/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }

        self.__params = {
            'pnameNewDel': self.__name,
            'cardNumNewDel': '',
            'j_captchaNewDel': self.__verifyCode,
            'caseCodeNewDel': self.__caseCode,
            'captchaIdNewDel': self.__captchaId
        }

        page = self.__htmlFetcher.get_html(url=self.__url,
                                            count=1,
                                            useProxy=self.__useProxy,
                                            data=self.__params)
        # print(page)
        return self.__parsePage(page)

    def __parsePage(self, pageHtml):
        soup = BeautifulSoup(pageHtml, 'html.parser')

        tables = soup.find_all('div', class_ = 'col-lg-12 col-md-12 col-sm-12 row-block')

        for table in tables:
            title = table.find('div', class_ = 'col-lg-12 col-md-12 col-sm-12 bg-title').text
            self.__detailItems.append(
                DetailItem(table = table, title = title, dataFrame = self.__dataFrame))

        wholeFrameList = []
        for detailItem in self.__detailItems:
            itemFrameList = detailItem.dataFrameList
            if len(wholeFrameList) == 0:
                for frameValue in itemFrameList:
                    wholeFrameList.append(frameValue)
            else:
                for i in range(0, len(wholeFrameList)):
                    assert not (len(wholeFrameList[i]) > 1 and len(itemFrameList[i]) > 1)
                    if len(wholeFrameList[i]) == 0 and len(itemFrameList[i]) > 1:
                        wholeFrameList[i] = itemFrameList[i]
        try:
            self.__dataFrame.loc[self.__dataFrame.index.size] = wholeFrameList
            return True
        except:
            try:
                self.__dataFrame.loc[self.__dataFrame.index.size] = wholeFrameList
                return True
            except:
                return False