import pandas as pd


class DetailItem():
    def __init__(self, table, title, dataFrame):
        self.__table = table
        self.__title = title
        self.__dataFrame = dataFrame
        self.__infoDict = {}

        self.dataFrameList = []

        if title == '失信被执行人':
            self.__deal_SXBZXR()
        elif title == '终本案件':
            self.__deal_ZBAJ()
        elif title == '限制消费人员':
            self.__deal_XZXFRY()
        elif title == '被执行人':
            self.__deal_BZXR()
        elif title == '失信企业四类人信息':
            self.__deal_SXQYSLRXX()
        else:
            print(title)

    def __deal_SXQYSLRXX(self):
        '''
        处理失信企业四类人信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            key = line[0].strip()
            value = line[1].strip()
            self.__infoDict[key] = value

        columnList = self.__dataFrame.columns.values.tolist()

        for i in range(0, len(columnList)):
            if self.__title == columnList[i][0: columnList[i].find('-')]:
                tableKey = columnList[i]
                selfKey = tableKey[tableKey.find('-') + 1:]
                if selfKey in self.__infoDict.keys():
                    tableValue = self.__infoDict[selfKey]
                else:
                    tableValue = '无信息'
                self.dataFrameList.append(tableValue)
            else:
                self.dataFrameList.append('')

    def __deal_SXBZXR(self):
        '''
        处理失信被执行人信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            key = line[0].strip()
            value = line[1].strip()
            self.__infoDict[key] = value

        columnList = self.__dataFrame.columns.values.tolist()

        for i in range(0, len(columnList)):
            if self.__title == columnList[i][0 : columnList[i].find('-')]:
                tableKey = columnList[i]
                selfKey = tableKey[tableKey.find('-') + 1:]
                if selfKey in self.__infoDict.keys():
                    tableValue = self.__infoDict[selfKey]
                else:
                    tableValue = '无信息'
                self.dataFrameList.append(tableValue)
            else:
                self.dataFrameList.append('')

    def __deal_ZBAJ(self):
        '''
        处理终本案件信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            key = line[0].strip()
            value = line[1].strip()
            self.__infoDict[key] = value

        columnList = self.__dataFrame.columns.values.tolist()

        for i in range(0, len(columnList)):
            if self.__title == columnList[i][0 : columnList[i].find('-')]:
                tableKey = columnList[i]
                selfKey = tableKey[tableKey.find('-') + 1:]
                if selfKey in self.__infoDict.keys():
                    tableValue = self.__infoDict[selfKey]
                else:
                    tableValue = '无信息'
                self.dataFrameList.append(tableValue)
            else:
                self.dataFrameList.append('')

    def __deal_XZXFRY(self):
        '''
        处理限制消费人员信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            key = line[0].strip()
            value = line[1].strip()
            self.__infoDict[key] = value

        columnList = self.__dataFrame.columns.values.tolist()

        for i in range(0, len(columnList)):
            if self.__title == columnList[i][0 : columnList[i].find('-')]:
                tableKey = columnList[i]
                selfKey = tableKey[tableKey.find('-') + 1:]
                if selfKey in self.__infoDict.keys():
                    tableValue = self.__infoDict[selfKey]
                else:
                    tableValue = '无信息'
                self.dataFrameList.append(tableValue)
            else:
                self.dataFrameList.append('')

    def __deal_BZXR(self):
        '''
        处理被执行人信息
        :return:
        '''
        items = self.__table.find_all('tr')
        for item in items:
            itemText = item.text
            line = itemText.split('：')
            key = line[0].strip()
            value = line[1].strip()
            self.__infoDict[key] = value

        columnList = self.__dataFrame.columns.values.tolist()

        for i in range(0, len(columnList)):
            if self.__title == columnList[i][0 : columnList[i].find('-')]:
                tableKey = columnList[i]
                selfKey = tableKey[tableKey.find('-') + 1:]
                if selfKey in self.__infoDict.keys():
                    tableValue = self.__infoDict[selfKey]
                else:
                    tableValue = '无信息'
                self.dataFrameList.append(tableValue)
            else:
                self.dataFrameList.append('')