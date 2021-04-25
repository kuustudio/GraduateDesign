import json

def CQZR(obj):
    obj.createDate = obj.info['createDate']  # 信息披露创建时间
    obj.itemId = obj.info['subjectId']  # 标的Id，用于构造Url
    obj.name = obj.info['subjectName']  # 标的名称
    obj.number = obj.info['subjectNum']  # 标的编号
    obj.startDate = obj.info['disclosureStartDate']  # 信息披露起始时间
    obj.endDate = obj.info['disclosureEndDate']  # 信息披露截至时间
    obj.area = obj.info['subjectCompanyArea']  # 标的企业所在地区
    obj.industry = obj.info['subjectCompanyIndustry']  # 标的企业所属行业
    obj.reservePrice = obj.info['transferReservePrice']  # 转让底价
    obj.contactInfo = obj.info['contactInfo']  # 联系人及电话
    obj.transferCommitment = obj.info['transferorCommitment']  # 转让申请与承诺

    linkInfoUrl = 'https://www.hzaee.com/api/api/subjectmaininfo/' + obj.itemId
    txt = obj.htmlFetcher.get_html(linkInfoUrl, 1, useProxy=False)
    json1 = json.loads(txt)
    assert json1['msg'] == 'success'
    data = json1['data']
    transferorBasicInfo = data['subjectTransferorBasicInfoDTO']

    """转让标的基本情况
    """
    # 标的企业的企业名称
    obj.subjectCompanyName = transferorBasicInfo['subjectCompanyName']
    # 标的企业的企业住所
    obj.residence = transferorBasicInfo['residence']
    # 标的企业的企业法人
    obj.legalPerson = transferorBasicInfo['legalPerson']
    # 标的企业的成立日期
    obj.establishDate = transferorBasicInfo['establishDate']
    # 标的企业的注册资本
    obj.registeredCapital = transferorBasicInfo['registeredCapital']
    # 标的企业的实缴资本
    obj.paidCapital = transferorBasicInfo['paidCapital']
    # 标的企业的企业类型
    obj.companyType = transferorBasicInfo['companyType']
    # 标的企业的所属行业
    obj.industry2 = transferorBasicInfo['industry']
    # 标的企业的职工人数
    obj.employeNum = transferorBasicInfo['employeNum']
    # 标的企业的统一社会信用代码
    obj.unifiedSocialCreditCode = transferorBasicInfo['unifiedSocialCreditCode']
    # 标的企业的经营规模
    obj.businessScale = transferorBasicInfo['businessScale']
    # 标的企业是否含有国有划拨土地
    obj.isAllocateLand = transferorBasicInfo['isAllocateLand']
    # 标的企业的经济性质
    obj.economicNature = transferorBasicInfo['economicNature']
    # 标的企业的经营范围
    obj.businessScope = transferorBasicInfo['businessScope']
    # 标的企业的其他股东是否放弃优先购买权
    obj.isPreemptiveRight = transferorBasicInfo['isPreemptiveRight']
    # 标的企业的企业管理层是否参与受让
    obj.isParticipateTransfer = transferorBasicInfo['isParticipateTransfer']
    # 标的企业是否涉及职工安置
    obj.isStaffPlacement = transferorBasicInfo['isStaffPlacement']
    # 标是否导致标的企业的实际控制权发生转移
    obj.isTransferControl = transferorBasicInfo['isTransferControl']
    # 标的企业前十位股东名称
    obj.top10Shareholder.append(
        (transferorBasicInfo['shareholder'],
         transferorBasicInfo['holdRatio'] + '%'))
    # 标的企业前十位股东持有比例
    for i in range(2, 11):
        tag1 = 'shareholder' + str(i)
        tag2 = 'holdRatio' + str(i)
        if transferorBasicInfo[tag1] != '':
            obj.top10Shareholder.append(
                (transferorBasicInfo[tag1],
                 transferorBasicInfo[tag2] + '%'))
        else:
            break
    # 最近一个年度审计报告年份
    obj.aduitYear = transferorBasicInfo['aduitYear']
    # 最近一个年度审计报告营业收入
    obj.operateIncome = transferorBasicInfo['operateIncome']
    # 最近一个年度审计报告营业利润
    obj.operateProfit = transferorBasicInfo['operateProfit']
    # 最近一个年度审计报告净利润
    obj.netProfit = transferorBasicInfo['netProfit']
    # 最近一个年度审计报告资产总计
    obj.totalAssets = transferorBasicInfo['totalAssets']
    # 最近一个年度审计报告负债总计
    obj.totalLiability = transferorBasicInfo['totalLiability']
    # 最近一个年度审计机构
    obj.auditInstitution = transferorBasicInfo['auditInstitution']
    # 最近一个月审计日期
    obj.recentReportDate = transferorBasicInfo['recentReportDate']
    # 最近一个月资产总计
    obj.recentTotalAssets = transferorBasicInfo['recentTotalAssets']
    # 最近一个月负债总计
    obj.recentTotalLiability = transferorBasicInfo['recentTotalLiability']
    # 最近一个月所有者权益
    obj.recentOwnersEquity = transferorBasicInfo['recentOwnersEquity']
    # 最近一个月营业收入
    obj.recentOperateIncome = transferorBasicInfo['recentOperateIncome']
    # 最近一个月营业利润
    obj.recentOperateProfit = transferorBasicInfo['recentOperateProfit']
    # 最近一个月填报类型
    obj.reportType = transferorBasicInfo['reportType']
    # 基准日审计机构
    obj.benchmarkAuditInstitution = transferorBasicInfo['benchmarkAuditInstitution']
    # 律师事务所
    obj.lawOffice = transferorBasicInfo['lawOffice']
    # 内部决策文件类型
    obj.internalType = transferorBasicInfo['internalType']
    # 内部决策文件名称及文号
    obj.fileAndDocument = transferorBasicInfo['fileAndDocument']
    # 其他披露事项
    obj.otherDisclosures = transferorBasicInfo['otherDisclosures']

    """转让方基本情况
    """
    if len(data['subjectTransferorLegalBasicInfoDTOList']) == 0:
        assert len(data['subjectTransferorNotLegalBasicInfoDTOList']) > 0
        subjectTransferorNotLegalBasicInfoDTOList = \
            data['subjectTransferorNotLegalBasicInfoDTOList']
        subjectTransferorNotLegalBasicInfoDTOList = data['subjectTransferorNotLegalBasicInfoDTOList'][0]
        # 转让方名称
        obj.transferorName = subjectTransferorNotLegalBasicInfoDTOList['transferorName']
        # 转让方主要经营场所
        obj.residence2 = subjectTransferorNotLegalBasicInfoDTOList['mainBusinesPremise']
        # 转让方执行事务合伙人
        obj.legal = subjectTransferorNotLegalBasicInfoDTOList['principal']
        # 转让方统一社会信用代码
        obj.unifiedSocialCreditCode2 = subjectTransferorNotLegalBasicInfoDTOList['unifiedSocialCreditCode']
        # 转让方企业类型
        obj.enterpriseType = subjectTransferorNotLegalBasicInfoDTOList['enterpriseType']
        # 转让方所属行业
        obj.industry3 = subjectTransferorNotLegalBasicInfoDTOList['industry']

        # 转让方经济性质
        obj.economicType = subjectTransferorNotLegalBasicInfoDTOList['economicType']
        # 转让方持有产（股）权比例（%）
        obj.propertyOwnership = subjectTransferorNotLegalBasicInfoDTOList['propertyOwnership']
        # 转让方拟转让产（股）权比例（%）
        obj.transferreProperty = subjectTransferorNotLegalBasicInfoDTOList['transferreProperty']
        # 产权转让行为决策文件类型
        obj.decisionType = subjectTransferorNotLegalBasicInfoDTOList['decisionType']
        # 产权转让行为决策文件名称及文号
        obj.fileAndDocument2 = subjectTransferorNotLegalBasicInfoDTOList['fileAndDocument']
        # 产权转让行为监管机构
        obj.regulatoryAuthority = subjectTransferorNotLegalBasicInfoDTOList['regulatoryAuthority']
        # 产权转让行为国家出资企业或主管部门
        obj.competentDepartment = subjectTransferorNotLegalBasicInfoDTOList['competentDepartment']
        # 产权转让行为统一社会信用代码
        obj.unifiedSocialCreditCode3 = subjectTransferorNotLegalBasicInfoDTOList['unifiedSocialCreditCode2']
        # 产权转让行为批准单位
        obj.authority = subjectTransferorNotLegalBasicInfoDTOList['authority']
        # 产权转让行为批准日期
        obj.approvalDate = subjectTransferorNotLegalBasicInfoDTOList['approvalDate']
        # 产权转让行为批准文件类型
        obj.approvedFileType = subjectTransferorNotLegalBasicInfoDTOList['approvedFileType']
        # 产权转让行为批准文件名称及文号
        obj.approveFileAndDocument = subjectTransferorNotLegalBasicInfoDTOList['approveFileAndDocument']

    elif len(data['subjectTransferorLegalBasicInfoDTOList']) == 1:
        subjectTransferorLegalBasicInfo = data['subjectTransferorLegalBasicInfoDTOList'][0]
        # 转让方名称
        obj.transferorName = subjectTransferorLegalBasicInfo['transferorName']
        # 转让方住所
        obj.residence2 = subjectTransferorLegalBasicInfo['residence']
        # 转让方法人
        obj.legal = subjectTransferorLegalBasicInfo['legal']
        # 转让方统一社会信用代码
        obj.unifiedSocialCreditCode2 = subjectTransferorLegalBasicInfo['unifiedSocialCreditCode']
        # 转让方注册资本
        obj.registeredCapital2 = subjectTransferorLegalBasicInfo['registeredCapital']
        # 转让方实收资本
        obj.paidCapital2 = subjectTransferorLegalBasicInfo['paidCapital']
        # 转让方企业类型
        obj.enterpriseType = subjectTransferorLegalBasicInfo['enterpriseType']
        # 转让方所属行业
        obj.industry3 = subjectTransferorLegalBasicInfo['industry']
        # 转让方经营规模
        obj.businessScale2 = subjectTransferorLegalBasicInfo['businessScale']
        # 转让方经济性质
        obj.economicType = subjectTransferorLegalBasicInfo['economicType']
        # 转让方持有产（股）权比例（%）
        obj.propertyOwnership = subjectTransferorLegalBasicInfo['propertyOwnership']
        # 转让方拟转让产（股）权比例（%）
        obj.transferreProperty = subjectTransferorLegalBasicInfo['transferreProperty']
        # 产权转让行为决策文件类型
        obj.decisionType = subjectTransferorLegalBasicInfo['decisionType']
        # 产权转让行为决策文件名称及文号
        obj.fileAndDocument2 = subjectTransferorLegalBasicInfo['fileAndDocument']
        # 产权转让行为监管机构
        obj.regulatoryAuthority = subjectTransferorLegalBasicInfo['regulatoryAuthority']
        # 产权转让行为国家出资企业或主管部门
        obj.competentDepartment = subjectTransferorLegalBasicInfo['competentDepartment']
        # 产权转让行为统一社会信用代码
        obj.unifiedSocialCreditCode3 = subjectTransferorLegalBasicInfo['unifiedSocialCreditCode2']
        # 产权转让行为批准单位
        obj.authority = subjectTransferorLegalBasicInfo['authority']
        # 产权转让行为批准日期
        obj.approvalDate = subjectTransferorLegalBasicInfo['approvalDate']
        # 产权转让行为批准文件类型
        obj.approvedFileType = subjectTransferorLegalBasicInfo['approvedFileType']
        # 产权转让行为批准文件名称及文号
        obj.approveFileAndDocument = subjectTransferorLegalBasicInfo['approveFileAndDocument']
    else:
        # 转让方名称
        obj.transferorName = []
        # 转让方住所
        obj.residence2 = []
        # 转让方法人
        obj.legal = []
        # 转让方统一社会信用代码
        obj.unifiedSocialCreditCode2 = []
        # 转让方注册资本
        obj.registeredCapital2 = []
        # 转让方实收资本
        obj.paidCapital2 = []
        # 转让方企业类型
        obj.enterpriseType = []
        # 转让方所属行业
        obj.industry3 = []
        # 转让方经营规模
        obj.businessScale2 = []
        # 转让方经济性质
        obj.economicType = []
        # 转让方持有产（股）权比例（%）
        obj.propertyOwnership = []
        # 转让方拟转让产（股）权比例（%）
        obj.transferreProperty = []
        # 产权转让行为决策文件类型
        obj.decisionType = []
        # 产权转让行为决策文件名称及文号
        obj.fileAndDocument2 = []
        # 产权转让行为监管机构
        obj.regulatoryAuthority = []
        # 产权转让行为国家出资企业或主管部门
        obj.competentDepartment = []
        # 产权转让行为统一社会信用代码
        obj.unifiedSocialCreditCode3 = []
        # 产权转让行为批准单位
        obj.authority = []
        # 产权转让行为批准日期
        obj.approvalDate = []
        # 产权转让行为批准文件类型
        obj.approvedFileType = []
        # 产权转让行为批准文件名称及文号
        obj.approveFileAndDocument = []
        for subjectTransferorLegalBasicInfo in data['subjectTransferorLegalBasicInfoDTOList']:
            # 转让方名称
            obj.transferorName.append(subjectTransferorLegalBasicInfo['transferorName'])
            # 转让方住所
            obj.residence2.append(subjectTransferorLegalBasicInfo['residence'])
            # 转让方法人
            obj.legal.append(subjectTransferorLegalBasicInfo['legal'])
            # 转让方统一社会信用代码
            obj.unifiedSocialCreditCode2.append(subjectTransferorLegalBasicInfo['unifiedSocialCreditCode'])
            # 转让方注册资本
            obj.registeredCapital2.append(subjectTransferorLegalBasicInfo['registeredCapital'])
            # 转让方实收资本
            obj.paidCapital2.append(subjectTransferorLegalBasicInfo['paidCapital'])
            # 转让方企业类型
            obj.enterpriseType.append(subjectTransferorLegalBasicInfo['enterpriseType'])
            # 转让方所属行业
            obj.industry3.append(subjectTransferorLegalBasicInfo['industry'])
            # 转让方经营规模
            obj.businessScale2.append(subjectTransferorLegalBasicInfo['businessScale'])
            # 转让方经济性质
            obj.economicType.append(subjectTransferorLegalBasicInfo['economicType'])
            # 转让方持有产（股）权比例（%）
            obj.propertyOwnership.append(subjectTransferorLegalBasicInfo['propertyOwnership'])
            # 转让方拟转让产（股）权比例（%）
            obj.transferreProperty.append(subjectTransferorLegalBasicInfo['transferreProperty'])
            # 产权转让行为决策文件类型
            obj.decisionType.append(subjectTransferorLegalBasicInfo['decisionType'])
            # 产权转让行为决策文件名称及文号
            obj.fileAndDocument2.append(subjectTransferorLegalBasicInfo['fileAndDocument'])
            # 产权转让行为监管机构
            obj.regulatoryAuthority.append(subjectTransferorLegalBasicInfo['regulatoryAuthority'])
            # 产权转让行为国家出资企业或主管部门
            obj.competentDepartment.append(subjectTransferorLegalBasicInfo['competentDepartment'])
            # 产权转让行为统一社会信用代码
            obj.unifiedSocialCreditCode3.append(subjectTransferorLegalBasicInfo['unifiedSocialCreditCode2'])
            # 产权转让行为批准单位
            obj.authority.append(subjectTransferorLegalBasicInfo['authority'])
            # 产权转让行为批准日期
            obj.approvalDate.append(subjectTransferorLegalBasicInfo['approvalDate'])
            # 产权转让行为批准文件类型
            obj.approvedFileType.append(subjectTransferorLegalBasicInfo['approvedFileType'])
            # 产权转让行为批准文件名称及文号
            obj.approveFileAndDocument.append(subjectTransferorLegalBasicInfo['approveFileAndDocument'])

    """受让方资格条件
    """
    # 受让方资格条件
    obj.transfereeQualificate = transferorBasicInfo['transfereeQualificate']
    # 受让方是否接收联合体受让
    obj.isConsortiumTransfer = transferorBasicInfo['isConsortiumTransfer']

    """交易条件
    """
    # 标的名称
    obj.subjectName = transferorBasicInfo['subjectName']
    # 转让低价
    obj.transferLowPrice = transferorBasicInfo['transferLowPrice']
    # 付款支付方式
    obj.paymentMethod = transferorBasicInfo['paymentMethod']
    # 分期付款支付要求
    obj.installmentPaymentRequest = transferorBasicInfo['installmentPaymentRequest']
    # 与转让相关的其他条件
    obj.otherConditions = transferorBasicInfo['otherConditions']
    # 是否交纳交易保证金
    obj.isPayTradeMargin = transferorBasicInfo['isPayTradeMargin']
    # 交易保证金交纳金额
    obj.amountPaid = transferorBasicInfo['amountPaid']
    # 交易保证金交纳时间
    obj.payTime = transferorBasicInfo['payTime']
    # 交易保证金处置方式
    obj.solveMethod = transferorBasicInfo['solveMethod']

    """信息披露期
    """
    # 信息披露期
    obj.informationDisclosure = transferorBasicInfo['informationDisclosure']
    # 信息披露期满，如未征集到意向受让方

    # 公告是否刊登媒体
    obj.isPublicationMedia = transferorBasicInfo['isPublicationMedia']
    # 刊登媒体
    obj.publicationMedia = transferorBasicInfo['publicationMedia']
    # 竞价方式
    obj.biddeMethod = transferorBasicInfo['biddeMethod']

    #print(json1)