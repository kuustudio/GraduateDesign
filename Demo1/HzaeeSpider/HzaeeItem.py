import json
from Demo1.HzaeeSpider.ItemParseFunctions_CQZR import *
from Demo1.HzaeeSpider.ItemParseFunctions_ZCZR import *
from Demo1.HzaeeSpider.ItemParseFunctions_FWZL import *
import pandas as pd
from Demo1.HzaeeSpider.SQL_EXEC.MYSQL_EXEC_Hzaee import *
from pymysql.err import InternalError
from bs4 import BeautifulSoup

class HzaeeItem():
    def __init__(self, guoyou, infoDict, htmlFetcher, ItemType = 1):
        self.isGuoyou = guoyou
        assert type(infoDict).__name__ == 'dict'
        self.info = infoDict
        self.htmlFetcher = htmlFetcher
        self.type = ItemType
        # print(infoDict)
        if ItemType == 1 or ItemType == 2:
            self.__dealCQZR()
        elif ItemType == 3:
            self.__dealZCZR()
        elif ItemType == 4:
            self.__dealQYZZ()
        elif ItemType == 5:
            self.__dealFWZL()
        elif ItemType == 6:
            self.__dealZS()
        else:
            self.__dealELSE()

    def __initAttribute_CQZR(self):
        self.createDate = ''  # 信息披露创建时间
        self.itemId = ''  # 标的Id，用于构造Url
        self.name = ''  # 标的名称
        self.number = ''  # 标的编号
        self.startDate = ''  # 信息披露起始时间
        self.endDate = ''  # 信息披露截至时间
        self.area = ''  # 标的企业所在地区
        self.industry = ''  # 标的企业所属行业
        self.reservePrice = ''  # 转让底价
        self.contactInfo = ''  # 联系人及电话
        self.transferCommitment = ''  # 转让申请与承诺

        self.subjectCompanyName = ''  # 标的企业的企业名称
        self.residence = ''  # 标的企业的企业住所
        self.legalPerson = ''  # 标的企业的企业法人
        self.establishDate = ''  # 标的企业的成立日期
        self.registeredCapital = ''  # 标的企业的注册资本
        self.paidCapital = ''  # 标的企业的实缴资本
        self.companyType = ''  # 标的企业的企业类型
        self.industry2 = ''  # 标的企业的所属行业
        self.employeNum = ''  # 标的企业的职工人数
        self.unifiedSocialCreditCode = ''  # 标的企业的统一社会信用代码
        self.businessScale = ''  # 标的企业的经营规模
        self.isAllocateLand = ''  # 标的企业是否含有国有划拨土地
        self.economicNature = ''  # 标的企业的经济性质
        self.businessScope = ''  # 标的企业的经营范围
        self.isPreemptiveRight = ''  # 标的企业的其他股东是否放弃优先购买权
        self.isParticipateTransfer = ''  # 标的企业的企业管理层是否参与受让
        self.isStaffPlacement = ''  # 标的企业是否涉及职工安置
        self.isTransferControl = ''  # 标是否导致标的企业的实际控制权发生转移
        self.top10Shareholder = []  # 标的企业前十位股东名称

        self.aduitYear = ''  # 最近一个年度审计报告年份
        self.operateIncome = ''  # 最近一个年度审计报告营业收入
        self.operateProfit = ''  # 最近一个年度审计报告营业利润
        self.netProfit = ''  # 最近一个年度审计报告净利润
        self.totalAssets = ''  # 最近一个年度审计报告资产总计
        self.totalLiability = ''  # 最近一个年度审计报告负债总计
        self.auditInstitution = ''  # 最近一个年度审计机构
        self.recentReportDate = ''  # 最近一个月审计日期
        self.recentTotalAssets = ''  # 最近一个月资产总计
        self.recentTotalLiability = ''  # 最近一个月负债总计
        self.recentOwnersEquity = ''  # 最近一个月所有者权益
        self.recentOperateIncome = ''  # 最近一个月营业收入
        self.recentOperateProfit = ''  # 最近一个月营业利润
        self.reportType = ''  # 最近一个月填报类型
        self.benchmarkAuditInstitution = ''  # 基准日审计机构
        self.lawOffice = ''  # 律师事务所
        self.internalType = ''  # 内部决策文件类型
        self.fileAndDocument = ''  # 内部决策文件名称及文号
        self.otherDisclosures = ''  # 其他披露事项

        self.transferorName = ''  # 转让方名称
        self.residence2 = ''  # 转让方住所
        self.legal = ''  # 转让方法人
        self.unifiedSocialCreditCode2 = ''  # 转让方统一社会信用代码
        self.registeredCapital2 = ''  # 转让方注册资本
        self.paidCapital2 = ''  # 转让方实收资本
        self.enterpriseType = ''  # 转让方企业类型
        self.industry3 = ''  # 转让方所属行业
        self.businessScale2 = ''  # 转让方经营规模
        self.economicType = ''  # 转让方经济性质
        self.propertyOwnership = ''  # 转让方持有产（股）权比例（%）
        self.transferreProperty = ''  # 转让方拟转让产（股）权比例（%）
        self.decisionType = ''  # 产权转让行为决策文件类型
        self.fileAndDocument2 = ''  # 产权转让行为决策文件名称及文号
        self.regulatoryAuthority = ''  # 产权转让行为监管机构
        self.competentDepartment = ''  # 产权转让行为国家出资企业或主管部门
        self.unifiedSocialCreditCode3 = ''  # 产权转让行为统一社会信用代码
        self.authority = ''  # 产权转让行为批准单位
        self.approvalDate = ''  # 产权转让行为批准日期
        self.approvedFileType = ''  # 产权转让行为批准文件类型
        self.approveFileAndDocument = ''  # 产权转让行为批准文件名称及文号
        self.transfereeQualificate = ''  # 受让方资格条件
        self.isConsortiumTransfer = ''  # 受让方是否接收联合体受让
        self.subjectName = ''  # 标的名称
        self.transferLowPrice = ''  # 转让低价
        self.paymentMethod = ''  # 付款支付方式
        self.installmentPaymentRequest = ''  # 分期付款支付要求
        self.otherConditions = ''  # 与转让相关的其他条件
        self.isPayTradeMargin = ''  # 是否交纳交易保证金
        self.amountPaid = ''  # 交易保证金交纳金额
        self.payTime = ''  # 交易保证金交纳时间
        self.solveMethod = ''  # 交易保证金处置方式
        self.informationDisclosure = ''  # 信息披露期
        self.isPublicationMedia = ''  # 公告是否刊登媒体
        self.publicationMedia = ''  # 刊登媒体
        self.biddeMethod = ''  # 竞价方式

    def __dealCQZR(self):
        self.__initAttribute_CQZR()
        CQZR(self)

    def __initAttribute_ZCZR(self):
        self.createDate = ''  # 信息披露创建时间
        self.itemId = ''  # 标的Id，用于构造Url
        self.name = ''  # 标的名称
        self.number = ''  # 标的编号
        self.startDate = ''  # 信息披露起始时间
        self.endDate = ''  # 信息披露截至时间
        self.area = ''  # 标的企业所在地区
        self.industry = ''  # 标的企业所属行业
        self.reservePrice = ''  # 转让底价
        self.contactInfo = ''  # 联系人及电话
        self.transferCommitment = ''  # 转让申请与承诺
        self.isMortgage = ''  # 标的是否存在抵押情况
        self.isPriorityPurchase = ''  # 权利人是否有意向行使优先购买

        ###realEstates
        self.subjectName = ''  # 标的名称
        self.location = ''  # 房产坐落位置
        self.useStatus = ''  # 房产使用现状
        self.propertyType = ''  # 房产物业类型
        self.improperPropertyLicenseNumber = ''  # 房产不动产权证号
        self.purpose = ''  # 房产用途
        self.commonSituation = ''  # 房产共有情况
        self.area2 = ''  # 房产面积
        self.natureRights = ''  # 房产权利性质
        self.periodUse = ''  # 房产使用期限
        self.otherDisclosures = ''  # 其他披露事项
        ###ownershipCertificates
        self.houseOwnershipCertificate = '' #房屋所有权证号
        self.landUseCertificateNumber = ''  # 土地使用证号
        self.useRightType = '' # 房产使用权类型
        self.rightUseArea = ''  # 房产使用权面积
        ###motorVehicles
        self.brandAndModel = ''#品牌型号
        self.engineNumber = ''#发动机编号
        self.purchaseDate = ''#购置日期
        self.registrationDate = ''#登记日期
        self.kilometersTraveled = ''#行驶公里数
        self.isIndicators = ''#是否带指标
        self.crossyDeadline = ''#交强险截止日
        self.annualValidityPeriod = ''#年检有效期
        ###equipmentSupplies
        self.specificationModel = '' #规格型号
        self.unit = '' #计量单位
        self.quantity = '' #数量
        ###finesMaterials
        self.model = ''  # 规格型号
        self.measurementUnit = ''  # 计量单位
        ###claims
        self.totalDebtInterest = '' # 债权本息合计
        ###others
        self.otherContent = ''

        ###transferorLegalPersons
        self.transferorName = ''  # 转让方名称
        self.residence = ''  # 转让方住所
        self.legal = ''  # 转让方法人
        self.unifiedSocialCreditCode = ''  # 转让方统一社会信用代码
        self.registeredCapital = ''  # 转让方注册资本
        self.enterpriseType = ''  # 转让方企业类型
        self.industry2 = ''  # 转让方所属行业
        self.economicType = ''  # 转让方经济性质
        self.decisionType = ''  # 转让方内部决策类型
        self.fileAndDocument = ''  # 内部决策文件名称及文号
        self.competentDepartment = ''  # 转让行为国家出资企业或主管部门
        self.authority = ''  # 产权转让行为批准单位
        self.approvedFileType = ''  # 产权转让行为批准文件类型
        self.approveFileAndDocument = ''  # 产权转让行为批准文件名称及文号
        ###transferorUnincorporatedSocieties
        self.leader = '' # 转让方负责人

        ###assetTransferBasicInfo
        self.transfereeQualificate = ''  # 受让方资格条件
        self.isAccepteTransferConsortium = ''  # 受让方是否接收联合体受让

        self.subjectName2 = ''  # 标的名称
        self.transferReservePrice = ''  # 转让低价
        self.isSetReservePrice = ''  # 是否设置保留价
        self.paymentRequest = ''  # 付款支付方式
        self.otherConditions = ''  # 与转让相关的其他条件

        self.surveyContact = ''  # 踏勘安排

        self.isPayTradingMargin = ''  # 是否交纳交易保证金
        self.amountPaid = ''  # 交易保证金交纳金额
        self.payTime = ''  # 交易保证金交纳时间
        self.solveMethod = ''  # 交易保证金处置方式

        self.informationDisclosure = ''  # 信息披露期
        self.isPublicationMedia = ''  # 公告是否刊登媒体
        self.publicationMedia = ''  # 刊登媒体
        self.biddeMethod = ''  # 竞价方式

    def __dealZCZR(self):
        self.__initAttribute_ZCZR()
        ZCZR(self)

    def __dealQYZZ(self):
        pass

    def __dealZS(self):
        pass

    def __initAttribute_FWZL(self):
        self.createDate = ''  # 信息披露创建时间
        self.itemId = ''  # 标的Id，用于构造Url
        self.name = ''  # 标的名称
        self.number = ''  # 标的编号
        self.startDate = ''  # 信息披露起始时间
        self.endDate = ''  # 信息披露截至时间
        self.area = ''  # 标的企业所在地区
        self.industry = ''  # 标的企业所属行业
        self.reservePrice = ''  # 转让底价
        self.contactInfo = ''  # 联系人及电话
        self.transferCommitment = ''  # 转让申请与承诺
        self.isMortgage = ''  # 标的是否存在抵押情况
        self.isPriorityPurchase = ''  # 权利人是否有意向行使优先购买

        self.houseName = ''  # 房屋名称
        self.location = ''  # 坐落位置
        self.useStatus = ''  # 使用现状
        self.propertyType = ''  # 物业类型
        self.improperPropertyLicenseNumber = ''  # 不动产权证号
        self.purpose = ''  # 用途
        self.commonSituation = ''  # 共有情况
        self.area2 = ''  # 面积
        self.natureRights = ''  # 权利性质
        self.periodUse = ''  # 使用期限
        self.otherDisclosures = ''  # 其他披露事项

        self.houseOwnershipCertificate = ''  # 房屋所有权证号
        self.planPurposes = ''  # 规划用途
        self.propertyNature = ''  # 房屋性质
        self.constructionArea = ''  # 建筑面积
        self.landUseCertificateNumber = ''  # 土地使用证号
        self.gentle = ''  # 地类（用途）
        self.useRightType = ''  # 使用权类型
        self.endDate2 = ''  # 终止日期
        self.rightUseArea = ''  # 使用权

        self.rentalReservePrice = ''  # 出租底价
        self.rentalArea = ''  # 出租面积
        self.rentalPeriod = ''  # 出租期限
        self.rentDate = ''  # 起租日
        self.rentFreePeriod = ''  # 免租期
        self.rentPaymentRequest = ''  # 租金支付条件
        self.rentAdjustmentMethod = ''  # 租金调整方式
        self.performanceBondPaymentRequirements = ''  # 履约保证金支付要求
        self.waterElectricityAgreement = ''  # 水电气物业费等费用的约定
        self.rentalUseRequirements = ''  # 出租用途要求
        self.allowRenovation = ''  # 是否允许装修改造
        self.otherConditions = ''  # 与出租相关的其他条件
        self.tenantQualification = ''  # 承租方资格条件
        self.surveyContact = ''  # 踏勘安排
        self.isPayTradingMargin = ''  # 交纳交易保证金
        self.amountPaid = ''  # 交纳金额
        self.payTime = ''  # 交纳时间
        self.solveMethod = ''  # 处置方式

        self.informationDisclosure = ''  # 信息披露期
        self.isPublicationMedia = ''  # 公告是否刊登媒体
        self.publicationMedia = ''  # 刊登媒体

        self.biddeMethod = ''  # 竞价方式

    def __dealFWZL(self):
        self.__initAttribute_FWZL()
        FWZL(self)

    def __dealELSE(self):
        pass

    def item2csv_sql(self, dataframe = None, mode = 1):
        '''
        :param dataframe:
        :param mode: mode = 1:转sql， mode = 2:转csv
        :return:
        '''
        attr2chinese = {
            'createDate' : '信息披露创建时间',
            'itemId' : '标的Id，用于构造Url',
            'name' : '标的名称',
            'number' : '标的编号',
            'startDate' : '信息披露起始时间',
            'endDate' : '信息披露截至时间',
            'area' : '标的企业所在地区',
            'industry' : '标的企业所属行业',
            'reservePrice' : '转让底价',
            'contactInfo' : '联系人及电话',
            'transferCommitment' : '转让申请与承诺',

            'subjectCompanyName' : '标的企业的企业名称',
            'residence' : '标的企业的企业住所',
            'legalPerson' : '标的企业的企业法人',
            'establishDate' : '标的企业的成立日期',
            'registeredCapital' : '标的企业的注册资本',
            'paidCapital' : '标的企业的实缴资本',
            'companyType' : '标的企业的企业类型',
            'industry2' : '标的企业的所属行业',
            'employeNum' : '标的企业的职工人数',
            'unifiedSocialCreditCode' : '标的企业的统一社会信用代码',
            'businessScale' : '标的企业的经营规模',
            'isAllocateLand' : '标的企业是否含有国有划拨土地',
            'economicNature' : '标的企业的经济性质',
            'businessScope' : '标的企业的经营范围',
            'isPreemptiveRight' : '标的企业的其他股东是否放弃优先购买权',
            'isParticipateTransfer' : '标的企业的企业管理层是否参与受让',
            'isStaffPlacement' : '标的企业是否涉及职工安置',
            'isTransferControl' : '标是否导致标的企业的实际控制权发生转移',
            'top10Shareholder' : '标的企业前十位股东名称',

            'aduitYear' : '最近一个年度审计报告年份',
            'operateIncome' : '最近一个年度审计报告营业收入',
            'operateProfit' : '最近一个年度审计报告营业利润',
            'netProfit' : '最近一个年度审计报告净利润',
            'totalAssets' : '最近一个年度审计报告资产总计',
            'totalLiability' : '最近一个年度审计报告负债总计',
            'auditInstitution' : '最近一个年度审计机构',
            'recentReportDate' : '最近一个月审计日期',
            'recentTotalAssets' : '最近一个月资产总计',
            'recentTotalLiability' : '最近一个月负债总计',
            'recentOwnersEquity' : '最近一个月所有者权益',
            'recentOperateIncome' : '最近一个月营业收入',
            'recentOperateProfit' : '最近一个月营业利润',
            'reportType' : '最近一个月填报类型',
            'benchmarkAuditInstitution' : '基准日审计机构',
            'lawOffice' : '律师事务所',
            'internalType' : '内部决策文件类型',
            'fileAndDocument' : '内部决策文件名称及文号',
            'otherDisclosures' : '其他披露事项',

            'transferorName' : '转让方名称',
            'residence2' : '转让方住所',
            'legal' : '转让方法人',
            'unifiedSocialCreditCode2' : '转让方统一社会信用代码',
            'registeredCapital2' : '转让方注册资本',
            'paidCapital2' : '转让方实收资本',
            'enterpriseType' : '转让方企业类型',
            'industry3' : '转让方所属行业',
            'businessScale2' : '转让方经营规模',
            'economicType' : '转让方经济性质',
            'propertyOwnership' : '转让方持有产（股）权比例（%）',
            'transferreProperty' : '转让方拟转让产（股）权比例（%）',
            'decisionType' : '产权转让行为决策文件类型',
            'fileAndDocument2' : '产权转让行为决策文件名称及文号',
            'regulatoryAuthority' : '产权转让行为监管机构',
            'competentDepartment' : '产权转让行为国家出资企业或主管部门',
            'unifiedSocialCreditCode3' : '产权转让行为统一社会信用代码',
            'authority' : '产权转让行为批准单位',
            'approvalDate' : '产权转让行为批准日期',
            'approvedFileType' : '产权转让行为批准文件类型',
            'approveFileAndDocument' : '产权转让行为批准文件名称及文号',
            'transfereeQualificate' : '受让方资格条件',
            'isConsortiumTransfer' : '受让方是否接收联合体受让',
            'subjectName' : '标的名称',
            'transferLowPrice' : '转让低价',
            'paymentMethod' : '付款支付方式',
            'installmentPaymentRequest' : '分期付款支付要求',
            'otherConditions' : '与转让相关的其他条件',
            'isPayTradeMargin' : '是否交纳交易保证金',
            'amountPaid' : '交易保证金交纳金额',
            'payTime' : '交易保证金交纳时间',
            'solveMethod' : '交易保证金处置方式',
            'informationDisclosure' : '信息披露期',
            'isPublicationMedia' : '公告是否刊登媒体',
            'publicationMedia' : '刊登媒体',
            'biddeMethod' : '竞价方式',

            'isMortgage' : '标的是否存在抵押情况',
            'isPriorityPurchase' : '权利人是否有意向行使优先购买',
            'location' : '房产坐落位置',
            'useStatus' : '房产使用现状',
            'propertyType' : '房产物业类型',
            'improperPropertyLicenseNumber' : '房产不动产权证号',
            'purpose' : '房产用途',
            'commonSituation' : '房产共有情况',
            'area2' : '房产面积',
            'natureRights' : '房产权利性质',
            'periodUse' : '房产使用期限',
            'houseOwnershipCertificate' : '房屋所有权证号',
            'landUseCertificateNumber' : '土地使用证号',
            'useRightType' : '房产使用权类型',
            'rightUseArea' : '房产使用权面积',
            'brandAndModel' : '品牌型号',
            'engineNumber' : '发动机编号',
            'purchaseDate' : '购置日期',
            'registrationDate' : '登记日期',
            'kilometersTraveled' : '行驶公里数',
            'isIndicators' : '是否带指标',
            'crossyDeadline' : '交强险截止日',
            'annualValidityPeriod' : '年检有效期',
            'specificationModel' : '规格型号',
            'unit' : '计量单位',
            'quantity' : '数量',
            'model' : '规格型号',
            'measurementUnit' : '计量单位',
            'totalDebtInterest' : '债权本息合计',
            'otherContent' : '标的其他情况',
            'leader' : '转让方负责人',
            'isAccepteTransferConsortium' : '受让方是否接收联合体受让',
            'subjectName2' : '标的名称',
            'transferReservePrice' : '转让低价',
            'isSetReservePrice' : '是否设置保留价',
            'paymentRequest' : '付款支付方式',
            'surveyContact' : '踏勘安排',
            'isPayTradingMargin' : '是否交纳交易保证金',

            'houseName': '房屋名称',
            'planPurposes': '规划用途',
            'propertyNature': '房屋性质',
            'constructionArea': '建筑面积',
            'gentle': '地类（用途）',
            'endDate2': '终止日期',
            'rentalReservePrice': '出租底价',
            'rentalArea': '出租面积',
            'rentalPeriod': '出租期限',
            'rentDate': '起租日',
            'rentFreePeriod': '免租期',
            'rentPaymentRequest': '租金支付条件',
            'rentAdjustmentMethod': '租金调整方式',
            'performanceBondPaymentRequirements': '履约保证金支付要求',
            'waterElectricityAgreement': '水电气物业费等费用的约定',
            'rentalUseRequirements': '出租用途要求',
            'allowRenovation': '是否允许装修改造',
            'tenantQualification': '承租方资格条件'
        }

        #if mode == 1 and dataframe is None:
        #    createDatabase('hzaee')
        #    try:
        #        createHzaeeTable()
        #    except InternalError:
        #        print('表已存在！')

        if dataframe is None:
            dataframe = pd.DataFrame(columns = attr2chinese.values())

        name2attr = {}
        for name in attr2chinese.values():
            name2attr[name] = ''

        for key, value in self.__dict__.items():
            if key in attr2chinese.keys():
                name2attr[attr2chinese[key]] = value

        attrlist = []
        for item in dataframe.columns:
            if type(name2attr[item]).__name__ == 'str' and \
                    ('</' in name2attr[item] or '<p>' in name2attr[item]):
                soup = BeautifulSoup(name2attr[item], 'html.parser')
                name2attr[item] = soup.text
            attrlist.append(name2attr[item])

        if mode == 2:
            dataframe.loc[dataframe.index.size] = attrlist
        else:
            insertItem(tuple(attrlist))
        #print(1)
