import pymysql
from Demo1.MySQL_EXEC_TYC.config import *

def createWenshuTable(connect, cursor):
    sql = '''
    create table Wenshu (
        wenshuName text(100) comment '文书名',
        type text(20) comment '文书类型',
        court text(100) comment '法院',
        wenshuYear text(50) comment '年份',
        area text(50) comment '地区',
        wenshuCode text(100) comment '文书代码',
        wenshuId text(100) comment '文书ID',
        createDate text(50) comment '文书创建日期',
        publicizeDate text(50) comment '文书公开日期',
        detailName text(100) comment '文书内容标题',
        detail text(5000) comment '文书内容',
        judgeAccording text(200) comment '法律依据',
        crime text(100) comment '犯罪原因'
    )
    '''
    cursor.execute(sql)
    connect.commit()

def createDatabase(name):
    preConnect = pymysql.Connect(
        host = host,
        port = port,
        user = user,
        passwd = passwd,
        charset = charset,
    )
    preCursor = preConnect.cursor()

    preCursor.execute('create database if not exists ' + name)
    preConnect.commit()

    newConnect = pymysql.Connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=name,
        charset=charset,
    )
    newCursor = newConnect.cursor()
    try:
        createWenshuTable(newConnect, newCursor)
    except:
        print('[Wenshu]表已经存在')
    return name

connect = pymysql.Connect(
    host = host,
    port = port,
    user = user,
    passwd = passwd,
    db = createDatabase('Wenshu'),
    charset = charset,
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connect.cursor()

def excute(sql, data):
    data_list = list(data)
    for i in range(len(data_list)):
        if type(data_list[i]).__name__ != 'str':
            data_list[i] = str(data_list[i])
        data_list[i] = data_list[i].replace('\'', "\\'")
        data_list[i] = data_list[i].replace('\"', '\\"')
    data = tuple(data_list)
    sqldata = sql % data
    cursor.execute(sqldata)
    connect.commit()

def insertItem(data):
    wenshuId = '\"' + data[3] + '\"'
    sql1 = "insert ignore into `Wenshu`(`wenshuId`) VALUES (%s)" % wenshuId
    cursor.execute(sql1)
    connect.commit()
    sql = 'update Wenshu set wenshuName = "%s",' \
          'type = "%s",' \
          'court = "%s",' \
          'wenshuYear = "%s",' \
          'area = "%s",' \
          'wenshuCode = "%s",' \
          'wenshuId = "%s",' \
          'createDate = "%s",' \
          'publicizeDate = "%s",' \
          'detailName = "%s",' \
          'detail = "%s",' \
          'judgeAccording= "%s",' \
          'crime = "%s" where wenshuId = ' + wenshuId
    excute(sql, data)
