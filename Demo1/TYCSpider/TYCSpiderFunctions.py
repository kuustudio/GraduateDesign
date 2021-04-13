from Demo1.HTML_Fetcher import *
from Demo1.config import *
from Demo1.TYCSpider.industry_info_list import *
from bs4 import BeautifulSoup
from Demo1.MySQL_EXEC_TYC.Functions import *
from Demo1.TYCSpider.Verification.Verifier import *
import math

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
        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc[0])

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
        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc[0])

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

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc[0])

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
        @brief: 搜索页面下，爬取所有分页的链接
    """
    def get_all_pages_search(self, search_href, count, useProxy = False):
        if count > self.__antiRobot_retries:
            print('本页面爬取失败：', search_href)
            return []

        allPagesSearch = []

        self.__html_fetcher.setCookie(cookie=Cookie_init_tyc[0])

        html = self.__html_fetcher.get_html(url=search_href,
                                            count=1,
                                            useProxy=useProxy)

        soup = BeautifulSoup(html, 'html.parser')

        div = soup.find('div', class_="search-pager")

        company_list_div = soup.find('div', class_="result-list sv-search-container")

        no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
        # 此条件下确实没有分页信息或者公司
        if no_company_div is not None:
            return []

        # 如果没有上面的条件，说明被反爬挡住了
        if company_list_div is None:
            print("此页查找不到分页 ：", search_href, "考虑被反爬虫拦截")
            self.__noContentHandler(html, search_href, useProxy)

            return self.get_all_pages(search_href, count + 1, useProxy=useProxy)

        # 如果公司列表的不为空，而分页为空，说明只有这一页
        if div is None:
            allPagesSearch.append({'href' : search_href})
            return allPagesSearch

        a_list = div.find_all('a')
        page_list = []
        page_num = len(a_list) - 1  # 页数
        page_count = 0
        for page_a in a_list:
            if page_count > 4:  # 后面的页数需要会员
                break
            page_count += 1
            if page_count > page_num:  # 少于5页，最后一个是下一页，不用加入
                break
            page_href = page_a.get('href')
            print("分页:", page_href)
            allPagesSearch.append({'href' : page_href})
            # qu_list.append(search_href)
        return allPagesSearch

    """
        @brief: 在一个具体的分页下，爬取所有公司的链接
        @:param [mode = 1] 全爬虫模式，公司url插入t_company
                [mode = 2] 搜索模式，公司url插入t_company_search
    """
    def get_page_company(self, page_url, count, useProxy = False, mode = 1):
        if count > self.__antiRobot_retries:
            return

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc[0])
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
            return self.get_page_company(page_url, count + 1, useProxy = useProxy, mode = mode)

        a_list = company_list_div.find_all('a')

        if a_list is not None:
            for item in a_list:
                if 'https://www.tianyancha.com/company/' in str(item.get("href")):
                    if len(str(item.get("href"))) > 36:
                        company_href = str(item.get("href"))
                        print('\t公司链接：', company_href)
                        if mode == 1:
                            insert_company(company_href)
                        else:
                            insert_search_company(company_href,
                                                  keyWord = page_url[page_url.find('=') + 1 : len(page_url)])
                        company_href_list.append(company_href)
        print("此页一共爬取公司数: ", len(company_href_list))

    """
        @brief 获取企业详细信息
    """
    def get_info(self, url, count, useProxy = False, searchMode = False):
        if count > self.__antiRobot_retries:
            print("重试超过%d次：建议停机检查：" % self.__antiRobot_retries, url)
            return

        self.__html_fetcher.setCookie(cookie = Cookie_init_tyc[0])

        html = self.__html_fetcher.get_html(url = url,
                                            count = 1,
                                            useProxy = useProxy)

        soup = BeautifulSoup(html, 'html.parser')

        if not self.__get_info_Details(soup, url, searchMode):
            self.__noContentHandler(html, url, useProxy)
            return self.get_info(url, count + 1, useProxy, searchMode)

        self.__get_info_logoImg(soup, url = url, searchMode = searchMode)

        self.__get_info_Connection(soup, url = url, searchMode = searchMode)

        self.__get_info_Manager(soup, url, searchMode = searchMode)


    """
        @brief 进入企业信息页，获取LOGO Img
        此项非必须爬取到，因为有些公司没有logo
        @ setData : img 图片source url
    """
    def __get_info_logoImg(self, soup, url, searchMode = False):
        # 企业logo
        logdiv = soup.find('div', class_="logo -w100")
        if logdiv is not None:
            img = logdiv.find('img', class_="img")
            if img is not None:
                imgsrc = img.get('data-src')
                #img_html = self.__html_fetcher.get_html(
                #    imgsrc, count = 1, useProxy = False)
                #可以考虑存图片
                data = (imgsrc, url)
                update_company_imgSource(data, searchMode)
                print('\t4、图片source：', imgsrc)
                return True
        else:
            print("\t此页查找不到公司logo[@class='logo -w100']：", url)
            return False

    """
        @brief: 进入企业信息页，获取企业人员信息
    """
    def __get_info_Manager(self, soup, url, searchMode = False):
        manager = soup.find('div', id = '_container_staffCount')
        if manager is None:
            print('\t无企业人员信息', url)
            return False
        else:
            tds = manager.find_all('td')
            names = [] #管理人名称
            posts = [] #管理人职位
            chigu = [] #管理人持股
            shouyigu = [] #管理人收益股
            count = len(tds) / 8
            # assert count - count.__round__() == 0.0
            count = math.floor(count)
            for i in range(0, count):
                names.append(tds[i * 8 + 3].text)
                posts.append(tds[i * 8 + 5].text)
                chigu.append(tds[i * 8 + 6].text)
                shouyigu.append(tds[i * 8 + 7].text)
            dsz = '-'
            zjl = '-'
            zysyr = names[0]
            dm = '-'
            glryrs = str(count)

            for i in range(0, count):
                if '董事长' in posts[i]:
                    dsz = names[i]
                elif '总经理' in posts[i]:
                    zjl = names[i]

            data = (dsz, dm, zjl, glryrs, url)
            print('\t6、企业管理人员信息：', data)
            update_company_manage(data, searchMode)
            return True

    """
        @brief: 进入企业信息页，获取企业证券信息
        @completed? : No
    """
    def __get_info_Securities(self, soup, url):
        pass

    """
        @brief: 进入企业信息页，获取企业联系信息
        @setData: lxdh, dzyx, cz, gswz, qy, yzbm, bgdz, zcdz
                联系电话，电子邮箱，传真，公司网址，区域，邮政编码，办公地址，注册地址
    """
    def __get_info_Connection(self, soup, url, searchMode = False):
        div = soup.find('div', class_='box -company-box')

        if div is None or len(div) is 0:
            print("\t此页查找不到企业联系信息[@class='box -company-box']:", url)
            return False
        else:
            detail = div.find('div', class_='detail')
            if detail is None or len(detail) is 0:
                print("\t此页查找不到企业联系信息 [@class='details']：", url)
                return False
            else:
                try:
                    lianxi = detail.find('div', class_='in-block sup-ie-company-header-child-1')
                    lxdh = detail.find('span', class_='').text  # 联系电话

                    if len(detail.find_all('span')) <= 15:
                        print("\t估计界面有问题：len(span) <= 15  ", url)
                        return False
                    try:
                        dzyx = detail.find('div',
                            class_='in-block sup-ie-company-header-child-2').find('span',
                            class_='email').text  # 电子邮箱
                    except:
                        dzyx = ''
                        print('\t\t公司', url, '没有电子邮箱')

                    cz = "-"  # 传真
                    try:
                        gswz = detail.find(
                            'div',
                            class_='f0 clearfix mb0').find(
                            'div',
                            class_='in-block sup-ie-company-header-child-1').find(
                            'a',
                            class_='company-link').get('href')  # 公司网址
                    except:
                        gswz = ''
                        print('\t\t公司', url, '没有网址')

                    qy = "-"  # 区域

                    yzbm = "-"  # 邮政编码

                    try:
                        bgdz = detail.\
                            find('div', class_='f0 clearfix mb0').\
                            find('div', class_='in-block sup-ie-company-header-child-2').\
                            find('div', class_='detail-content').text  # 办公地址
                    except:
                        bgdz = ''
                        print('\t\t公司', url, '没有地址， 考虑被注销')

                    zcdz = "-"  # 注册地址

                    contact_info = (lxdh, dzyx, cz, gswz, qy, yzbm, bgdz, zcdz, url)

                    print('\t5、企业联系信息：', contact_info)

                    update_company_lxxx(contact_info, searchMode)

                    return True

                except:
                    print('\t查找联系方式失败')
                    return False

    """
        @brief: 进入企业信息页，获取企业详细工商信息
        @setData：compCh, fddbrr, jyzt1, clrq1, zczb1, sjzb1, gszc1, tyshxxdm1
                  nsrsbh1, zzjgdm1, yyqx1, nsrzz1, hzrq1, gslx1, hy1, rygm1,
                  cbrs1, djjg1, cym1, ywmc1, zcdz1, jyfw1
    """
    def __get_info_Details(self, soup, url, searchMode = False):
        div = soup.find('div', id="_container_baseInfo")

        if div is None:
            print("\t此页查找不到公司内容 [@id='_container_baseInfo']:", url, "考虑被反爬虫阻挡!")
            return False
        else:
            compChdiv = soup.find('div', class_="header")
            if compChdiv is None:
                print("\t此页查找不到公司全称呼 [@class_='header']：", url, "考虑被反爬虫阻挡！但不返回")
                compCh = ""
            else:
                compCh = compChdiv.find('h1', class_="name").get_text()
                print("\t1、企业全名：", compCh)

            frdiv = div.find('div', class_="humancompany")
            fddbrr = "None"
            if frdiv is None:
                print("\t此页查找不到公司法人[@class='humancompany']：", url, "先进行第二轮查找")
                try:
                    fddbrr = div.find('tr').find('span').text
                    print("\t\t找到了公司法人 [//tr/span]：", fddbrr)
                except:
                    print('\t\t此页没有公司法人[//tr/span]', url, "考虑被反爬虫阻挡！但不返回")
            else:
                fddbrr = frdiv.find('a', class_="link-click").get_text()  # 法定代表人
                print('\t2、公司法人：', fddbrr)

            table = div.find('table', class_="table -striped-col -breakall")
            if table is None:
                print("\t此页查找不到公司内容 [table@class='-striped-col -breakall']：", url, "转为注销公司查找模式！")
                tds_else = div.find_all('td')
                if (tds_else is None):
                    print("\t\t此页查找不到注销公司内容，", url, "页面查找失败")
                    return False
                elif (len(tds_else) < 15):
                    print("\t\t此页查找不到注销公司内容[len(tds_else) < 15]:", url, "页面查找失败")
                    return False
                else:
                    print("\t\t找到注销公司内容！", url)
                    self.__get_info_Details_to_sql(
                        tds_else,
                        compCh = compCh,
                        fddbrr = fddbrr,
                        url = url,
                        mode = 2,
                        search = searchMode)
            else:
                tds = table.find_all('td')
                if len(tds) <= 40:
                    print("\t本页面有问题[len(tds) <= 40]:", url)
                    return False
                self.__get_info_Details_to_sql(tds,
                                               compCh = compCh,
                                               fddbrr = fddbrr,
                                               url = url,
                                               mode = 1,
                                               search = searchMode)
            return True

    def __get_info_Details_to_sql(self, tds, compCh, fddbrr, url, mode = 1, search = False):
        if (mode == 1):
            jyzt1 = tds[3].get_text()  # 经营状态
            clrq1 = tds[7].get_text()  # 成立日期
            zczb1 = tds[9].get_text()  # 注册资本
            sjzb1 = tds[11].get_text()  # 实缴资本
            gszc1 = tds[13].get_text()  # 工商注册号
            tyshxxdm1 = tds[15].get_text()  # 统一社会信用代码
            nsrsbh1 = tds[17].get_text()  # 纳税人识别号
            zzjgdm1 = tds[19].get_text()  # 组织机构代码
            yyqx1 = tds[21].get_text()  # 营业期限
            nsrzz1 = tds[23].get_text()  # 纳税人资质
            hzrq1 = tds[25].get_text()  # 核准日期
            gslx1 = tds[27].get_text()  # 公司类型
            hy1 = tds[29].get_text()  # 行业
            rygm1 = tds[31].get_text()  # 人员规模
            cbrs1 = tds[33].get_text()  # 参保人数
            djjg1 = tds[35].get_text()  # 登记机关
            cym1 = tds[37].get_text()  # 曾用名
            ywmc1 = tds[39].get_text()  # 英文名称
            zcdz1 = tds[41].get_text()  # 注册地址
            jyfw1 = tds[43].get_text()  # 经营范围  需要很大的空间 2000
        else:
            # 注销的公司，另外处理
            jyzt1 = tds[5].get_text()  # 经营状态/登记状态
            clrq1 = '-'  # 成立日期
            zczb1 = tds[3].get_text()  # 注册资本/开办资金
            sjzb1 = '-'  # 实缴资本
            gszc1 = tds[13].get_text()  # 工商注册号/原证书号
            tyshxxdm1 = tds[15].get_text()  # 统一社会信用代码
            nsrsbh1 = '-'  # 纳税人识别号
            zzjgdm1 = '-'  # 组织机构代码
            yyqx1 = '-'  # 营业期限
            nsrzz1 = '-'  # 纳税人资质
            hzrq1 = tds[17].get_text()  # 核准日期/有效期
            gslx1 = '已注销'  # 公司类型
            hy1 = '-'  # 行业
            rygm1 = '-'  # 人员规模
            cbrs1 = '-'  # 参保人数
            djjg1 = tds[11].get_text()  # 登记机关/登记管理机关
            cym1 = '-'  # 曾用名
            ywmc1 = '-'  # 英文名称
            zcdz1 = tds[19].get_text()  # 注册地址/住所
            jyfw1 = tds[21].get_text()  # 经营范围  需要很大的空间 2000

        data = (compCh, fddbrr, zczb1, sjzb1, clrq1, jyzt1, tyshxxdm1,
                gszc1, nsrsbh1, zzjgdm1, gslx1, hy1, hzrq1, djjg1,
                yyqx1, nsrzz1, rygm1, cbrs1, cym1, ywmc1, zcdz1, jyfw1, url)

        print('\t3、公司详细信息：', url, data)
        update_company_qybj(data, searchMode = search)
