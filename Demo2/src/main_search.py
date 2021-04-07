# -*- coding: utf-8 -*-
from Demo2.src.get_html import *
from bs4 import BeautifulSoup

def get_info(url, count):
    if count > 50:
        print("重试超过10次：建议停机检查：", url)
        return True
    html = get_html(url, count)
    # f = open("z_company1.html", encoding="UTF-8", mode='r')
    # html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # # 企业logo
    # logdiv = soup.find('div', class_="logo -w100")
    # imgsrc = ""
    # if logdiv is not None:
    #     img = logdiv.find('img', class_="img")
    #     if img is not None:
    #         imgsrc = img.get('data-src')
    #         # print(html)
    # else:
    #     print("此页查找不到公司log logo -w100：", url)

    # 企业简介
    div = soup.find('div', id="nav-main-stockNum")
    if div is None:
        print("此页查找不到公司内容nav-main-stockNum：", url)
        # print(html)
        # refresh_proxy_ip()
        # return get_info(url)
    else:
        table = div.find('table', class_="table -striped-col")
        if table is None:
            print("此页查找不到公司内容 table -striped-col：", url)
            # refresh_proxy_ip()
            # return get_info(url)
        else:
            tds = table.find_all('td')
            if len(tds) <= 31:
                print("估计界面有问题：len(tds) <= 31", url)
                return True
            compCh = tds[1].get_text()  # 公司全称
            compEn = tds[3].get_text()  # 英文名称
            sscym = tds[5].get_text()  # 上市曾用名
            gsdj = tds[7].get_text()  # 工商登记
            zczb = tds[9].get_text()  # 注册资本
            sshy = tds[11].get_text()  # 所属行业
            dsz = tds[13].get_text()  # 董事长
            dm = tds[15].get_text()  # 董秘
            fddbr = tds[17].get_text()  # 法定代表人
            zjl = tds[19].get_text()  # 总经理
            ygrs = tds[21].get_text()  # 员工人数
            glryrs = tds[23].get_text()  # 管理人员人数
            kggd = tds[25].get_text().replace(" ", "")  # 控股股东
            sjkzr = tds[27].get_text().replace(" ", "")  # 实际控制人
            zzkzr = tds[29].get_text().replace(" ", "")  # 最终控制人
            zyyw = tds[31].get_text().replace(" ", "")  # 主营业务'
            desc = (compCh, compEn, sscym, gsdj, zczb, sshy, dsz, dm, fddbr, zjl, ygrs, glryrs, kggd, sjkzr, zzkzr, zyyw, url)
            print(desc)

    # 证券信息
    div = soup.find('div', id="nav-main-secBasicInfoCount")
    if div is None or len(div) is 0:
        print("此页查找不到公司内容nav-main-secBasicInfoCount：", url)
        # print(html)
        # refresh_proxy_ip()
        # return get_info(url)
    else:
        table = div.find('table', class_="table -striped-col")
        if table is None or len(div) is 0:
            print("此页查找不到公司内容table -striped-col：", url)
            # print(html)
        else:
            tds2 = table.find_all('td')
            if len(tds) <= 13:
                print("估计界面有问题：len(tds) <= 13", url)
                return True
            agdm = tds2[1].get_text()  # A股代码
            agjc = tds2[3].get_text()  # A股简称
            bgdm = tds2[5].get_text()  # B股代码
            bgjc = tds2[7].get_text()  # B股简称
            hgdm = tds2[9].get_text()  # H股代码
            hgjc = tds2[11].get_text()  # H股简称
            zqlb = tds2[13].get_text()  # 证券类别
            sec_info = (agdm, agjc, bgdm, bgjc, hgdm, hgjc, zqlb, url)
            print(sec_info)

    # 联系信息
    div = soup.find('div', id="_container_corpContactInfo")
    if div is None or len(div) is 0:
        print("此页查找不到公司内容 _container_corpContactInfo：", url)
        # print(html)
        # refresh_proxy_ip()
        # return get_info(url)
    else:
        table = div.find('table', class_="table -striped-col -breakall")
        if table is None or len(table) is 0:
            print("此页查找不到公司内容 table -striped-col -breakall：", url)
            # print(html)
            # refresh_proxy_ip()
            # return get_info(url)
        else:
            tds = table.find_all('td')
            if len(tds) <= 15:
                print("估计界面有问题：len(tds) <= 15", url)
                return True
            lxdh = tds[1].get_text()  # 联系电话
            dzyx = tds[3].get_text().replace(" ", "")  # 电子邮箱
            cz = tds[5].get_text()  # 传真
            gswz = tds[7].get_text()  # 公司网址
            qy = tds[9].get_text()  # 区域
            yzbm = tds[11].get_text()  # 邮政编码
            bgdz = tds[13].get_text().replace(" ", "")  # 办公地址
            zcdz = tds[15].get_text().replace(" ", "")  # 注册地址
            contact_info = (lxdh, dzyx, cz, gswz, qy, yzbm, bgdz, zcdz, url)
            print(contact_info)


    # 公司背景
    div = soup.find('div', id="_container_baseInfo")
    if div is None:
        print("此页查找不到公司内容 _container_baseInfo：", url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        # print(html)
        refresh_proxy_ip(1)
        return get_info(url, count+1)
    else:
        compChdiv  = soup.find('div', class_="header")
        if compChdiv is None:
            print("此页查找不到公司全称呼  class_=header：", url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！但先不刷新IP！")
            compCh= ""
        else:
            compCh = compChdiv.find('h1', class_="name").get_text()
            print(compCh)
        frdiv=div.find('div', class_="humancompany")
        if frdiv is None:
            print("此页查找不到公司法人 humancompany：", url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
            # print(html)
            refresh_proxy_ip(1)
            return get_info(url, count+1)
        table = div.find('table', class_="table -striped-col -border-top-none -breakall")
        if table is None:
            print("此页查找不到公司内容 table -striped-col -border-top-none -breakall：", url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
            # print(html)
            refresh_proxy_ip(1)
            return get_info(url, count+1)
        else:
            tds = table.find_all('td')
            fddbrr = frdiv.find('a', class_="link-click").get_text()  # 法定代表人
            if len(tds) <= 40:
                print("估计界面有问题：len(tds) <= 40", url)
                exit(1)
            zczb1 = tds[1].get_text()  # 注册资本
            sjzb1 = tds[3].get_text()  # 实缴资本
            clrq1 = tds[6].get_text()  # 成立日期
            jyzt1 = tds[8].get_text()  # 经营状态
            tyshxxdm1 = tds[10].get_text()  # 统一社会信用代码
            gszc1 = tds[12].get_text()  # 工商注册号
            nsrsbh1 = tds[14].get_text()  # 纳税人识别号
            zzjgdm1 = tds[16].get_text()  # 组织机构代码
            gslx1 = tds[18].get_text()  # 公司类型
            hy1 = tds[20].get_text()  # 行业
            hzrq1 = tds[22].get_text()  # 核准日期
            djjg1 = tds[24].get_text()  # 登记机关
            yyqx1 = tds[26].get_text()  # 营业期限
            nsrzz1 = tds[28].get_text()  # 纳税人资质
            rygm1 = tds[30].get_text()  # 人员规模
            cbrs1 = tds[32].get_text()  # 参保人数
            cym1 = tds[34].get_text()   # 曾用名
            ywmc1 = tds[36].get_text()  # 英文名称
            zcdz1 = tds[38].get_text()  # 注册地址
            jyfw1 = tds[40].get_text()  # 经营范围  需要很大的空间 2000
            data = (compCh, fddbrr, zczb1, sjzb1, clrq1, jyzt1, tyshxxdm1, gszc1, nsrsbh1, zzjgdm1, gslx1, hy1, hzrq1, djjg1, yyqx1, nsrzz1, rygm1, cbrs1, cym1, ywmc1, zcdz1, jyfw1, url)

            print(data)


# 根据搜索页获得公司
def get_page_company(page_url):
    html = get_html(page_url, 0)
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)

    # 页内公司href 链表
    company_href_list = []
    company_list_div = soup.find('div', class_="result-list sv-search-container")
    no_company_div = soup.find('div', class_="no-result-container deep-search-detail")
    # 此条件下确实没有分页信息或者公司
    if no_company_div is not None:
        return True
    # 如果没有上面的条件，说明被反爬挡住了
    if company_list_div is None:
        print("此页查找不到分页 scope：", page_url, "注意这个必须要查到哦哦哦哦哦哦哦！！！！！！！！！！！")
        refresh_proxy_ip(1)
        return get_page_company(page_url)
    a_list = company_list_div.find_all('a')

    if a_list is not None:
        for item in a_list:
            if 'https://www.tianyancha.com/company/' in str(item.get("href")):
                if len(str(item.get("href"))) > 36:
                    return str(item.get("href"))




# 爬取 行业 -> 省份直辖市 -> 市区 -> 所有分页 -> 公司下 所有的链接 存到mysql
def get_company_on_name(company_name_list):
    url = 'https://www.tianyancha.com/search?key='
    for company_name in company_name_list:
        print("将爬取的分页：", ['href'])
        company_url = get_page_company(url+company_name)
        get_info(company_url, 1)



if __name__ == '__main__':
    # 根据你的公司名字列表进行爬取
    company_name_list = ["中公教育科技股份有限公司",
                         "恒宁健康产业南京有限公司"]
    get_company_on_name(company_name_list)



