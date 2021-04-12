# -*- coding: utf-8 -*-
import pymysql
from Demo1.MySQL_EXEC_TYC.config import *
import time

connect = pymysql.Connect(
    host = host,
    port = port,
    user = user,
    passwd = passwd,
    db = db,
    charset = charset,
    cursorclass = pymysql.cursors.DictCursor
)
cursor = connect.cursor()


def insert(sql, data):
    cursor.execute(sql % data)
    connect.commit()


def excute(sql, data):
    data_list = list(data)
    for i in range(len(data_list)):
        data_list[i] = data_list[i].replace('\'', "\\'")
    data = tuple(data_list)
    sqldata = sql % data
    # print(sqldata)
    # print(sqldata)
    # escape_string_sql = pymysql.escape_string(sqldata)
    # print(escape_string_sql)
    # cursor.execute(escape_string_sql % data)
    cursor.execute(sqldata)

    connect.commit()

"""
    暂未使用，暴力更新公司信息
"""
def update_company(data):
    sql = "update t_company set img= '%s', compCh= '%s', compEn= '%s', sscym= '%s', gsdj= '%s', zczb= '%s', " \
          "sshy= '%s', dsz= '%s', dm= '%s', fddbr= '%s', zjl= '%s', ygrs= '%s', glryrs= '%s', kggd= '%s', sjkzr= '%s', " \
          "zzkzr= '%s', zyyw= '%s', agdm= '%s', agjc= '%s', bgdm= '%s', bgjc= '%s', hgdm= '%s', hgjc= '%s', zqlb= '%s', " \
          "lxdh= '%s', dzyx= '%s', cz= '%s', gswz= '%s', qy= '%s', yzbm= '%s', bgdz= '%s', zcdz= '%s', flag='%d' " \
          "where id= '%s' "
    excute(sql, data)

"""
    更新数据库公司logo
"""
def update_company_imgSource(data):
    sql = "update t_company set img='%s' where id = '%s'"
    excute(sql, data)

"""
    更新数据库公司企业背景信息
"""
def update_company_qybj(data):
    sql = "update t_company set compCh= '%s', fddbrr = '%s', zczb1 = '%s', sjzb1 = '%s', clrq1 = '%s', jyzt1 = '%s', " \
          "tyshxxdm1 = '%s', gszc1 = '%s', nsrsbh1 = '%s', zzjgdm1 = '%s', gslx1 = '%s', hy1 = '%s', " \
          "hzrq1 = '%s', djjg1 = '%s', yyqx1 = '%s', nsrzz1 = '%s', rygm1 = '%s', cbrs1 = '%s', cym1 = '%s', " \
          "ywmc1 = '%s', zcdz1 = '%s', jyfw1 = '%s' " \
          "where id= '%s' "
    excute(sql, data)

    sql = "update t_company set compEn = '%s', " \
          "sscym = '%s', gsdj = '%s', zczb = '%s', sshy = '%s', " \
          "fddbr = '%s', ygrs = '%s', zyyw = '%s' where id = '%s'"

    data_1 = (data[len(data) - 4],
              data[len(data) - 5],
              data[7],
              data[2],
              data[11],
              data[1],
              data[len(data) - 7],
              data[len(data) - 2],
              data[len(data) - 1])

    excute(sql, data_1)

"""
    更新数据库企业简介信息
"""
def update_company_qyjj(data):
    sql = "update t_company set compCh= '%s', compEn= '%s', sscym= '%s', gsdj= '%s', zczb= '%s', " \
          "sshy= '%s', dsz= '%s', dm= '%s', fddbr= '%s', zjl= '%s', ygrs= '%s', glryrs= '%s', kggd= '%s', sjkzr= '%s', " \
          "zzkzr= '%s', zyyw= '%s' " \
          "where id= '%s' "
    excute(sql, data)

"""
    更新数据库企业管理人员信息
"""
def update_company_manage(data):
    sql = "update t_company set dsz = '%s', " \
          "dm = '%s', zjl = '%s', glryrs = '%s' where id = '%s'"
    excute(sql, data)

"""
    更新数据库证券信息
"""
def update_company_zqxx(data):
    sql = "update t_company set agdm= '%s', agjc= '%s', bgdm= '%s', bgjc= '%s', hgdm= '%s', hgjc= '%s', zqlb= '%s' " \
          "where id= '%s' "
    excute(sql, data)

"""
    更新数据库联系方式信息
"""
def update_company_lxxx(data):
    sql = "update t_company set lxdh= '%s', dzyx= '%s', cz= '%s', gswz= '%s', qy= '%s', yzbm= '%s', bgdz= '%s', zcdz= '%s' " \
          "where id= '%s' "
    excute(sql, data)

"""
    标记某公司信息完成爬取
"""
def finish_company(company_href):
    sql = "update t_company set flag = TRUE where id = '%s'"
    cursor.execute(sql % company_href)
    connect.commit()

"""
    插入新公司
"""
def insert_company(id):
    sql = "INSERT IGNORE INTO `t_company`(`id`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (id, False))
    connect.commit()


def do_industry(href):
    sql = 'update t_industry  set flag= "%d" where href = "%s"'
    cursor.execute(sql % (True, href))
    connect.commit()


def clear_industry():
    sql = "truncate table t_industry_copy1"
    cursor.execute(sql)
    connect.commit()

def insert_industry(data):
    sql = "insert  t_industry (`industry`,`href`,`flag`)  VALUES ('%s', '%s', '%d')"
    cursor.execute(sql % data)
    connect.commit()


def get_todo_industry(start,limit_step):
    sql = 'select href from t_industry where flag = false limit '+str(start)+','+str(limit_step)
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company():
    sql = 'select id from t_company where flag = false limit 0,100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def get_todo_company(start,num):
    sql = 'select id from t_company where flag = false limit '+str(start)+','+str(num)
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

def get_todo_company_limit():
    sql = 'select id from t_company where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

"""
    获取某企业的具体信息 URL
"""
def get_company_task():
    sql1 = 'SET @hrefs := 0;  '
    sql2 = 'UPDATE t_company SET flag = 1, id = (SELECT @hrefs := id)WHERE flag  = 0  LIMIT 1;'
    sql3= 'SELECT @hrefs;'
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    todo_href_list = cursor.fetchall()
    connect.commit()
    return todo_href_list
    # todo_href_list = cursor.fetchall()


def insert_industry_province(href):
    sql = "INSERT IGNORE INTO `t_industry_province`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()

"""
    插入新城市
"""
def insert_industry_province_city(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()

"""
    插入新的区/县
"""
def insert_industry_province_city_qu(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()

"""
    插入新的具体分页
"""
def insert_industry_province_city_qu_page(href):
    sql = "INSERT IGNORE INTO `t_industry_province_city_qu_page`(`href`, `flag`) VALUES ('%s', '%d')"
    cursor.execute(sql % (href, False))
    connect.commit()

"""
    获取要爬取的城市url
"""
def get_todo_industry_province_city():
    sql = 'select href from t_industry_province_city where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

"""
    标记此城市的所有 区/县 信息已经全部爬取完
"""
def do_industry_province_city(href):
    sql = 'update t_industry_province_city  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()

"""
    获取要爬取的 区/县 URL
"""
def get_todo_industry_province_city_qu():
    sql = 'select href from t_industry_province_city_qu where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

"""
    标记此 区/县 的所有分页信息已经爬取完
"""
def do_industry_province_city_qu(href):
    sql = 'update t_industry_province_city_qu  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()

"""
    获取未爬取的分页
"""
def get_todo_industry_province_city_qu_page():
    sql = 'select href from t_industry_province_city_qu_page where flag = false limit 100'
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list

"""
    标记某分页的所有公司url已经爬取完成
"""
def do_industry_province_city_qu_page(href):
    sql = 'update t_industry_province_city_qu_page  set flag= true where href = "%s"' % href
    cursor.execute(sql)
    connect.commit()

def get_qu():
    sql = "select * FROM t_industry_province_city where href like '%oc01%areaCode%'"
    # sql = "SELECT * FROM t_industry_province_city_qu_copy where href like  '%oc01?%'"
    cursor.execute(sql)
    todo_href_list = cursor.fetchall()
    return todo_href_list


def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print("the running time is : ", d_time)

    return decor


@timer
def save_to_mysql():
    qu_list = get_qu()
    print(len(qu_list))
    for ii in range(1, 96):
        i = str(ii)
        if ii<10:
            i='0'+i
        print("#####################################################"+i)
        data = []
        sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`) VALUES ('%s')"
        for qu in qu_list:
            href =qu['href'].replace("oc01","oc"+i)
            data.append((href))

            sql = "INSERT IGNORE INTO `t_industry_province_city_qu`(`href`,`flag`) VALUES ('%s','%d')"
            print(sql%(href, False))
            # cursor.execute(sql%(href, False))
        # cursor.executemany(sql, data)
        # connect.commit()

        print('OK')


@timer
def save_to_file():
    qu_list = get_qu()
    print(len(qu_list))
    with open("qu_list1.csv", encoding="UTF-8", mode='w') as f:
        for ii in range(1, 96):
            i = str(ii)
            if ii<10:
                i='0'+i
            print("#####################################################"+i)
            # data = []
            for qu in qu_list:
                # print(qu['href'])
                href =qu['href'].replace("oc01","oc"+i)
                f.write('"%s","%d"'%(href, 0)+"\n")

# save_to_mysql()
# insert_industry_province_city_qu("ssssss")

# print(get_company_task())