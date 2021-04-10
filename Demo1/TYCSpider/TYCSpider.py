from Demo1.TYCSpider.TYCSpiderFunctions import *

class TYCSpider():

    def __init__(self):
        self.__htmlFetcher = HTML_Fetcher(name='天眼查', headers=headers_tyc)
        self.__functions = TYCSpiderFunctions(self.__htmlFetcher)

    def main_all(self):
        self.__get_city_to_mysql()

    """
    @brief: 在数据库中构造爬取链接 
            爬取 行业 + 省份直辖市 -> 市 所有的链接 存到mysql
    """
    def __get_city_to_mysql(self):
        for industry_href in industry_href_list:
            for province_str in province_list:
                # 行业 -> 省份直辖市
                province_href = industry_href + province_str
                # 行业 -> 省份直辖市 -> 市
                self.__functions.get_page_city(province_href)

    """
    @brief: 在数据库中构造爬取链接 
            爬取 行业 -> 省份直辖市 -> 区 所有的链接 存到mysql
    """
    def __get_qu_to_mysql(self):
        pass

    """
    @brief: 在数据库中构造爬取链接 
            爬取 行业 -> 省份/直辖市 -> 市 ->区县 -> 所有分页 所有的链接 存到mysql
    """
    def __get_page_to_mysql(self):
        pass

    """
    @brief: 在数据库中构造爬取链接 
            爬取 行业 -> 省份直辖市 -> 市区 -> 所有分页 -> 公司下 所有的链接 存到mysql
    """
    def __get_company_to_mysql(self):
        pass

    """
    @brief: 在数据库中构造爬取链接 
            爬取 行业 -> 省份直辖市 -> 市区 -> 所有分页 -> 公司 -> 公司背景等信息 存到mysql
    """
    def __get_company_info_to_mysql(self):
        pass

if __name__ == '__main__':
    spider = TYCSpider()
    spider.main_all()
