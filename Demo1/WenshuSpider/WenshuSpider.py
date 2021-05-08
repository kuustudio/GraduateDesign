from Demo1.HTML_Fetcher import *
from Demo1.config import *
import execjs
import json
from Demo1.WenshuSpider.WenshuItemDetails import *
from selenium import webdriver
import time
from Demo1.WenshuSpider.SearchList import *

class WenshuSpider():
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

        self.__cookie = ''

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

        self.__queryCondition = [{"key":"s8","value":"02"}]

        self.__data = {
            #'pageId': 'c2c0bdb832a4221d3548cdc366f9812b',
            's8': '02',
            'sortFields': 's50:desc',
            'ciphertext': '1010111 1001101 1111000 1000100 1100111 1100010 1000110 110111 1111010 1100111 1101000 1100101 1000010 1010010 1110100 1110010 1100111 1101001 1100101 1110100 1000100 1001011 1010000 1001111 110010 110000 110010 110001 110000 110101 110000 110110 1001100 101011 1111000 1001111 1001100 1000011 111000 1111001 1100101 1010110 1110011 1010011 1001101 1100100 110101 1110110 1000011 110110 1110110 1001100 1010110 1000001 111101 111101',
            'pageNum': '1',
            'queryCondition': str(self.__queryCondition),
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

        self.__hasLogIn = False

    def __refreshCookie(self, newCookie):
        self.__cookie = newCookie
        self.__wenshu_headers['Cookie'] = newCookie
        self.__htmlFetcher.setCookie(newCookie)

    def __logIn_noWebdriver(self):
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

        self.__encodePassword = self.__JSLoginEnv.call('encodePassword', self.__password)
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
            'username': self.__username,
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

    def __logIn_Webdriver(self):
        browser = webdriver.Chrome()
        iframe_url = 'https://account.court.gov.cn/app?back_url=https%3A%2F%2Faccount.court.gov.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dzgcpwsw%26redirect_uri%3Dhttps%253A%252F%252Fwenshu.court.gov.cn%252FCallBackController%252FauthorizeCallBack%26state%3D1b1b7539-4023-47ec-bba7-defe7d38c2ae%26timestamp%3D1620445772894%26signature%3D83913547A97CFC0D1FD949B6141B1E94F8C97469D4508DDCD5E3C1678415BD7E%26scope%3Duserinfo#/login'
        browser.get(iframe_url)
        while True:
            try:
                username = browser.find_element_by_xpath('//*[@id="root"]/div/form/div[1]/div[1]/div/div/div/input')
                psw = browser.find_element_by_xpath('//*[@id="root"]/div/form/div[1]/div[2]/div/div/div/input')
                break
            except:
                time.sleep(0.5)

        username.send_keys(self.__username)
        psw.send_keys(self.__password)


        button = browser.find_element_by_xpath('//*[@id="root"]/div/form/div/div[3]/span')
        button.click()

        while 'https://wenshu.court.gov.cn/' not in browser.current_url:
            time.sleep(0.5)

        login = browser.find_element_by_xpath('//*[@id="loginLi"]/a')
        login.click()

        time.sleep(0.5)
        print(browser.get_cookies())
        cookieSetter_new = CookieSetter(browser.get_cookies())
        self.__refreshCookie(cookieSetter_new.strCookie)
        print('Cookie更新为：', self.__cookie)
        browser.close()

    def __dealItems(self, jsonData):
        resultList = jsonData['queryResult']['resultList']
        for item in resultList:
            wenshuItem = WenshuItemDetails(item, self.__htmlFetcher, self.__JSRunEnvironment)
            self.__wenshuList.append(wenshuItem)

    def __setWenshuType(self, wenshuType = '民事案件'):
        self.__queryCondition = []
        typeCode = dict_type[wenshuType]["value"]

        self.__data['s8'] = typeCode

        self.__queryCondition.append(dict_type[wenshuType])

    def __setCourtLevel(self, courtLevel = '高级法院'):
        self.__queryCondition.append(dict_court[courtLevel])

    def __setYear(self, year = 2021):
        assert 2000 <= year <= 2021
        dict_year = {"key" : key_year, "value" : str(year)}
        self.__queryCondition.append(dict_year)

    def __setArea(self, area):
        for dict in list_area:
            if dict['value'] == area:
                self.__queryCondition.append(dict)
                break

    def findWholeWenshu(self):
        for type in dict_type.keys():
            self.__setWenshuType(type)
            for court in dict_court.keys():
                self.__setCourtLevel(courtLevel=court)
                for year in range(2000, 2022):
                    self.__setYear(year)
                    if court == '最高法院':
                        print(self.__queryCondition)
                        self.__getWenshu()
                    else:
                        for area in list_area:
                            self.__setArea(area["value"])
                            print(self.__queryCondition)
                            self.__getWenshu()
                            del self.__queryCondition[-1]
                    del self.__queryCondition[-1]
                del self.__queryCondition[-1]
            del self.__queryCondition[-1]


    def __getWenshu(self, currentPage = 1):
        '''
        :param currentPage: 当前页面
        :return:
        '''
        if not self.__hasLogIn:
            self.__logIn_Webdriver()
            self.__hasLogIn = True

        if currentPage == 1:
            self.__data['queryCondition'] = str(self.__queryCondition)

        if currentPage == 1 or (not self.__hasLogIn):
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
            assert data['success'] == False
            print('获取一级文书页面出现问题，Cookie需要更新')
            self.__hasLogIn = False
            self.__getWenshu(currentPage=currentPage)
            return

        if currentPage == 1:
            itemsNum = realContentJson['queryResult']['resultCount']
            if itemsNum == 0:
                print('本条件下没有文书！结束本次搜索')
                return
            self.__totalPageNum = 600 if itemsNum >= 600 else itemsNum
            print('总文书数量：', str(self.__totalPageNum))

        self.__dealItems(realContentJson)

        if currentPage == self.__totalPageNum:
            return
        else:
            self.__getWenshu(currentPage=currentPage + 1)

if __name__ == '__main__':
    wenshuSpider = WenshuSpider('18801353952', 'Cai123456')
    wenshuSpider.findWholeWenshu()