from Demo1.HTML_Fetcher import *
import re
from Demo1.Chaojiying import *
from Demo1.ZXGKSpider.verificationSettings import *

class ZXGKVerifier:
    def __init__(self):
        self.__getVerifyPngHeader = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
            'Cache-Control': 'max-age=0',
            # 'Cookie': 'JSESSIONID=F37C50DD075A0F2232A98835A717F368; UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; _gscu_15322769=18972572ixmhz018; SESSION=34c45484-c189-4106-838b-0f33868995fd; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1618976614,1619357881,1619358020,1619537171; _gscbrs_15322769=1; _gscs_15322769=19537218g5dt2867|pv:15; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619538402',
            'Host': 'zxgk.court.gov.cn',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://zxgk.court.gov.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }

        self.__html_fetcher = HTML_Fetcher(name='执行信息公开网验证码', headers=self.__getVerifyPngHeader)

        self.__chaoJiYing = Chaojiying_Client(username=CJY_USERNAME,
                                              password=CJY_PASSWORD,
                                              soft_id=CJY_SOFT_ID)

    def __getVerifyPng(self, type = 1, useProxy = False):
        '''
        获取验证码
        :param type: type为1时，代表被执行人查询，type为2时，代表司法拍卖查询
        :return: None
        '''

        self.__verifierUrl = 'http://zxgk.court.gov.cn/zhzxgk/' if type == 1 \
            else 'http://zxgk.court.gov.cn/sfpm/'

        txt = self.__html_fetcher.get_html(self.__verifierUrl, count = 1, useProxy = useProxy)

        pattern = 'captcha.do\?(.*?)"' if type == 1 else 'captchaSfpm.do\?(.*?)"'

        reSearchGroup = re.search(pattern, txt, re.S)
        #print(reSearchGroup[1])

        verifyCodeUrl = self.__verifierUrl + reSearchGroup[0]
        capchaInfo = reSearchGroup[1]
        self.__capchaId = capchaInfo[10 : capchaInfo.find('&')]
        self.__randomNum = capchaInfo[capchaInfo.find('random') + 7 : ]

        png = self.__html_fetcher.get_html(verifyCodeUrl,
                                           count=1,
                                           useProxy=False,
                                           returnType='content')
        # with open('5.png', 'wb') as f:
        #     f.write(png)
        return png

    def getVerifyInfo(self, type = 1, useProxy = False):
        png = self.__getVerifyPng(type = type, useProxy = useProxy)
        response = self.__chaoJiYing.PostPic(png, IMG_TYPE_GETVALUE)
        verifyValue = response['pic_str']
        return self.__capchaId, self.__randomNum, verifyValue

#if __name__ == '__main__':
#    verifier = ZXGKVerifier()
#    ret = verifier.getVerifyInfo(type=2)
#    print(type(ret))
#    print(ret)
