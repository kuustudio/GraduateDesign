class DetailItem():
    def __init__(self, table, title):
        self.__table = table
        self.__title = title
        self.__infoDict = {}
        if title == '失信被执行人':
            self.__deal_SXBZXR()
        elif title == '终本案件':
            self.__deal_ZBAJ()
        elif title == '限制消费人员':
            self.__deal_XZXFRY()
        elif title == '被执行人':
            self.__deal_BZXR()
        else:
            print(title)

    def __deal_SXBZXR(self):
        '''
        处理失信被执行人信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            self.__infoDict[line[0].strip()] = line[1].strip()

    def __deal_ZBAJ(self):
        '''
        处理终本案件信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            self.__infoDict[line[0].strip()] = line[1].strip()

    def __deal_XZXFRY(self):
        '''
        处理限制消费人员信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            self.__infoDict[line[0].strip()] = line[1].strip()

    def __deal_BZXR(self):
        '''
        处理被执行人信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            self.__infoDict[line[0].strip()] = line[1].strip()