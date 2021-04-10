import time

class ProxyIP():
    """ 对象变量
    liveTime: 此ip生存时间
    type: 此ip类型
    address: 此ip地址， socket(ip, port)
    request_time: 此ip的请求时间
    deathTime: 此ip的失效时间
    """
    def __init__(self, liveTime, type, address, request_time):
        self.liveTime = liveTime
        self.type = type

        self.address = ('http://' if type == 'http' else 'https://') + address

        self.request_time = request_time
        self.deathTime = request_time + liveTime

    def hasDead(self):
        if time.time() >= self.deathTime:
            return True
        return False

    def indanger(self):
        if self.deathTime - time.time() < 30:
            return True
        return False

    def __eq__(self, other):
        return self.address == other.address

