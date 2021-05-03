from Demo1.ProxyManage.ProxyManagerZhima import *

class ProxyManger():

    def __init__(self, proxyProvider = '芝麻'):
        self.proxyType = proxyProvider
        self.manager = ProxyManagerZhima()

    def getProxyIP_HTTP(self):
        http_proxy = self.manager.getIP_HTTP()
        if '{' in http_proxy:
            time.sleep(0.5)
            return self.getProxyIP_HTTP()
        else:
            return http_proxy

    def getProxyIP_HTTPS(self):
        https_proxy = self.manager.getIP_HTTPS()
        if '{' in https_proxy:
            time.sleep(0.5)
            return self.getProxyIP_HTTPS()
        else:
            return https_proxy