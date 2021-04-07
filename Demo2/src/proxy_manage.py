from Demo2.src.config import *
import requests
import time

proxy_http = ''
proxy_https = ''

proxies_http = []
proxies_https = []

def get_API(num = 1, protocol = 'http'):
    api = 'http://api.shenlongip.com/ip?key='
    api += appkey_shenglong
    api += '&pattern=txt&count=' + str(num)
    api += '&protocol=' + protocol_shenglong[protocol]
    return api

"""
@brief: 神龙HTTP代理获取，由于每个IP使用期只有3分钟，所以一次不能请求太多
"""
def refresh_proxy_ip_shenglong(num = 1, protocol = 'http'):
    print('刷新代理IP，请求中......')
    global proxies_http
    global proxy_http
    global proxy_https
    global proxies_http
    global proxies_https

    response_proxy = requests.get(get_API(num, protocol))
    if (protocol == 'http'):
        if len(proxies_http) < 1:
            proxies_http = response_proxy.text.rstrip().split('\r\n')
            time.sleep(3)
        proxy_http = proxies_http.pop(0)
    elif (protocol == 'https'):
        if len(proxies_https) < 1:
            proxies_https = response_proxy.text.rstrip().split('\r\n')
            time.sleep(3)
        proxy_https = proxies_https.pop(0)

    print('更换代理IP为 : ' + protocol + '://' + (proxy_http if (protocol == 'http') else proxy_https) )

    return proxy_http if (protocol == 'http') else proxy_https