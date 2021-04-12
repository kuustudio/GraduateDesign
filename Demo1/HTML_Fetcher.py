from Demo1.ProxyManage import *


class HTML_Fetcher():
    """
    类静态变量
    """
    html_retries = 5  # 爬取一个页面请求异常 的换代理IP重试次数
    request_timeout = 10  # 爬取一个页面超时时间 （秒）
    proxyManger = ProxyManger('芝麻')  # 代理池管理对象

    """ 类成员变量
    name = ''
    proxy = {}
    headers = {}
    request_type = ''
    cookie = ''
    """

    def __init__(self, name, headers, request_type='GET'):
        self.name = name
        self.request_type = request_type
        self.headers = headers
        self.proxy_http = ''
        self.proxy_https = ''
        self.cookie = ''

    """
        设置代理IP
    """
    def __setProxy(self, proxy_http, proxy_https):
        self.proxy = {
            'http': proxy_http,
            'https': proxy_https
        }
        self.proxy_http = proxy_http
        self.proxy_https = proxy_https
        print('设置新代理IP ：')
        print('\thttp代理： ', self.proxy_http)
        print('\thttps代理：', self.proxy_https)

    """
        刷新代理池
    """
    def refresh_proxy(self):
        self.__setProxy(HTML_Fetcher.proxyManger.getProxyIP_HTTP(),
                        HTML_Fetcher.proxyManger.getProxyIP_HTTPS())

    """
        设置cookie
    """

    def setCookie(self, cookie):
        self.cookie = cookie
        self.headers['Cookie'] = cookie

    """
        获取网页HTML TEXT
    """

    def get_html(self, url, count, useProxy=True, data=''):
        if self.name == '天眼查':
            assert len(self.cookie) > 0

        if count > HTML_Fetcher.html_retries:
            print("重试超过%d次：建议停机检查：" % HTML_Fetcher.html_retries,
                  url,
                  "目前正在使用代理" if useProxy else "目前不使用代理")
            return ''

        # 检查是否先设置了代理
        if (useProxy):
            if (len(self.proxy_http) == 0 or len(self.proxy_https) == 0):
                self.__setProxy(HTML_Fetcher.proxyManger.getProxyIP_HTTP(),
                                HTML_Fetcher.proxyManger.getProxyIP_HTTPS())
            assert (len(self.proxy_http) > 0)
            assert (len(self.proxy_https) > 0)
            print("爬取此网页：", url, "次数：", count, "时间：", time.time(), " 代理IP：",
                  self.proxy_https if 'https' in url else self.proxy_http)
        else:
            print("爬取此网页：", url, "次数：", count, "时间：", time.time(), "不使用代理IP")

        if (self.request_type == 'GET'):
            try:
                if not useProxy:
                    response = requests.get(url, headers = self.headers)
                else:
                    response = requests.get(url, headers = self.headers,
                                            proxies = self.proxy,
                                            timeout = HTML_Fetcher.request_timeout)
            except BaseException:
                print("请求过程中，异常发生")
                # 这里没有对异常情况作具体处理，只是直接换代理IP 重新请求 就完事昂
                if useProxy:
                    self.__setProxy(HTML_Fetcher.proxyManger.getProxyIP_HTTP(),
                                    HTML_Fetcher.proxyManger.getProxyIP_HTTPS())

                return self.get_html(url, count + 1, useProxy, data)

            if response.status_code is not 200:
                print("请求完毕，但响应不正常， 响应码为：" + str(response.status_code))
                if useProxy:
                    self.__setProxy(HTML_Fetcher.proxyManger.getProxyIP_HTTP(),
                                    HTML_Fetcher.proxyManger.getProxyIP_HTTPS())

                return self.get_html(url, count + 1, useProxy, data)

            else:
                return response.text

        else:
            # POST请求，暂时用不到
            return ''


