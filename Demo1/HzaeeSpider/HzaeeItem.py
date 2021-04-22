import json
from Demo1.HzaeeSpider.ItemParseFunctions_CQZR import *
from Demo1.HzaeeSpider.ItemParseFunctions_ZCZR import *

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
            self.__dealZS()
        elif ItemType == 6:
            self.__dealFWZL()
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
        self.companyType = ''  # 标的企业的实缴资本
        self.companyType = ''  # 标的企业的企业类型
        self.industry = ''  # 标的企业的所属行业
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
        self.residence = ''  # 转让方住所
        self.legal = ''  # 转让方法人
        self.unifiedSocialCreditCode = ''  # 转让方统一社会信用代码
        self.registeredCapital = ''  # 转让方注册资本
        self.paidCapital = ''  # 转让方实收资本
        self.enterpriseType = ''  # 转让方企业类型
        self.industry = ''  # 转让方所属行业
        self.businessScale = ''  # 转让方经营规模
        self.economicType = ''  # 转让方经济性质
        self.propertyOwnership = ''  # 转让方持有产（股）权比例（%）
        self.transferreProperty = ''  # 转让方拟转让产（股）权比例（%）
        self.decisionType = ''  # 产权转让行为决策文件类型
        self.fileAndDocument = ''  # 产权转让行为决策文件名称及文号
        self.regulatoryAuthority = ''  # 产权转让行为监管机构
        self.competentDepartment = ''  # 产权转让行为国家出资企业或主管部门
        self.unifiedSocialCreditCode2 = ''  # 产权转让行为统一社会信用代码
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
        self.area = ''  # 房产面积
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
        self.industry = ''  # 转让方所属行业
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

        self.subjectName = ''  # 标的名称
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
        pass

    def __dealFWZL(self):
        pass

    def __dealELSE(self):
        pass
