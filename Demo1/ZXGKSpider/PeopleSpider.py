from Demo1.ZXGKSpider.Verifier import *
from Demo1.ZXGKSpider.PeopleInfo_ZX import *
import json

class PeopleSpider():
    '''
        被执行人爬虫
    '''
    def __init__(self):
        self.__url = 'http://zxgk.court.gov.cn/zhzxgk/searchZhcx.do'
        self.__PostHeader = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Connection': 'keep-alive',
            # 'Content-Length': '284',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'JSESSIONID=E9C61273BEE39B1A7789FBE075E3AD45; UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; _gscu_15322769=18972572ixmhz018; SESSION=e68c7979-c0dc-4288-878d-dcd7260584a5; _gscbrs_15322769=1; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619357881,1619358020,1619537171,1619665618; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619665618; _gscs_15322769=19665617d3m7d317|pv:5',
            'Host': 'zxgk.court.gov.cn',
            'Origin': 'http://zxgk.court.gov.cn',
            'Referer': 'http://zxgk.court.gov.cn/zhzxgk/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.__html_fetcher = HTML_Fetcher(name='被执行人',
                                           headers=self.__PostHeader,
                                           request_type='POST')
        self.__form_data = {
            'pName': '', #被执行人名称
            'pCardNum': '', #身份证号 / 社会信用代码
            'selectCourtId': '0',
            'pCode': '', #pCode
            'captchaId': '', #captchaId
            'searchCourtName': '全国法院（包含地方各级法院）',
            'selectCourtArrange': '1',
            'currentPage': '1' #default : 1
        }

        self.__verifier = ZXGKVerifier()

        self.__peopleInfos = {}

    def search(self, pName, pCardNum = ''):
        self.__form_data['pName'] = pName
        self.__form_data['pCardNum'] = pCardNum
        (captchaId, randomNum, pCode) = self.__verifier.getVerifyInfo(1)
        self.__form_data['captchaId'] = captchaId
        self.__form_data['pCode'] = pCode
        #print('获取第 1 页，被执行人：' + pName + ' 的信息')
        data = self.__html_fetcher.get_html(url=self.__url,
                                            count=1,
                                            useProxy=False,
                                            data=self.__form_data)

        json1 = json.loads(data)
        dataDict = json1[0]
        totalPageNum = dataDict['totalPage']
        result = dataDict['result']

        if pName not in self.__peopleInfos.keys():
            self.__peopleInfos[pName] = []

        for each in result:
            peopleInfo = PeopleInfo(each, captchaId, pCode, self.__html_fetcher)
            self.__peopleInfos[pName].append(peopleInfo)

        for i in range(2, totalPageNum + 1):
            self.__form_data['currentPage'] = str(i)
            #print('获取第 '+ str(i) + ' 页，被执行人：' + pName + ' 的信息')
            data = self.__html_fetcher.get_html(url=self.__url,
                                                count=1,
                                                useProxy=False,
                                                data=self.__form_data)
            json1 = json.loads(data)
            dataDict = json1[0]
            result = dataDict['result']
            for each in result:
                peopleInfo = PeopleInfo(each, captchaId, pCode, self.__html_fetcher)
                self.__peopleInfos[pName].append(peopleInfo)
        # print(data)

if __name__ == '__main__':
    peopleSpider = PeopleSpider()
    peopleSpider.search('王刚')
