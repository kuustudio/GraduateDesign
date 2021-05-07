import requests
import time
from Demo1.CookieSetter import *

headers_purchase = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

headers_tyc = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5",
        #"Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        #"Host": "www.tianyancha.com",
        #"Sec-Fetch-Dest": "document",
        #"Sec-Fetch-Mode": "navigate",
        #"Sec-Fetch-Site": "none",
        #"Sec-Fetch-User": "?1",
        #"Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

headers_credit = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5",
"Connection": "keep-alive",
"Host": "public.creditchina.gov.cn",
"Origin": "https://www.creditchina.gov.cn",
"Referer": "https://www.creditchina.gov.cn/",
"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
"sec-ch-ua-mobile": "?0",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

headers_hzaee = {
'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
'Connection': 'keep-alive',
# 'Cookie': 'AlteonP=BIMZCRHhg7cL/Uly/GDJVg$$; Hm_lvt_05e3682ca851c2a922f23641393889d4=1617960790,1618219712,1618972159,1618978661; Hm_lpvt_05e3682ca851c2a922f23641393889d4=1618978661',
'Host': 'www.hzaee.com',
# 'Referer': 'https://www.hzaee.com/transfer?type=3',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

Cookie_init_tyc_list = [
{
    "domain": ".tianyancha.com",
    "expirationDate": 1681207899,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.1624191352.1617533829",
    "id": 1
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1618222299,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.1532262798.1617787893",
    "id": 2
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1622717844,
    "hostOnly": False,
    "httpOnly": False,
    "name": "auth_token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgwMTM1Mzk1MiIsImlhdCI6MTYxNzUzMzg0NCwiZXhwIjoxNjQ5MDY5ODQ0fQ.wEc8uT-M7b-qVXjXJMU_xLhFqSPQXsKISHJ_G5dR_thPSDE2kvl_RAzTRNrYb3xP2crNzRm36Wu1kTU2RiZs-A",
    "id": 3
},
{
    "domain": ".tianyancha.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "bannerFlag",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "False",
    "id": 4
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1618156800,
    "hostOnly": False,
    "httpOnly": False,
    "name": "bannerHide",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "18801353952",
    "id": 5
},
{
    "domain": ".tianyancha.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lpvt_e92c8d65d92d534b0fc290df538b4758",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "1618135899",
    "id": 6
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1649671899,
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lvt_e92c8d65d92d534b0fc290df538b4758",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1618116422,1618116516,1618124165,1618135349",
    "id": 7
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1620658772.069306,
    "hostOnly": False,
    "httpOnly": False,
    "name": "jsid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "SEM-BAIDU-PP-TYC-000001",
    "id": 8
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1620704193,
    "hostOnly": False,
    "httpOnly": False,
    "name": "searchSessionId",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1618112193.60637977",
    "id": 9
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 7925335898,
    "hostOnly": False,
    "httpOnly": False,
    "name": "sensorsdata2015jssdkcross",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%7B%22distinct_id%22%3A%22237742725%22%2C%22first_id%22%3A%221789c877440764-01393c21ed68b8-c781f38-1327104-1789c877441264%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221789c877440764-01393c21ed68b8-c781f38-1327104-1789c877441264%22%7D",
    "id": 10
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 2145956226,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ssuid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "6921320576",
    "id": 11
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1622717844,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tyc-user-info",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "{%22claimEditPoint%22:%220%22%2C%22explainPoint%22:%220%22%2C%22vipToMonth%22:%22False%22%2C%22personalClaimType%22:%22none%22%2C%22integrity%22:%2220%25%22%2C%22state%22:%220%22%2C%22score%22:%220%22%2C%22anonymityLogo%22:%22https://static.tianyancha.com/design/anonymity/anonymity2.png%22%2C%22announcementPoint%22:%220%22%2C%22messageShowRedPoint%22:%220%22%2C%22vipManager%22:%220%22%2C%22monitorUnreadCount%22:%220%22%2C%22discussCommendCount%22:%220%22%2C%22onum%22:%220%22%2C%22showPost%22:null%2C%22showAnonymityName%22:%22%E5%8C%BF%E5%90%8D%E7%94%A8%E6%88%B7e2baa85%22%2C%22messageBubbleCount%22:%220%22%2C%22claimPoint%22:%220%22%2C%22token%22:%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgwMTM1Mzk1MiIsImlhdCI6MTYxNzUzMzg0NCwiZXhwIjoxNjQ5MDY5ODQ0fQ.wEc8uT-M7b-qVXjXJMU_xLhFqSPQXsKISHJ_G5dR_thPSDE2kvl_RAzTRNrYb3xP2crNzRm36Wu1kTU2RiZs-A%22%2C%22schoolAuthStatus%22:%222%22%2C%22userId%22:%22237742725%22%2C%22scoreUnit%22:%22%22%2C%22redPoint%22:%220%22%2C%22myTidings%22:%220%22%2C%22companyAuthStatus%22:%222%22%2C%22originalScore%22:%220%22%2C%22myAnswerCount%22:%220%22%2C%22myQuestionCount%22:%220%22%2C%22signUp%22:%220%22%2C%22privateMessagePointWeb%22:%220%22%2C%22nickname%22:%22%E6%AE%B5%E6%AD%A3%E6%B7%B3%22%2C%22headPicUrl%22:%22https://cdn.tianyancha.com/design/avatar/v3/man11.png%22%2C%22privateMessagePoint%22:%220%22%2C%22bossStatus%22:%222%22%2C%22isClaim%22:%220%22%2C%22yellowDiamondEndTime%22:%220%22%2C%22yellowDiamondStatus%22:%22-1%22%2C%22pleaseAnswerCount%22:%220%22%2C%22bizCardUnread%22:%220%22%2C%22vnum%22:%220%22%2C%22mobile%22:%2218801353952%22%2C%22riskManagement%22:{%22servicePhone%22:null%2C%22mobile%22:18801353952%2C%22title%22:null%2C%22currentStatus%22:null%2C%22lastStatus%22:null%2C%22quickReturn%22:False%2C%22oldVersionMessage%22:null%2C%22riskMessage%22:null}}",
    "id": 12
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1622717844,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tyc-user-info-save-time",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1617533844334",
    "id": 13
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1622717844,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tyc-user-phone",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%255B%252218801353952%2522%255D",
    "id": 14
},
{
    "domain": ".tianyancha.com",
    "expirationDate": 1680605824.105185,
    "hostOnly": False,
    "httpOnly": False,
    "name": "TYCID",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "7d8b6ee0953411ebbb29973a111131f0",
    "id": 15
},
{
    "domain": "www.tianyancha.com",
    "expirationDate": 1618137146.559333,
    "hostOnly": True,
    "httpOnly": True,
    "name": "acw_tc",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "2f6fc12d16181353460081292e6f6f631de3eb04e405955e6982e6bfc065a2",
    "id": 16
},
{
    "domain": "www.tianyancha.com",
    "hostOnly": True,
    "httpOnly": True,
    "name": "aliyungf_tc",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "6621abf23984e906996449d95d46282196a9fef9bd25784ede4bb9c4b80e3523",
    "id": 17
},
{
    "domain": "www.tianyancha.com",
    "expirationDate": 1620396434.800836,
    "hostOnly": True,
    "httpOnly": False,
    "name": "bdHomeCount",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 18
},
{
    "domain": "www.tianyancha.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "csrfToken",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "5OaYfvFG6wOsD5CH6bA9Q5L9",
    "id": 19
},
{
    "domain": "www.tianyancha.com",
    "expirationDate": 1620185849.773977,
    "hostOnly": True,
    "httpOnly": False,
    "name": "hkGuide",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 20
}
]

cookieSetter = CookieSetter(Cookie_init_tyc_list)

# 改为list，类型为引用，可在外修改
Cookie_init_tyc = []
Cookie_init_tyc.append(cookieSetter.strCookie)

# 微信爬取Cookie
Cookie_init_wx_list = [
{
    "domain": ".sogou.com",
    "expirationDate": 1650875785.875945,
    "hostOnly": False,
    "httpOnly": False,
    "name": "IPLOC",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "CN1100",
    "id": 1
},
{
    "domain": ".sogou.com",
    "expirationDate": 1620549684.91627,
    "hostOnly": False,
    "httpOnly": False,
    "name": "passport",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "5|1619340085|1620549685|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8Y3J0OjEwOjE2MTkzNDAwODV8cmVmbmljazoyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8dXNlcmlkOjQ0Om85dDJsdUtJNHhnT0RuMDliaktZNVROdklzLVlAd2VpeGluLnNvaHUuY29tfA|e036adb998|t-SChwRRREAHIcj9ncEz4RfElCiM1xF4F-v8d2y69uGG7GbQYBCZV_c7mQ3nIzSjVeuLxrWPQUQVuA4rDHd5ffXedz4SzuppOBIxeb0soWhvGCvN0DwYrU00nDcSU3OlIs6EhI6uvtQNZnv9ANooZ6jTHq0Zb75Fv0XAd5QkeoA",
    "id": 2
},
{
    "domain": ".sogou.com",
    "expirationDate": 1620549684.916114,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ppinf",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "5|1619340085|1620549685|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8Y3J0OjEwOjE2MTkzNDAwODV8cmVmbmljazoyNzolRTklOTMlODElRTklOTMlQkElRTclOUIlOTZ8dXNlcmlkOjQ0Om85dDJsdUtJNHhnT0RuMDliaktZNVROdklzLVlAd2VpeGluLnNvaHUuY29tfA",
    "id": 3
},
{
    "domain": ".sogou.com",
    "expirationDate": 1620549684.916241,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ppinfo",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "0b475c99a9",
    "id": 4
},
{
    "domain": ".sogou.com",
    "expirationDate": 1620549684.916204,
    "hostOnly": False,
    "httpOnly": False,
    "name": "pprdig",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "t-SChwRRREAHIcj9ncEz4RfElCiM1xF4F-v8d2y69uGG7GbQYBCZV_c7mQ3nIzSjVeuLxrWPQUQVuA4rDHd5ffXedz4SzuppOBIxeb0soWhvGCvN0DwYrU00nDcSU3OlIs6EhI6uvtQNZnv9ANooZ6jTHq0Zb75Fv0XAd5QkeoA",
    "id": 5
},
{
    "domain": ".sogou.com",
    "expirationDate": 1620549684.916289,
    "hostOnly": False,
    "httpOnly": False,
    "name": "sgid",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "05-50247413-AWCFKzUyXy93mfwy7b0oI4E",
    "id": 6
},
{
    "domain": ".sogou.com",
    "expirationDate": 1650876034.466666,
    "hostOnly": False,
    "httpOnly": False,
    "name": "SNUID",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "20626E5A818441467B1973008128FFED",
    "id": 7
},
{
    "domain": ".sogou.com",
    "expirationDate": 2250059785.943009,
    "hostOnly": False,
    "httpOnly": False,
    "name": "SUID",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "A1E3EFDB7050A00A0000000060852A0A",
    "id": 8
},
{
    "domain": ".sogou.com",
    "expirationDate": 1934699787.454339,
    "hostOnly": False,
    "httpOnly": False,
    "name": "SUV",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "00764FC2DBEFE3A160852A0BEDD5A820",
    "id": 9
},
{
    "domain": ".weixin.sogou.com",
    "expirationDate": 2250059785.875974,
    "hostOnly": False,
    "httpOnly": False,
    "name": "SUID",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "A1E3EFDB1B0DA00A0000000060852A0A",
    "id": 10
},
{
    "domain": "weixin.sogou.com",
    "expirationDate": 1621931785.875865,
    "hostOnly": True,
    "httpOnly": False,
    "name": "ABTEST",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "0|1619339786|v1",
    "id": 11
},
{
    "domain": "weixin.sogou.com",
    "hostOnly": True,
    "httpOnly": False,
    "name": "JSESSIONID",
    "path": "/",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "aaae7fq_ewU7Nb4LmliKx",
    "id": 12
},
{
    "domain": "weixin.sogou.com",
    "hostOnly": True,
    "httpOnly": True,
    "name": "ppmdig",
    "path": "/",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "16193400850000001bcc89d8cf4cdf3966d0ae1f9bc9687c",
    "id": 13
},
{
    "domain": "weixin.sogou.com",
    "expirationDate": 1627979786,
    "hostOnly": True,
    "httpOnly": False,
    "name": "weixinIndexVisited",
    "path": "/",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 14
}
]
cookieSetter_wx = CookieSetter(Cookie_init_wx_list)
Cookie_init_wx = cookieSetter_wx.strCookie

# 裁判文书爬取Cookie
Cookie_init_Wenshu_list = [
{
    "domain": ".court.gov.cn",
    "expirationDate": 1636114182,
    "hostOnly": False,
    "httpOnly": False,
    "name": "UM_distinctid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "17946bbca9092-08a4068b8d23cc-c3f3568-144000-17946bbca91375",
    "id": 1
},
{
    "domain": "wenshu.court.gov.cn",
    "hostOnly": True,
    "httpOnly": True,
    "name": "SESSION",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "5ea17c30-6cac-44f7-b228-e63a95c3c375",
    "id": 2
}
]
cookieSetter_wenshu = CookieSetter(Cookie_init_Wenshu_list)
Cookie_init_Wenshu = cookieSetter_wenshu.strCookie