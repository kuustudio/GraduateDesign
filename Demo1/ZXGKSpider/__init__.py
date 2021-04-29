import requests

if __name__ == '__main__':
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
        'Cache-Control': 'max-age=0',
        #'Cookie': 'JSESSIONID=F37C50DD075A0F2232A98835A717F368; UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; _gscu_15322769=18972572ixmhz018; SESSION=34c45484-c189-4106-838b-0f33868995fd; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1618976614,1619357881,1619358020,1619537171; _gscbrs_15322769=1; _gscs_15322769=19537218g5dt2867|pv:15; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619538402',
        'Host': 'zxgk.court.gov.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://zxgk.court.gov.cn/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    url = 'http://zxgk.court.gov.cn/zhzxgk/'

    res = requests.get(url, headers = headers)
    pattern = 'captcha.do\?(.*?)"'
    import re
    txt = res.text
    group = re.search(pattern, txt, re.S)

    print(group[1])
    param = group[1]
    url2 = 'http://zxgk.court.gov.cn/zhzxgk/captcha.do?' + param

    res_png = requests.get(url2, headers = headers)

    with open('2.png', 'wb') as f:
        f.write(res_png.content)
    #print(res_png.content)

    url_data_get = 'http://zxgk.court.gov.cn/zhzxgk/searchZhcx.do'

    header_post = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh-HK;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '284',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=E9C61273BEE39B1A7789FBE075E3AD45; UM_distinctid=1789ace0eca5b-0f964b0224f8c7-c781f38-144000-1789ace0ecb22e; _gscu_15322769=18972572ixmhz018; SESSION=e68c7979-c0dc-4288-878d-dcd7260584a5; _gscbrs_15322769=1; Hm_lvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619357881,1619358020,1619537171,1619665618; Hm_lpvt_d59e2ad63d3a37c53453b996cb7f8d4e=1619665618; _gscs_15322769=19665617d3m7d317|pv:5',
        'Host': 'zxgk.court.gov.cn',
        'Origin': 'http://zxgk.court.gov.cn',
        'Referer': 'http://zxgk.court.gov.cn/zhzxgk/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    form_data = {
        'pName': '王刚',
        'pCardNum': '',
        'selectCourtId': '0',
        'pCode': '', #pCode
        'captchaId': '', #captchaId
        'searchCourtName': '全国法院（包含地方各级法院）',
        'selectCourtArrange': '1',
        'currentPage': '1' #default : 1
    }
    form_data['captchaId'] = '7544bc6b841f4b7788fbab88e51b9796'
    form_data['pCode'] = 'rWdp'

    res = requests.post(url_data_get, headers = header_post, data=form_data)

    print(res.text)