from Demo1.HTML_Fetcher import *
from Demo1.config import *
import execjs
import json
from Demo1.WenshuSpider.WenshuItemDetails import *


class WenshuSpider():
    def __init__(self):
        self.__cookie = Cookie_init_Wenshu

        self.__wenshu_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Connection': 'keep-alive',
            # 'Content-Length': '709',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': self.__cookie,
            'Host': 'wenshu.court.gov.cn',
            'Origin': 'https://wenshu.court.gov.cn',
            # 'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=c2c0bdb832a4221d3548cdc366f9812b&s8=02',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.__htmlFetcher = HTML_Fetcher('中国裁判文书网',
                                          headers = self.__wenshu_headers,
                                          request_type = 'POST')
        self.__data = {
            #'pageId': 'c2c0bdb832a4221d3548cdc366f9812b',
            's8': '02',
            'sortFields': 's50:desc',
            'ciphertext': '1010111 1001101 1111000 1000100 1100111 1100010 1000110 110111 1111010 1100111 1101000 1100101 1000010 1010010 1110100 1110010 1100111 1101001 1100101 1110100 1000100 1001011 1010000 1001111 110010 110000 110010 110001 110000 110101 110000 110110 1001100 101011 1111000 1001111 1001100 1000011 111000 1111001 1100101 1010110 1110011 1010011 1001101 1100100 110101 1110110 1000011 110110 1110110 1001100 1010110 1000001 111101 111101',
            'pageNum': '1',
            'queryCondition': '[{"key":"s8","value":"02"}]',
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
            '__RequestVerificationToken': 'lBfMrxn52pklQddl7nsYqu5m'
        }
        with open('./CryptoJS.js', 'r', encoding='utf8') as f:
            jsCode = f.read()

        with open('./EncodePassword.js', 'r', encoding='utf8') as f:
            jsCode1 = f.read()

        self.__JSRunEnvironment = execjs.compile(jsCode)

        self.__JSLoginEnv = execjs.compile(jsCode1)

        self.__url = 'https://wenshu.court.gov.cn/website/parse/rest.q4w'

        self.__wenshuList = []

        self.__totalPageNum = 1

    def logIn(self):
        authorizeHeaders = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'wenshu.court.gov.cn',
            'Origin': 'https://wenshu.court.gov.cn',
            'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?open=login',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        session = requests.session()
        authorizeResponse = session.post('https://wenshu.court.gov.cn/tongyiLogin/authorize', headers = authorizeHeaders)
        authorText = authorizeResponse.text

        print(authorText)

        getBase64_header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Connection': 'keep-alive',
            #'Cookie': 'HOLDONKEY=MTRiNjA1YTQtY2MzYS00M2Y0LWEyYjQtYmRkYjhkNWQzYmMy; UM_distinctid=179468720061-0b7477abd9de96-c3f3568-144000-17946872007790; CNZZDATA1278108394=619915756-1620385519-https%253A%252F%252Fwenshu.court.gov.cn%252F%7C1620385519',
            'Host': 'account.court.gov.cn',
            'Referer': 'https://account.court.gov.cn/app',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        getBase64_url = 'https://account.court.gov.cn/captcha/getBase64?appDomain=wenshu.court.gov.cn'
        getBase64_params = {'appDomain': 'wenshu.court.gov.cn'}
        getBase64_response = session.get(getBase64_url, headers = getBase64_header, params = getBase64_params)

        psw = 'Cai123456'
        self.__encodePassword = self.__JSLoginEnv.call('encodePassword', psw)
        logIn_headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Connection': 'keep-alive',
            #'Content-Length': '452',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #'Cookie': 'UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; ncCookie=DQS_rjTJPXb3B8HXj7nSl02R7kjh3oUG5VK0Fu6Od7LhzoC5o1w2iyi2kTxouM3P8lu0e2Z8tOVtDv0CgSEhZzzYj1t120ZO3OAjQcDDoTJV2bnFwXFOcvcPt51qqcfo; HOLDONKEY=YzYwNGEyYzItYTNjYS00YjRiLTllZTEtMjA0OTNhNGViNmY3; CNZZDATA1278108394=626397521-1617503530-https%253A%252F%252Fwenshu.court.gov.cn%252F%7C1620374678',
            'Host': 'account.court.gov.cn',
            'Origin': 'https://account.court.gov.cn',
            #'Referer': 'https://account.court.gov.cn/app?back_url=https%3A%2F%2Faccount.court.gov.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dzgcpwsw%26redirect_uri%3Dhttps%253A%252F%252Fwenshu.court.gov.cn%252FCallBackController%252FauthorizeCallBack%26state%3D42c9fff4-e90d-47ae-966b-b34bf47da79a%26timestamp%3D1620378923403%26signature%3D0EC746AB97256336792577D3A58B4C6DE5590631CEB0F3CD7C9EB4AB45209C8B%26scope%3Duserinfo',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        logInUrl = 'https://account.court.gov.cn/api/login'
        logInData = {
            'username': '18801353952',
            'password': self.__encodePassword,
            'appDomain': 'wenshu.court.gov.cn'
        }


        response = session.post(url=logInUrl, headers = logIn_headers, data=logInData)
        print(response.text)
        responseDict = json.loads(response.text)
        assert responseDict['message'] == '操作成功'

        cookieDict = requests.utils.dict_from_cookiejar(session.cookies)
        newCookie = self.__cookie[ : self.__cookie.find('SESSION=')]
        newCookie += 'SESSION=' + cookieDict['SESSION']

        self.__cookie = newCookie
        self.__wenshu_headers['Cookie'] = self.__cookie
        self.__htmlFetcher.setCookie(self.__cookie)


    def __dealItems(self, jsonData):
        resultList = jsonData['queryResult']['resultList']
        for item in resultList:
            wenshuItem = WenshuItemDetails(item, self.__htmlFetcher, self.__JSRunEnvironment)
            self.__wenshuList.append(wenshuItem)

    def getWenshu(self, currentPage = 1, wenshuType = 1):
        '''
        :param currentPage: 当前页面
        :param wenshuType:  文书类型
                    1、刑事案件文书
        :return:
        '''
        if currentPage == 1:
            self.__data['s8'] = '02'
            self.__data['queryCondition'] = '[{"key":"s8","value":"02"}]'
            self.__data['__RequestVerificationToken'] = self.__JSRunEnvironment.call('random', 24)
            self.__data['ciphertext'] = self.__JSRunEnvironment.call('getCipher')

        self.__data['pageNum'] = str(currentPage)

        data = json.loads(
            self.__htmlFetcher.get_html(self.__url, 1, useProxy=False, data=self.__data)
        )
        try:
            key = data["secretKey"]
            result = data["result"]
            realContent = self.__JSRunEnvironment.call('Decipher', result, key)
            realContentJson = json.loads(realContent)
        except:
            print('Cookie需要更新')

        if currentPage == 1:
            itemsNum = realContentJson['queryResult']['resultCount']
            self.__totalPageNum = 600 if itemsNum >= 600 else itemsNum

        self.__dealItems(realContentJson)

        if currentPage == self.__totalPageNum:
            return
        else:
            self.getWenshu(currentPage=currentPage + 1, wenshuType = wenshuType)

if __name__ == '__main__':
    wenshuSpider = WenshuSpider()
    wenshuSpider.logIn()
    wenshuSpider.getWenshu()