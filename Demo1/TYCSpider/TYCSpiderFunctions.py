from Demo1.HTML_Fetcher import *
from Demo1.config import *
from Demo1.TYCSpider.industry_info_list import *
from bs4 import BeautifulSoup
from Demo1.MySQL_EXEC_TYC.Functions import *
from Demo1.TYCSpider.Verification.Verifier import *

"""
    天眼查爬虫方法类
"""
class TYCSpiderFunctions():
    __antiRobot_retries = 3     #被反爬虫挡住的最大重试次数

    def __init__(self, html_fetcher):
        self.__html_fetcher = html_fetcher

    """
        @brief：处理返回的网页没有目标数据的情况
        @details: 处理方式：
                    1、更换代理
                    2、验证码
                    3、更新Cookie
    """
    def __noContentHandler(self, htmlText, url, useProxy):
        if useProxy:
            self.__html_fetcher.refresh_proxy()
        if '天眼查校验' in htmlText:
            tycVerifier.verify(url)

    """
        @brief: 爬取 行业 -> 省份/直辖市 -> 市 链接
    """
    def get_page_city(self, province_href, useProxy = True):
        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc)

        html = self.__html_fetcher.get_html(url = province_href,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_="scope-box")
        if div is None:
            print("此页查找不到市区内容 scope-box：", province_href, "考虑代理失效导致网页返回初始界面")
            self.__noContentHandler(html, province_href, useProxy)

            return self.get_page_city(province_href, useProxy=useProxy)

        a_list = div.find_all('a')

        for city_a in a_list:
            city_href = city_a.get('href')
            print(city_href)
            insert_industry_province_city(city_href)
            # qu_list.append(qu_href)

    """
        @brief: 爬取 行业 -> 省份直辖市 -> 市 -> 区/县 链接
    """
    def get_page_qu(self, city_href, useProxy = False):
        self.__html_fetcher.setCookie(cookie=Cookie_init_tyc)

        html = self.__html_fetcher.get_html(url = city_href,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', class_="scope-box")

        if div is None:
            print("此页查找不到县区内容 scope：", city_href, "考虑被反爬虫拦截")
            self.__noContentHandler(html, city_href, useProxy)

            return self.get_page_qu(city_href, useProxy = useProxy)

        a_list = div.find_all('a')

        for city_a in a_list:
            qu_href = city_a.get('href')
            print("县区:", qu_href)
            insert_industry_province_city_qu(qu_href)
            # qu_list.append(qu_href)

    """
        @brief: 爬取具体到某一个 区/县 下， 所有分页的链接
    """
    def get_all_pages(self, qu_href, count, useProxy = False):
        if count > self.__antiRobot_retries:
            print('本页面爬取失败：', qu_href)
            return

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc)

        html = self.__html_fetcher.get_html(url = qu_href,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')

        div = soup.find('div', class_="search-pager")

        company_list_div = soup.find('div', class_="result-list sv-search-container")

        no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
        # 此条件下确实没有分页信息或者公司
        if no_company_div is not None:
            return

        # 如果没有上面的条件，说明被反爬挡住了
        if company_list_div is None:
            print("此页查找不到分页 ：", qu_href, "考虑被反爬虫拦截")
            self.__noContentHandler(html, qu_href, useProxy)

            return self.get_all_pages(qu_href, count + 1, useProxy = useProxy)

        # 如果公司列表的不为空，而分页为空，说明只有这一页
        if div is None:
            insert_industry_province_city_qu_page(qu_href)
            return

        a_list = div.find_all('a')
        page_list = []
        page_num = len(a_list) - 1 #页数
        page_count = 0
        for page_a in a_list:
            if page_count > 4:  #后面的页数需要会员
                break
            page_count += 1
            if page_count > page_num: #少于5页，最后一个是下一页，不用加入
                break
            page_href = page_a.get('href')
            print("分页:", page_href)
            insert_industry_province_city_qu_page(page_href)
            # qu_list.append(qu_href)

    """
        @brief: 在一个具体的分页下，爬取所有公司的链接
    """
    def get_page_company(self, page_url, count, useProxy = False):
        if count > self.__antiRobot_retries:
            return

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc)
        html = self.__html_fetcher.get_html(url = page_url,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')
        # 页内公司href 链表
        company_href_list = []
        company_list_div = soup.find('div', class_="result-list sv-search-container")
        no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
        # 此条件下确实没有分页信息或者公司
        if no_company_div is not None:
            return
        # 如果没有上面的条件，说明被反爬挡住了
        if company_list_div is None:
            print("此页查找不到公司列表：", page_url, "考虑被反爬虫阻挡")
            self.__noContentHandler(html, page_url, useProxy)
            return self.get_page_company(page_url, count + 1, useProxy = useProxy)

        a_list = company_list_div.find_all('a')

        if a_list is not None:
            for item in a_list:
                if 'https://www.tianyancha.com/company/' in str(item.get("href")):
                    if len(str(item.get("href"))) > 36:
                        company_href = str(item.get("href"))
                        print('\t公司链接：', company_href)
                        insert_company(company_href)
                        company_href_list.append(company_href)
        print("此页一共爬取公司数: ", len(company_href_list))

    """
        @brief 获取企业详细信息
    """
    def get_info(self, url, count, useProxy = False):
        if count > self.__antiRobot_retries:
            print("重试超过%d次：建议停机检查：" % self.__antiRobot_retries, url)
            return

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc)

        html = self.__html_fetcher.get_html(url = url,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')
        self.__get_info_logoImg(soup, url = url)

    """
        @brief 进入企业信息页，获取LOGO Img
        此项非必须爬取到，因为有些公司没有logo
    """
    def __get_info_logoImg(self, soup, url):
        # 企业logo
        logdiv = soup.find('div', class_="logo -w100")
        imgsrc = ""
        if logdiv is not None:
            img = logdiv.find('img', class_="img")
            if img is not None:
                imgsrc = img.get('data-src')
                with open('233.png', 'w') as f:
                    f.write(imgsrc)
        else:
            print("此页查找不到公司logo[@class='logo -w100']：", url)
            return False

    """
        @brief: 进入企业信息页，获取企业简介
    """
    def __get_info_Brief(self, soup, url):
        pass

    """
        @brief: 进入企业信息页，获取企业证券信息
    """
    def __get_info_Securities(self, soup, url):
        pass

    """
        @brief: 进入企业信息页，获取企业联系信息
    """
    def __get_info_Connection(self, soup, url):
        pass

    """
        @brief: 进入企业信息页，获取企业详细信息
    """
    def __get_info_Details(self, soup, url):
        pass

