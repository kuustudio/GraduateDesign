from Demo1.ProxyManage.ProxyManagerZhima import *

class ProxyManger():

    def __init__(self, proxyProvider = '芝麻'):
        self.proxyType = proxyProvider
        self.manager = ProxyManagerZhima()

    def getProxyIP_HTTP(self):
        return self.manager.getIP_HTTP()

    def getProxyIP_HTTPS(self):
        https_proxy = self.manager.getIP_HTTPS()
        if '{' in https_proxy:
            time.sleep(1)
            return self.getProxyIP_HTTPS()
        else:
            return https_proxy