import pymysql
from Demo1.MySQL_EXEC_TYC.config import *
import time

connect = pymysql.Connect(
    host = remote_host,
    port = remote_port,
    user = remote_user,
    passwd = remote_passwd,
    db = 'hzaee',
    charset = charset,
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connect.cursor()

def createDatabase(name):
    global connect
    global cursor
    cursor.execute('create database if not exists ' + name)
    connect.commit()

    connect = pymysql.Connect(
        host = remote_host,
        port = remote_port,
        user = remote_user,
        passwd = remote_passwd,
        db = 'hzaee',
        charset = charset,
        cursorclass = pymysql.cursors.DictCursor
    )
    cursor = connect.cursor()

def createHzaeeTable():
    sql = '''
    create table Hzaee (
        createDate text(100) comment '信息披露创建时间',
        itemId text(100) comment '标的Id，用于构造Url',
        name text(100) comment '标的名称' not null ,
        number text(100) comment '标的编号',
        startDate text(100) comment '信息披露起始时间',
        endDate text(100) comment '信息披露截至时间',
        area text(100) comment '标的企业所在地区',
        industry text(100) comment '标的企业所属行业',
        reservePrice text(100) comment '转让底价',
        contactInfo text(100) comment '联系人及电话',
        transferCommitment text(1000) comment '转让申请与承诺',
        subjectCompanyName text(100) comment '标的企业的企业名称',
        residence text(100) comment '标的企业的企业住所',
        legalPerson text(100) comment '标的企业的企业法人',
        establishDate text(100) comment '标的企业的成立日期',
        registeredCapital text(100) comment '标的企业的注册资本',
        paidCapital text(100) comment '标的企业的实缴资本',
        companyType text(100) comment '标的企业的企业类型',
        industry2 text(100) comment '标的企业的所属行业',
        employeNum text(100) comment '标的企业的职工人数',
        unifiedSocialCreditCode text(100) comment '标的企业的统一社会信用代码',
        businessScale text(100) comment '标的企业的经营规模',
        isAllocateLand text(100) comment '标的企业是否含有国有划拨土地',
        economicNature text(100) comment '标的企业的经济性质',
        businessScope text(500) comment '标的企业的经营范围',
        isPreemptiveRight text(100) comment '标的企业的其他股东是否放弃优先购买权',
        isParticipateTransfer text(100) comment '标的企业的企业管理层是否参与受让',
        isStaffPlacement text(100) comment '标的企业是否涉及职工安置',
        isTransferControl text(100) comment '标是否导致标的企业的实际控制权发生转移',
        top10Shareholder text(500) comment '标的企业前十位股东名称',
        aduitYear text(100) comment '最近一个年度审计报告年份',
        operateIncome text(100) comment '最近一个年度审计报告营业收入',
        operateProfit text(100) comment '最近一个年度审计报告营业利润',
        netProfit text(100) comment '最近一个年度审计报告净利润',
        totalAssets text(100) comment '最近一个年度审计报告资产总计',
        totalLiability text(100) comment '最近一个年度审计报告负债总计',
        auditInstitution text(100) comment '最近一个年度审计机构',
        recentReportDate text(100) comment '最近一个月审计日期',
        recentTotalAssets text(100) comment '最近一个月资产总计',
        recentTotalLiability text(100) comment '最近一个月负债总计',
        recentOwnersEquity text(100) comment '最近一个月所有者权益',
        recentOperateIncome text(100) comment '最近一个月营业收入',
        recentOperateProfit text(100) comment '最近一个月营业利润',
        reportType text(100) comment '最近一个月填报类型',
        benchmarkAuditInstitution text(100) comment '基准日审计机构',
        lawOffice text(100) comment '律师事务所',
        internalType text(100) comment '内部决策文件类型',
        fileAndDocument text(100) comment '内部决策文件名称及文号',
        otherDisclosures text(6000) comment '其他披露事项',
        transferorName text(100) comment '转让方名称',
        residence2 text(100) comment '转让方住所',
        legal text(100) comment '转让方法人',
        unifiedSocialCreditCode2 text(100) comment '转让方统一社会信用代码',
        registeredCapital2 text(100) comment '转让方注册资本',
        paidCapital2 text(100) comment '转让方实收资本',
        enterpriseType text(100) comment '转让方企业类型',
        industry3 text(100) comment '转让方所属行业',
        businessScale2 text(100) comment '转让方经营规模',
        economicType text(100) comment '转让方经济性质',
        propertyOwnership text(100) comment '转让方持有产（股）权比例（%）',
        transferreProperty text(100) comment '转让方拟转让产（股）权比例（%）',
        decisionType text(100) comment '产权转让行为决策文件类型',
        fileAndDocument2 text(100) comment '产权转让行为决策文件名称及文号',
        regulatoryAuthority text(100) comment '产权转让行为监管机构',
        competentDepartment text(100) comment '产权转让行为国家出资企业或主管部门',
        unifiedSocialCreditCode3 text(100) comment '产权转让行为统一社会信用代码',
        authority text(100) comment '产权转让行为批准单位',
        approvalDate text(100) comment '产权转让行为批准日期',
        approvedFileType text(100) comment '产权转让行为批准文件类型',
        approveFileAndDocument text(100) comment '产权转让行为批准文件名称及文号',
        transfereeQualificate text(1000) comment '受让方资格条件',
        isConsortiumTransfer text(100) comment '受让方是否接收联合体受让',
        subjectName text(100) comment '标的名称',
        transferLowPrice text(100) comment '转让低价',
        paymentMethod text(100) comment '付款支付方式',
        installmentPaymentRequest text(100) comment '分期付款支付要求',
        otherConditions text(3000) comment '与转让相关的其他条件',
        isPayTradeMargin text(100) comment '是否交纳交易保证金',
        amountPaid text(100) comment '交易保证金交纳金额',
        payTime text(100) comment '交易保证金交纳时间',
        solveMethod text(1000) comment '交易保证金处置方式',
        informationDisclosure text(100) comment '信息披露期',
        isPublicationMedia text(100) comment '公告是否刊登媒体',
        publicationMedia text(100) comment '刊登媒体',
        biddeMethod text(100) comment '竞价方式',
        isMortgage text(100) comment '标的是否存在抵押情况',
        isPriorityPurchase text(100) comment '权利人是否有意向行使优先购买',
        location text(100) comment '房产坐落位置',
        useStatus text(100) comment '房产使用现状',
        propertyType text(100) comment '房产物业类型',
        improperPropertyLicenseNumber text(100) comment '房产不动产权证号',
        purpose text(100) comment '房产用途',
        commonSituation text(100) comment '房产共有情况',
        area2 text(100) comment '房产面积',
        natureRights text(100) comment '房产权利性质',
        periodUse text(100) comment '房产使用期限',
        houseOwnershipCertificate text(100) comment '房屋所有权证号',
        landUseCertificateNumber text(100) comment '土地使用证号',
        useRightType text(100) comment '房产使用权类型',
        rightUseArea text(100) comment '房产使用权面积',
        brandAndModel text(100) comment '品牌型号',
        engineNumber text(100) comment '发动机编号',
        purchaseDate text(100) comment '购置日期',
        registrationDate text(100) comment '登记日期',
        kilometersTraveled text(100) comment '行驶公里数',
        isIndicators text(100) comment '是否带指标',
        crossyDeadline text(100) comment '交强险截止日',
        annualValidityPeriod text(100) comment '年检有效期',
        specificationModel text(100) comment '规格型号',
        unit text(100) comment '计量单位',
        quantity text(100) comment '数量',
        model text(100) comment '规格型号',
        measurementUnit text(100) comment '计量单位',
        totalDebtInterest text(100) comment '债权本息合计',
        otherContent text(100) comment '标的其他情况',
        leader text(100) comment '转让方负责人',
        isAccepteTransferConsortium text(100) comment '受让方是否接收联合体受让',
        subjectName2 text(100) comment '标的名称',
        transferReservePrice text(100) comment '转让低价',
        isSetReservePrice text(100) comment '是否设置保留价',
        paymentRequest text(100) comment '付款支付方式',
        surveyContact text(400) comment '踏勘安排',
        isPayTradingMargin text(100) comment '是否交纳交易保证金',
        houseName text(100) comment '房屋名称',
        planPurposes text(100) comment '规划用途',
        propertyNature text(100) comment '房屋性质',
        constructionArea text(100) comment '建筑面积',
        gentle text(100) comment '地类（用途）',
        endDate2 text(100) comment '终止日期',
        rentalReservePrice text(100) comment '出租底价',
        rentalArea text(100) comment '出租面积',
        rentalPeriod text(100) comment '出租期限',
        rentDate text(100) comment '起租日',
        rentFreePeriod text(100) comment '免租期',
        rentPaymentRequest text(100) comment '租金支付条件',
        rentAdjustmentMethod text(100) comment '租金调整方式',
        performanceBondPaymentRequirements text(100) comment '履约保证金支付要求',
        waterElectricityAgreement text(100) comment '水电气物业费等费用的约定',
        rentalUseRequirements text(100) comment '出租用途要求',
        allowRenovation text(100) comment '是否允许装修改造',
        tenantQualification text(1000) comment '承租方资格条件'
    )
    '''
    cursor.execute(sql)
    connect.commit()

def excute(sql, data):
    data_list = list(data)
    for i in range(len(data_list)):
        if type(data_list[i]).__name__ != 'str':
            data_list[i] = str(data_list[i])
        data_list[i] = data_list[i].replace('\'', "\\'")
        data_list[i] = data_list[i].replace('\"', '\\"')
    data = tuple(data_list)
    sqldata = sql % data
    # print(sqldata)
    # print(sqldata)
    # escape_string_sql = pymysql.escape_string(sqldata)
    # print(escape_string_sql)
    # cursor.execute(escape_string_sql % data)
    cursor.execute(sqldata)

    connect.commit()

def insertItem(data):
    itemId = '\"' + data[1] + '\"'
    sql1 = "insert ignore into `hzaee`(`itemId`) VALUES (%s)" % itemId
    cursor.execute(sql1)
    connect.commit()
    sql = 'update hzaee set createDate = "%s",' \
          'itemId = "%s",' \
          'name = "%s",' \
          'number = "%s",' \
          'startDate = "%s",' \
          'endDate = "%s",' \
          'area = "%s",' \
          'industry = "%s",' \
          'reservePrice = "%s",' \
          'contactInfo = "%s",' \
          'transferCommitment = "%s",' \
          'subjectCompanyName = "%s",' \
          'residence = "%s",' \
          'legalPerson = "%s",' \
          'establishDate = "%s",' \
          'registeredCapital = "%s",' \
          'paidCapital = "%s",' \
          'companyType = "%s",' \
          'industry2 = "%s",' \
          'employeNum = "%s",' \
          'unifiedSocialCreditCode = "%s",' \
          'businessScale = "%s",' \
          'isAllocateLand = "%s",' \
          'economicNature = "%s",' \
          'businessScope = "%s",' \
          'isPreemptiveRight = "%s",' \
          'isParticipateTransfer = "%s",' \
          'isStaffPlacement = "%s",' \
          'isTransferControl = "%s",' \
          'top10Shareholder = "%s",' \
          'aduitYear = "%s",' \
          'operateIncome = "%s",' \
          'operateProfit = "%s",' \
          'netProfit = "%s",' \
          'totalAssets = "%s",' \
          'totalLiability = "%s",' \
          'auditInstitution = "%s",' \
          'recentReportDate = "%s",' \
          'recentTotalAssets = "%s",' \
          'recentTotalLiability = "%s",' \
          'recentOwnersEquity = "%s",' \
          'recentOperateIncome = "%s",' \
          'recentOperateProfit = "%s",' \
          'reportType = "%s",' \
          'benchmarkAuditInstitution = "%s",' \
          'lawOffice = "%s",' \
          'internalType = "%s",' \
          'fileAndDocument = "%s",' \
          'otherDisclosures = "%s",' \
          'transferorName = "%s",' \
          'residence2 = "%s",' \
          'legal = "%s",' \
          'unifiedSocialCreditCode2 = "%s",' \
          'registeredCapital2 = "%s",' \
          'paidCapital2 = "%s",' \
          'enterpriseType = "%s",' \
          'industry3 = "%s",' \
          'businessScale2 = "%s",' \
          'economicType = "%s",' \
          'propertyOwnership = "%s",' \
          'transferreProperty = "%s",' \
          'decisionType = "%s",' \
          'fileAndDocument2 = "%s",' \
          'regulatoryAuthority = "%s",' \
          'competentDepartment = "%s",' \
          'unifiedSocialCreditCode3 = "%s",' \
          'authority = "%s",' \
          'approvalDate = "%s",' \
          'approvedFileType = "%s",' \
          'approveFileAndDocument = "%s",' \
          'transfereeQualificate = "%s",' \
          'isConsortiumTransfer = "%s",' \
          'subjectName = "%s",' \
          'transferLowPrice = "%s",' \
          'paymentMethod = "%s",' \
          'installmentPaymentRequest = "%s",' \
          'otherConditions = "%s",' \
          'isPayTradeMargin = "%s",' \
          'amountPaid = "%s",' \
          'payTime = "%s",' \
          'solveMethod = "%s",' \
          'informationDisclosure = "%s",' \
          'isPublicationMedia = "%s",' \
          'publicationMedia = "%s",' \
          'biddeMethod = "%s",' \
          'isMortgage = "%s",' \
          'isPriorityPurchase = "%s",' \
          'location = "%s",' \
          'useStatus = "%s",' \
          'propertyType = "%s",' \
          'improperPropertyLicenseNumber = "%s",' \
          'purpose = "%s",' \
          'commonSituation = "%s",' \
          'area2 = "%s",' \
          'natureRights = "%s",' \
          'periodUse = "%s",' \
          'houseOwnershipCertificate = "%s",' \
          'landUseCertificateNumber = "%s",' \
          'useRightType = "%s",' \
          'rightUseArea = "%s",' \
          'brandAndModel = "%s",' \
          'engineNumber = "%s",' \
          'purchaseDate = "%s",' \
          'registrationDate = "%s",' \
          'kilometersTraveled = "%s",' \
          'isIndicators = "%s",' \
          'crossyDeadline = "%s",' \
          'annualValidityPeriod = "%s",' \
          'specificationModel = "%s",' \
          'unit = "%s",' \
          'quantity = "%s",' \
          'model = "%s",' \
          'measurementUnit = "%s",' \
          'totalDebtInterest = "%s",' \
          'otherContent = "%s",' \
          'leader = "%s",' \
          'isAccepteTransferConsortium = "%s",' \
          'subjectName2 = "%s",' \
          'transferReservePrice = "%s",' \
          'isSetReservePrice = "%s",' \
          'paymentRequest = "%s",' \
          'surveyContact = "%s",' \
          'isPayTradingMargin = "%s",' \
          'houseName = "%s",' \
          'planPurposes = "%s",' \
          'propertyNature = "%s",' \
          'constructionArea = "%s",' \
          'gentle = "%s",' \
          'endDate2 = "%s",' \
          'rentalReservePrice = "%s",' \
          'rentalArea = "%s",' \
          'rentalPeriod = "%s",' \
          'rentDate = "%s",' \
          'rentFreePeriod = "%s",' \
          'rentPaymentRequest = "%s",' \
          'rentAdjustmentMethod = "%s",' \
          'performanceBondPaymentRequirements = "%s",' \
          'waterElectricityAgreement = "%s",' \
          'rentalUseRequirements = "%s",' \
          'allowRenovation = "%s",' \
          'tenantQualification = "%s" where itemId = ' + itemId
    excute(sql, data)


