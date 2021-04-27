from Demo1.config import *
from Demo1.HTML_Fetcher import *
import re
import math
from Demo1.WXSpider.WXPage import *

class WXSpider():
    __headers_wx = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'ABTEST=0|1619339786|v1; IPLOC=CN1100; SUID=A1E3EFDB1B0DA00A0000000060852A0A; SUID=A1E3EFDB7050A00A0000000060852A0A; weixinIndexVisited=1; SUV=00764FC2DBEFE3A160852A0BEDD5A820; SNUID=20626E5A818441467B1973008128FFED; JSESSIONID=aaae7fq_ewU7Nb4LmliKx; ppinf=5|1619340085|1620549685|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8Y3J0OjEwOjE2MTkzNDAwODV8cmVmbmljazoyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8dXNlcmlkOjQ0Om85dDJsdUtJNHhnT0RuMDliaktZNVROdklzLVlAd2VpeGluLnNvaHUuY29tfA; pprdig=t-SChwRRREAHIcj9ncEz4RfElCiM1xF4F-v8d2y69uGG7GbQYBCZV_c7mQ3nIzSjVeuLxrWPQUQVuA4rDHd5ffXedz4SzuppOBIxeb0soWhvGCvN0DwYrU00nDcSU3OlIs6EhI6uvtQNZnv9ANooZ6jTHq0Zb75Fv0XAd5QkeoA; ppinfo=0b475c99a9; passport=5|1619340085|1620549685|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8Y3J0OjEwOjE2MTkzNDAwODV8cmVmbmljazoyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8dXNlcmlkOjQ0Om85dDJsdUtJNHhnT0RuMDliaktZNVROdklzLVlAd2VpeGluLnNvaHUuY29tfA|e036adb998|t-SChwRRREAHIcj9ncEz4RfElCiM1xF4F-v8d2y69uGG7GbQYBCZV_c7mQ3nIzSjVeuLxrWPQUQVuA4rDHd5ffXedz4SzuppOBIxeb0soWhvGCvN0DwYrU00nDcSU3OlIs6EhI6uvtQNZnv9ANooZ6jTHq0Zb75Fv0XAd5QkeoA; sgid=05-50247413-AWCFKzUyXy93mfwy7b0oI4E; ppmdig=16193400850000001bcc89d8cf4cdf3966d0ae1f9bc9687c',
        'Host': 'weixin.sogou.com',
        'Referer': 'https://open.weixin.qq.com/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    def __init__(self):
        self.__htmlFetcher = HTML_Fetcher(name='微信公众号文章', headers=self.__headers_wx)
        self.__keyWord = ''

        self.__basicUrl = 'https://weixin.sogou.com/weixin'

        self.__params = {
            'query': '西兴发布',
            '_sug_type_':'',
            's_from': 'input',
            '_sug_': 'n',
            'type': '2',
            'page': '1',
            'ie': 'utf8'
        }
        self.__pages = []
        self.__dataframe = pd.DataFrame(columns=['标题', '简介', '公众号名', '文章内容'])
        self.__getAllPages()
        self.__dataframe.to_csv(str(self.__pageNum) + '.csv', encoding='utf-8-sig')

    def __getPage(self, pageNum = 1):
        self.__params['page'] = str(pageNum)

        html = self.__htmlFetcher.get_html(url = self.__basicUrl,
                                           count = 1,
                                           useProxy = False,
                                           data = self.__params)

        #print(html)
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_ = 'news-box')

        assert div is not None

        itemNum = div.find('div', class_ = 'mun')

        if pageNum == 1:
            num = ''
            for i in itemNum.text:
                if i >= '0' and i <= '9':
                    num += i

            self.__pageNum = math.ceil(int(num) / 10)
            print('一共：', self.__pageNum, '页')

        page = WXPage(html, pageNum, dataframe=self.__dataframe)
        self.__pages.append(page)

    def __getAllPages(self):
        self.__getPage(1)

        for i in range(2, 10):
            print('第', i, '页：')
            self.__getPage(i)



if __name__ == '__main__':
    wx = WXSpider()