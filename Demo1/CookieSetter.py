class CookieSetter():
    def __cookie_list2str(self):
        result = ''
        for i in range(0, len(self.dictCookies)):
            dict = self.dictCookies[i]
            result += dict['name'] + '=' + dict['value']
            if i != len(self.dictCookies) - 1:
                result += '; '
        return result

    def changed(self, newlist):
        self.dictCookies = newlist
        self.strCookie = self.__cookie_list2str()

    def __init__(self, initCookies):
        self.strCookie = ''
        self.dictCookies = []
        assert type(initCookies).__name__ == 'list'
        self.dictCookies = initCookies
        self.strCookie = self.__cookie_list2str()