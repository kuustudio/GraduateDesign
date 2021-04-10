from Demo1.HTML_Fetcher import *
from Demo1.config import *
from Demo1.TYCSpider.industry_info_list import *
from bs4 import BeautifulSoup
from Demo1.MySQL_EXEC_TYC.Functions import *

"""
    方法类
"""
class TYCSpiderFunctions():
    def __init__(self, html_fetcher):
        self.__html_fetcher = html_fetcher
        pass

    # 爬取 行业 -> 省份直辖市 -> 市 链接
    def get_page_city(self, province_href):
        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc)

        html = self.__html_fetcher.get_html(url = province_href,
                                            count = 1)
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_="scope-box")
        if div is None:
            print("此页查找不到市区内容 scope-box：", province_href, "考虑代理失效导致网页返回初始界面")
            self.__html_fetcher.refresh_proxy()
            return self.get_page_city(province_href)
        a_list = div.find_all('a')

        for city_a in a_list:
            city_href = city_a.get('href')
            print(city_href)
            insert_industry_province_city(city_href)
            # qu_list.append(qu_href)