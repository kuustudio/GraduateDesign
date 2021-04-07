from Demo2.src.mysql import *

def getConnection(soup, url):
    # 联系信息
    div = soup.find('div', class_ = 'box -company-box')
    if div is None or len(div) is 0:
        print("此页查找不到公司内容 _container_corpContactInfo：", url)
    else:
        detail = div.find('div', class_ = 'detail')
        if detail is None or len(detail) is 0:
            print("此页查找不到公司内容 [details]：", url)
        else:
            try:
                lianxi = detail.find('div', class_='in-block sup-ie-company-header-child-1')
                lxdh = detail.find('span', class_ = '').text    # 联系电话
                if len(detail.find_all('span')) <= 15:
                    print("估计界面有问题：len(span) <= 15", url)
                    return True
                dzyx = detail.find('div', class_ = 'in-block sup-ie-company-header-child-2').find('span', class_ = 'email').text    # 电子邮箱
                cz = "-"  # 传真
                gswz = detail.find('div', class_ = 'f0 clearfix mb0').\
                    find('div', class_ = 'in-block sup-ie-company-header-child-1').\
                    find('a', class_ = 'company-link').get('href')  # 公司网址
                qy = "-"  # 区域
                yzbm = "-" # 邮政编码
                bgdz = detail.find('div', class_ = 'f0 clearfix mb0').find('div', class_ = 'in-block sup-ie-company-header-child-2').find('div', class_ = 'detail-content').text # 办公地址
                zcdz = "-"  # 注册地址
                contact_info = (lxdh, dzyx, cz, gswz, qy, yzbm, bgdz, zcdz, url)
                print(contact_info)
                update_company_lxxx(contact_info)
            except:
                print('查找联系方式失败')

def get_info_to_sql(tds, compCh, fddbrr, url, mode = 1):
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
        rygm1 = '-' # 人员规模
        cbrs1 = '-'  # 参保人数

        djjg1 = tds[11].get_text()  # 登记机关/登记管理机关

        cym1 = '-'  # 曾用名
        ywmc1 = '-'  # 英文名称
        zcdz1 = tds[19].get_text()  # 注册地址/住所
        jyfw1 = tds[21].get_text()  # 经营范围  需要很大的空间 2000

    data = (compCh, fddbrr, zczb1, sjzb1, clrq1, jyzt1, tyshxxdm1, gszc1, nsrsbh1, zzjgdm1, gslx1, hy1, hzrq1, djjg1, yyqx1,
    nsrzz1, rygm1, cbrs1, cym1, ywmc1, zcdz1, jyfw1, url)

    print(data)
    update_company_qybj(data)