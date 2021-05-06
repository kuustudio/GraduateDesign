from Demo1.ZXGKSpider.Verifier import *
from Demo1.ZXGKSpider.PeopleInfo_ZX import *
import json
import os

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

        self.__dataFrameColumns = [
            '终本案件-案号',
            '终本案件-被执行人姓名/名称',
            '终本案件-性别',
            '终本案件-身份证号码/组织机构代码',
            '终本案件-执行法院',
            '终本案件-立案时间',
            '终本案件-终本日期',
            '终本案件-执行标的',
            '终本案件-未履行金额',
            '失信被执行人-被执行人姓名/名称',
            '失信被执行人-性别',
            '失信被执行人-身份证号码/组织机构代码',
            '失信被执行人-执行法院',
            '失信被执行人-省份',
            '失信被执行人-执行依据文号',
            '失信被执行人-立案时间',
            '失信被执行人-案号',
            '失信被执行人-做出执行依据单位',
            '失信被执行人-生效法律文书确定的义务',
            '失信被执行人-被执行人的履行情况',
            '失信被执行人-失信被执行人行为具体情形',
            '失信被执行人-发布时间',
            '限制消费人员-限制消费人员姓名',
            '限制消费人员-性别',
            '限制消费人员-身份证号码/组织机构代码',
            '限制消费人员-执行法院',
            '限制消费人员-省份',
            '限制消费人员-案号',
            '限制消费人员-立案时间',
            '限制消费人员-查看限消令',
            '被执行人-被执行人姓名/名称',
            '被执行人-身份证号码/组织机构代码',
            '被执行人-性别',
            '被执行人-执行法院',
            '被执行人-立案时间',
            '被执行人-案号',
            '被执行人-执行标的',
            '失信企业四类人信息-被执行人姓名/名称',
            '失信企业四类人信息-身份证号码/组织机构代码',
            '失信企业四类人信息-法定代表人',
            '失信企业四类人信息-执行法院',
            '失信企业四类人信息-省份',
            '失信企业四类人信息-立案时间',
            '失信企业四类人信息-案号',
            '失信企业四类人信息-生效法律文书确定的义务',
            '失信企业四类人信息-被执行人的履行情况',
            '失信企业四类人信息-失信被执行人行为具体情形',
            '失信企业四类人信息-发布时间'
        ]

        self.__dataFrame = pd.DataFrame(columns=self.__dataFrameColumns)

    def search(self, pName, pCardNum = '', currentPage = 1, exceptionFlag = False, useProxy = False):
        self.__form_data['currentPage'] = str(currentPage)

        if currentPage == 1:
            self.__form_data['pName'] = pName
            self.__form_data['pCardNum'] = pCardNum
            if not exceptionFlag:
                self.__dataFrame = pd.DataFrame(columns=self.__dataFrameColumns)

        if currentPage == 1 or exceptionFlag == True:
            (captchaId, randomNum, pCode) = self.__verifier.getVerifyInfo(1, False)
            self.__form_data['captchaId'] = captchaId
            self.__form_data['pCode'] = pCode
        else:
            (captchaId, pCode) = (self.__form_data['captchaId'], self.__form_data['pCode'])

        data = self.__html_fetcher.get_html(url=self.__url,
                                            count=1,
                                            useProxy=useProxy,
                                            data=self.__form_data)

        try:
            json1 = json.loads(data)
        except:
            try:
                json1 = json.loads(data)
            except:
                print('爬取过程中出现错误！[json & data & totalPageNum & result]')
                if exceptionFlag:
                    print('连续在此处出现错误，取消本次爬取！')
                    time.sleep(3)
                    return False
                return self.search(pName, pCardNum, currentPage, exceptionFlag = True, useProxy = useProxy)
        try:
            dataDict = json1[0]
            totalPageNum = dataDict['totalPage']
            result = dataDict['result']
        except:
            print('爬取过程中出现错误！[dataDict & totalPageNum & result]')
            return self.search(pName, pCardNum, currentPage, exceptionFlag=True, useProxy=useProxy)


        print('获取第 ' + str(currentPage) + ' 页，被执行人：' + pName + ' 的信息。' + '共 ' + str(totalPageNum) + ' 页。')

        if pName not in self.__peopleInfos.keys():
            assert currentPage == 1
            self.__peopleInfos[pName] = []

        temp_list = []
        isNotSame = False
        for each in result:
            try:
                peopleInfo = PeopleInfo(each, captchaId, pCode, self.__html_fetcher, self.__dataFrame, useProxy = useProxy)
                if not peopleInfo.isNameEqual(pName):
                    print('截至当前页，姓名已经不相同，停止对该名称用户人的爬取。')
                    isNotSame = True
                    break
            except:
                return self.search(pName, pCardNum, currentPage, exceptionFlag=True, useProxy=useProxy)
            temp_list.append(peopleInfo)

        for peopleInfo in temp_list:
            self.__peopleInfos[pName].append(peopleInfo)

        if isNotSame:
            return True

        if totalPageNum > 1:
            if currentPage == totalPageNum:
                return True
            else:
                return self.search(pName, pCardNum, currentPage + 1,
                            exceptionFlag = False,
                            useProxy = useProxy)
        else:
            return True

        # print(data)

    def infoSave2Csv(self, name):
        self.__dataFrame.to_csv(name + '.csv', encoding='utf-8-sig', index=False)

    def deletePeopleInfo(self, pName):
        if pName in self.__peopleInfos.keys():
            del self.__peopleInfos[pName]

if __name__ == '__main__':
    peopleSpider = PeopleSpider()
    #peopleSpider.search('谢建华')
    path = os.getcwd()

    with open('../HzaeeSpider/name.txt') as f:
        a = f.read().split('\n')
        nameSet = set(a)

    for name in nameSet:
        hasFlag = False
        for i in os.listdir(path):
            if '.csv' in i:
                fileName = i[0: i.find('.')]
                if name == fileName:
                    hasFlag = True
                    break
        if not hasFlag:
            succeed = peopleSpider.search(name, useProxy=True)
            if succeed:
                peopleSpider.infoSave2Csv(name)
            else:
                print('本次爬取', name, '中途出现问题，后续重新进行爬取')
                peopleSpider.deletePeopleInfo(name)

