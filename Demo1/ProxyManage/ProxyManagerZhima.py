from Demo1.ProxyManage.ProxyManger import *
from Demo1.ProxyManage.ProxyIP import *
import requests

"""
    芝麻HTTP代理管理
"""
class ProxyManagerZhima():

    def __init__(self):
        self.proxies_http = []
        self.proxies_https = []
        self.nowProxy_http = None
        self.nowProxy_https = None
        self.api = ''

    """
    @param:num      提取的ip数量， 默认1
    @param:protocol 代理协议 1:HTTP 2:SOCK5 11:HTTPS 
    @param:time     稳定时长 1:5-25min 2:25min-3h 3:3-6h 4:6-12h 7:48-72h
    @param:tiqu     提取模式1：直连ip 2：独享ip 3：隧道ip
    """
    def __buildAPI(self, num = 1, protocol = 'https', useTime = 1, tiqu = 2):
        api = ''
        if tiqu == 1:
            api = 'http://webapi.http.zhimacangku.com/getip?'
        else:
            api = 'http://http.tiqu.letecs.com/getip3?'

        api += 'num=' + str(num)
        api += '&type=1&pro=0&city=0&yys=0'
        api += '&port=' + ('1' if protocol == 'http' else '11')
        api += '&time=' + str(useTime)
        api += '&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='

        if tiqu == 2:
            api += '&gm=4'

        self.api = api
        return self.api


    """
    @brief：获取http代理ip， 默认一次一个
    """
    def getIP_HTTP(self, useTime = 1, tiqu = 2):
        if (self.nowProxy_http is None):
            response_proxy = requests.get(self.__buildAPI(protocol = 'http', useTime = useTime, tiqu = tiqu))
            proxy_http = response_proxy.text.rstrip().split('\r\n').pop(0)

            self.nowProxy_http = ProxyIP(liveTime = 10 * 60,
                                         type = 'http',
                                         address = proxy_http,
                                         request_time = time.time())

            self.proxies_http.append(self.nowProxy_http)

            # print('更换代理IP为 : ' + self.nowProxy_http.address)

            return self.nowProxy_http.address

        else:
            # 现在的代理出了问题
            # 先找现有的，在list池中的ip，把过期的、危险的ip去掉
            newList = []
            for i in range(0, len(self.proxies_http)):
                if not (self.proxies_http[i].hasDead() or self.proxies_http[i].indanger()):
                    newList.append(self.proxies_http[i])
            self.proxies_http = newList

            if len(self.proxies_http) == 0:
                self.nowProxy_http = None
                return self.getIP_HTTP()

            else:
                if (len(self.proxies_http) == 1 and
                        self.proxies_http[0].__eq__(self.nowProxy_http)):
                    self.nowProxy_http = None
                    return self.getIP_HTTP()
                elif len(self.proxies_http) < 5:
                    self.nowProxy_http = None
                    return self.getIP_HTTP()
                else:
                    for proxy in self.proxies_http:
                        if not proxy.__eq__(self.nowProxy_http):
                            proxy.addUseTime()
                            self.nowProxy_http = proxy
                            break
                    return self.nowProxy_http.address

    """
    @brief: 获取https代理ip， 默认一次一个
    """
    def getIP_HTTPS(self, useTime = 1, tiqu = 2, hasGetHTTP = True):
        if hasGetHTTP:
            time.sleep(2)

        if (self.nowProxy_https is None):
            response_proxy = requests.get(self.__buildAPI(protocol='https', useTime=useTime, tiqu=tiqu))
            proxy_https = response_proxy.text.rstrip().split('\r\n').pop(0)

            self.nowProxy_https = ProxyIP(liveTime=10 * 60,
                                         type='https',
                                         address=proxy_https,
                                         request_time=time.time())

            self.proxies_https.append(self.nowProxy_https)

            # print('更换代理IP为 : ' + self.nowProxy_https.address)

            return self.nowProxy_https.address

        else:
            # 现在的代理出了问题
            # 先找现有的，在list池中的ip，把过期的、危险的ip去掉
            newList = []
            for i in range(0, len(self.proxies_https)):
                if not (self.proxies_https[i].hasDead() or \
                        self.proxies_https[i].indanger() or \
                        ('{' in self.proxies_https[i].address)):
                    newList.append(self.proxies_https[i])
            self.proxies_https = newList

            if len(self.proxies_https) == 0:
                self.nowProxy_https = None
                return self.getIP_HTTPS(hasGetHTTP=False)

            else:
                if (len(self.proxies_https) == 1 and
                        self.proxies_https[0].__eq__(self.nowProxy_https)):
                    self.nowProxy_https = None
                    return self.getIP_HTTPS(hasGetHTTP=False)
                elif len(self.proxies_https) < 5:
                    self.nowProxy_https = None
                    return self.getIP_HTTPS(hasGetHTTP=False)
                else:
                    for proxy in self.proxies_https:
                        if not proxy.__eq__(self.nowProxy_https):
                            proxy.addUseTime()
                            self.nowProxy_https = proxy
                            break
                    #print('更换代理IP为 : ' + self.nowProxy_https.address)
                    return self.nowProxy_https.address



