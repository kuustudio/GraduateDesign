import requests
import time

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

Cookie_init_tyc = 'TYCID=7d8b6ee0953411ebbb29973a111131f0; ssuid=6921320576; _ga=GA1.2.1624191352.1617533829; hkGuide=1; _gid=GA1.2.1532262798.1617787893; bdHomeCount=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22237742725%22%2C%22first_id%22%3A%221789c877440764-01393c21ed68b8-c781f38-1327104-1789c877441264%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221789c877440764-01393c21ed68b8-c781f38-1327104-1789c877441264%22%7D; tyc-user-info={%22claimEditPoint%22:%220%22%2C%22explainPoint%22:%220%22%2C%22vipToMonth%22:%22false%22%2C%22personalClaimType%22:%22none%22%2C%22integrity%22:%2220%25%22%2C%22state%22:%220%22%2C%22score%22:%220%22%2C%22anonymityLogo%22:%22https://static.tianyancha.com/design/anonymity/anonymity2.png%22%2C%22announcementPoint%22:%220%22%2C%22messageShowRedPoint%22:%220%22%2C%22vipManager%22:%220%22%2C%22monitorUnreadCount%22:%220%22%2C%22discussCommendCount%22:%220%22%2C%22onum%22:%220%22%2C%22showPost%22:null%2C%22showAnonymityName%22:%22%E5%8C%BF%E5%90%8D%E7%94%A8%E6%88%B7e2baa85%22%2C%22messageBubbleCount%22:%220%22%2C%22claimPoint%22:%220%22%2C%22token%22:%22eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgwMTM1Mzk1MiIsImlhdCI6MTYxNzUzMzg0NCwiZXhwIjoxNjQ5MDY5ODQ0fQ.wEc8uT-M7b-qVXjXJMU_xLhFqSPQXsKISHJ_G5dR_thPSDE2kvl_RAzTRNrYb3xP2crNzRm36Wu1kTU2RiZs-A%22%2C%22schoolAuthStatus%22:%222%22%2C%22userId%22:%22237742725%22%2C%22scoreUnit%22:%22%22%2C%22redPoint%22:%220%22%2C%22myTidings%22:%220%22%2C%22companyAuthStatus%22:%222%22%2C%22originalScore%22:%220%22%2C%22myAnswerCount%22:%220%22%2C%22myQuestionCount%22:%220%22%2C%22signUp%22:%220%22%2C%22privateMessagePointWeb%22:%220%22%2C%22nickname%22:%22%E6%AE%B5%E6%AD%A3%E6%B7%B3%22%2C%22headPicUrl%22:%22https://cdn.tianyancha.com/design/avatar/v3/man11.png%22%2C%22privateMessagePoint%22:%220%22%2C%22bossStatus%22:%222%22%2C%22isClaim%22:%220%22%2C%22yellowDiamondEndTime%22:%220%22%2C%22yellowDiamondStatus%22:%22-1%22%2C%22pleaseAnswerCount%22:%220%22%2C%22bizCardUnread%22:%220%22%2C%22vnum%22:%220%22%2C%22mobile%22:%2218801353952%22%2C%22riskManagement%22:{%22servicePhone%22:null%2C%22mobile%22:18801353952%2C%22title%22:null%2C%22currentStatus%22:null%2C%22lastStatus%22:null%2C%22quickReturn%22:false%2C%22oldVersionMessage%22:null%2C%22riskMessage%22:null}}; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODgwMTM1Mzk1MiIsImlhdCI6MTYxNzUzMzg0NCwiZXhwIjoxNjQ5MDY5ODQ0fQ.wEc8uT-M7b-qVXjXJMU_xLhFqSPQXsKISHJ_G5dR_thPSDE2kvl_RAzTRNrYb3xP2crNzRm36Wu1kTU2RiZs-A; tyc-user-info-save-time=1617533844334; tyc-user-phone=%255B%252218801353952%2522%255D; jsid=SEM-BAIDU-PP-TYC-000001; searchSessionId=1618023584.42103695; aliyungf_tc=aaebe29a5c95f3169006c7f55f9120c2d12d8b6af5ae7f7826c777f2ef9cb17b; acw_tc=781bad4516181101175044359e760433c0f321e3d77aad14fa70bdda710af0; csrfToken=wAF74Bs_0x5k-zBcDASbpIsV; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1618050057,1618054641,1618066774,1618110123; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1618110123; bannerFlag=true; _gat_gtag_UA_123487620_1=1'