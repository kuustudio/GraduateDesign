import execjs
from Demo1.HTML_Fetcher import *
import json

class WenshuItemDetails():
    def __init__(self, basicInfoDict, htmlFetcher, JSRunEnv):
        self.__name = basicInfoDict['1']
        self.__court = basicInfoDict['2']
        self.__number = basicInfoDict['7']
        self.__id = basicInfoDict['rowkey']
        self.__date = basicInfoDict['31']

        self.__htmlFetcher = htmlFetcher
        self.__JSRunEnvironment = JSRunEnv

        self.__getDetail()


    def __getDetail(self):
        self.__url = 'https://wenshu.court.gov.cn/website/parse/rest.q4w'
        self.__data = {
            'docId': self.__id,
            'ciphertext': self.__JSRunEnvironment.call('getCipher'),
            'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@docInfoSearch',
            '__RequestVerificationToken': self.__JSRunEnvironment.call('random', 24)
        }

        data = json.loads(
            self.__htmlFetcher.get_html(self.__url, 1, useProxy=True, data=self.__data, printInfo=False)
        )
        try:
            key = data["secretKey"]
            result = data["result"]

            realContent = self.__JSRunEnvironment.call('Decipher', result, key)
            realContentJson = json.loads(realContent)
            print(realContentJson)
        except:
            print('获取文书详细信息出现问题，Cookie需要更新')
            raise SyntaxError

        try:
            self.__publicizeDate = realContentJson['s41']
            self.__detailName = realContentJson['s22']
            try:
                self.__detail = realContentJson['s51'] + realContentJson['s28']
            except:
                self.__detail = realContentJson['s23'] if 's23' in realContentJson.keys() else ''
                self.__detail += realContentJson['s26'] if 's26' in realContentJson.keys() else ''
                self.__detail += realContentJson['s27'] if 's27' in realContentJson.keys() else ''
                self.__detail += realContentJson['s28'] if 's28' in realContentJson.keys() else ''
            self.__judgeAccording = ''

            according = realContentJson['s47']

            for judgeAccordingItem in according:
                self.__judgeAccording += (judgeAccordingItem['fgmc'] + judgeAccordingItem['tkx'] + ';')

            self.__crime = str(realContentJson['s11'])
        except:
            print('获取详细信息出现问题')