class WXArticleItem():
    def __init__(self, href, title, brief, gzh):
        self.__href = href
        self.__title = title
        self.__brief = brief
        self.__gzh = gzh
        print((href, title, brief, gzh))
