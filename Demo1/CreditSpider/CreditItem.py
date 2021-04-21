from Demo1.config import *
from Demo1.HTML_Fetcher import HTML_Fetcher
from Demo1.CreditSpider.AdministrativeLicensing import *
import json

class CreditItem():

    def __init__(self, itemInfo):
        # print(itemInfo)
        self.__info = itemInfo
        self.__basicUrl = 'https://public.creditchina.gov.cn/private-api/typeSourceSearch'
        self.__params = {
            'source': '',
            'type': '行政许可',
            'searchState': '1',
            'entityType': self.__info['entityType'],
            'scenes': 'defaultscenario',
            'keyword': self.__info['accurate_entity_name'],
            'page': '1',
            'pageSize': '10'
        }
        self.__htmlFetcher = HTML_Fetcher(name='信用中国公司条目', headers=headers_credit)

        self.__adminLicenses = []
        self.__adminSanctions = []
        self.__trustworthyIncentives = []
        self.__punishments = []
        self.__focuses = []
        self.__qualifications = []
        self.__risks = []
        self.__elseCreditInfos = []

        self.__getXZXK()

    """
        分析行政许可
    """
    def __getXZXK(self, pageNum = 1):
        self.__params['type'] = '行政许可'
        self.__params['page'] = str(pageNum)

        adminLicenseHtml = self.__htmlFetcher.get_html(self.__basicUrl, 1, useProxy=False, data=self.__params)

        json1 = json.loads(adminLicenseHtml)
        assert json1['message'] == '成功'
        data = json1['data']
        adminLicenses = data['list']

        for adminLincenseInfo in adminLicenses:
            self.__adminLicenses.append(AdminLicense(adminLincenseInfo))

        count = data['total']
        if count > 10:
            wholePageNum = data['totalSize']
            if pageNum == wholePageNum:
                return
            else:
                assert pageNum < wholePageNum
                self.__getXZXK(pageNum = pageNum + 1)
        else:
            return

    """
        分析行政处罚
    """
    def __getXZCF(self, pageNum = 1):
        self.__params['type'] = '行政处罚'
        self.__params['page'] = str(pageNum)

    """
        分析守信激励
    """
    def __getSXJL(self, pageNum = 1):
        self.__params['type'] = '守信激励'
        self.__params['page'] = str(pageNum)

    """
        分析失信惩戒
    """
    def __getSXCJ(self, pageNum = 1):
        self.__params['type'] = '失信惩戒'
        self.__params['page'] = str(pageNum)

    """
        分析重点关注
    """
    def __getZDGZ(self, pageNum = 1):
        self.__params['type'] = '重点关注'
        self.__params['page'] = str(pageNum)

    """
        分析资质资格
    """
    def __getZiZhi(self, pageNum = 1):
        self.__params['type'] = '资质资格'
        self.__params['page'] = str(pageNum)

    """
        分析风险提示
    """
    def __getFXTS(self, pageNum = 1):
        self.__params['type'] = '风险提示'
        self.__params['page'] = str(pageNum)

    """
        分析其他
    """
    def __getElse(self, pageNum = 1):
        self.__params['type'] = '其他'
        self.__params['page'] = str(pageNum)










