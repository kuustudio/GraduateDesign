from Demo1.WenshuSpider.SQL_EXEC.MySQL_EXEC_Wenshu import *
from Demo1.HTML_Fetcher import *
import json
from Demo1.WenshuSpider.SearchList import *

class WenshuItemDetails():
    def __init__(self, basicInfoDict, htmlFetcher, JSRunEnv, queryCondition):
        self.__name = basicInfoDict['1']
        self.__court = basicInfoDict['2']
        self.__number = basicInfoDict['7']
        self.__id = basicInfoDict['rowkey']
        self.__date = basicInfoDict['31']

        self.__area = ''

        self.__htmlFetcher = htmlFetcher
        self.__JSRunEnvironment = JSRunEnv
        for dict in queryCondition:
            if dict['key'] == 's8':
                for (wenshuType, value) in dict_type.items():
                    if value == dict:
                        self.__type = wenshuType
                        break
            elif dict['key'] == 's42':
                self.__year = dict['value']
            elif dict['key'] == 's33':
                self.__area = dict['value']

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
            try:
                self.__detailName = realContentJson['s22']
            except:
                self.__detailName = ''

            try:
                self.__detail = realContentJson['s51'] + realContentJson['s28']
            except:
                self.__detail = realContentJson['s23'] if 's23' in realContentJson.keys() else ''
                self.__detail += realContentJson['s26'] if 's26' in realContentJson.keys() else ''
                self.__detail += realContentJson['s27'] if 's27' in realContentJson.keys() else ''
                self.__detail += realContentJson['s28'] if 's28' in realContentJson.keys() else ''
            self.__judgeAccording = ''
            try:
                according = realContentJson['s47']

                for judgeAccordingItem in according:
                    self.__judgeAccording += (judgeAccordingItem['fgmc'] + judgeAccordingItem['tkx'] + ';')
            except:
                self.__judgeAccording = ''
            try:
                self.__crime = str(realContentJson['s11'])
            except:
                self.__crime = ''

            self.__save()
        except:
            print('获取详细信息出现问题')

    def __save(self):
        data = (self.__name,
                self.__type,
                self.__court,
                self.__year,
                self.__area,
                self.__number,
                self.__id,
                self.__date,
                self.__publicizeDate,
                self.__detailName,
                self.__detail,
                self.__judgeAccording,
                self.__crime)

        insertItem(data=data)