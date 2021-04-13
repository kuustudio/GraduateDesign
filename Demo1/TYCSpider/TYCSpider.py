from Demo1.TYCSpider.TYCSpiderFunctions import *

class TYCSpider():

    def __init__(self):
        self.__htmlFetcher = HTML_Fetcher(name='天眼查', headers=headers_tyc)
        self.__functions = TYCSpiderFunctions(self.__htmlFetcher)

    """
    @brief: 启动全爬虫程序
    """
    def main_all(self):
        self.__get_company_info_to_mysql()

    """
    @brief:启动搜索关键词爬虫程序
    """
    def main_search(self, keyWord):
        search_href = 'https://www.tianyancha.com/search?key=' + keyWord
        print('搜索企业关键字：' + keyWord)
        pages = self.__functions.get_all_pages_search(search_href, 1)
        if pages is None or len(pages) == 0:
            print('没有对应关键字信息！')
            return
        self.__get_company_to_mysql(todo_pages = pages)
        self.__get_company_info_to_mysql(searchMode = True)


    """
    @brief: 在数据库中构造爬取链接 
            爬取: URL@[行业 + 省份直辖市] -> 市 所有的链接 存到mysql
    """
    def __get_city_to_mysql(self):
        for industry_href in industry_href_list:
            for province_str in province_list:
                # 行业 -> 省份直辖市
                province_href = industry_href + province_str
                # 行业 -> 省份直辖市 -> 市
                self.__functions.get_page_city(province_href, useProxy=False)

    """
    @brief: 在数据库中构造爬取链接 
            爬取 URL@[行业 + 省份直辖市 + 市] -> 区/县城 所有的链接 存到mysql
    """
    def __get_qu_to_mysql(self):
        todo_city_list = get_todo_industry_province_city()
        while len(todo_city_list) > 0:
            for todo_city_url in todo_city_list:
                print("开始爬取未爬的城市：", todo_city_url['href'])
                self.__functions.get_page_qu(todo_city_url['href'])
                do_industry_province_city(todo_city_url['href'])
            todo_city_list = get_todo_industry_province_city()

    """
    @brief: 在数据库中构造爬取链接 
            爬取 URL@[行业 + 省份/直辖市 + 市 + 区/县] -> 所有分页 所有的链接 存到mysql
    """
    def __get_all_pages_to_mysql(self):
        todo_url_list = get_todo_industry_province_city_qu()
        while len(todo_url_list) > 0:
            for todo_url in todo_url_list:
                print("开始爬取未爬的区县：", todo_url['href'])
                self.__functions.get_all_pages(todo_url['href'], 1)
                do_industry_province_city_qu(todo_url['href'])
            todo_url_list = get_todo_industry_province_city_qu()

    """
    @brief: 在数据库中构造爬取链接 
            爬取 URL@[行业 + 省份直辖市 + 市区 + 所有分页] -> 具体公司 所有的链接 存到mysql
    """
    def __get_company_to_mysql(self, todo_pages = None):
        if todo_pages is None:
            todo_page_list = get_todo_industry_province_city_qu_page()
        else:
            todo_page_list = todo_pages

        while len(todo_page_list) > 0:
            for todo_url in todo_page_list:
                print("开始爬取未爬的分页：", todo_url['href'])
                self.__functions.get_page_company(page_url = todo_url['href'],
                                                  count = 1,
                                                  mode = 1 if todo_pages is None else 2)
                if todo_pages is None:
                    do_industry_province_city_qu_page(todo_url['href'])
                else:
                    del todo_page_list[todo_page_list.index(todo_url)]

            if todo_pages is None:
                todo_page_list = get_todo_industry_province_city_qu_page()

    """
    @brief: 在数据库中构造爬取链接 
            根据已经存储完毕的公司URL， 爬取所有公司背景等信息 存到mysql
    @hasTested: YES
    """
    def __get_company_info_to_mysql(self, searchMode = False):
        todo_company_list = get_todo_company_limit(searchMode)
        while len(todo_company_list) > 0:
            for todo_url in todo_company_list:
                print('=====================================================================')
                print("开始爬取未爬的公司：", todo_url['id'])
                self.__functions.get_info(todo_url['id'], 1, searchMode = searchMode)
                finish_company(todo_url['id'], searchMode)
            todo_company_list = get_todo_company_limit(searchMode)

if __name__ == '__main__':
    spider = TYCSpider()
    # spider.main_search('腾讯')
    spider.main_all()
