# str = '''
#     # 最近一个年度审计报告年份
#     obj.__aduitYear = transferorBasicInfo['aduitYear']
#     # 最近一个年度审计报告营业收入
#     obj.__operateIncome = transferorBasicInfo['operateIncome']
#     # 最近一个年度审计报告营业利润
#     obj.__operateProfit = transferorBasicInfo['operateProfit']
#     # 最近一个年度审计报告净利润
#     obj.__netProfit = transferorBasicInfo['netProfit']
#     # 最近一个年度审计报告资产总计
#     obj.__totalAssets = transferorBasicInfo['totalAssets']
#     # 最近一个年度审计报告负债总计
#     obj.__totalLiability = transferorBasicInfo['totalLiability']
#     # 最近一个年度审计机构
#     obj.__auditInstitution = transferorBasicInfo['auditInstitution']
#     # 最近一个月审计日期
#     obj.__recentReportDate = transferorBasicInfo['recentReportDate']
#     # 最近一个月资产总计
#     obj.__recentTotalAssets = transferorBasicInfo['recentTotalAssets']
#     # 最近一个月负债总计
#     obj.__recentTotalLiability = transferorBasicInfo['recentTotalLiability']
#     # 最近一个月所有者权益
#     obj.__recentOwnersEquity = transferorBasicInfo['recentOwnersEquity']
#     # 最近一个月营业收入
#     obj.__recentOperateIncome = transferorBasicInfo['recentOperateIncome']
#     # 最近一个月营业利润
#     obj.__recentOperateProfit = transferorBasicInfo['recentOperateProfit']
#     # 最近一个月填报类型
#     obj.__reportType = transferorBasicInfo['reportType']
#     # 基准日审计机构
#     obj.__benchmarkAuditInstitution = transferorBasicInfo['benchmarkAuditInstitution']
#     # 律师事务所
#     obj.__lawOffice = transferorBasicInfo['lawOffice']
#     # 内部决策文件类型
#     obj.__internalType = transferorBasicInfo['internalType']
#     # 内部决策文件名称及文号
#     obj.__fileAndDocument = transferorBasicInfo['fileAndDocument']
#     # 其他披露事项
#     obj.__otherDisclosures = transferorBasicInfo['otherDisclosures']
#
#     """转让方基本情况
#     """
#     # 转让方名称
#     subjectTransferorLegalBasicInfo = data['subjectTransferorLegalBasicInfoDTOList'][0]
#     obj.__transferorName = subjectTransferorLegalBasicInfo['transferorName']
#     # 转让方住所
#     obj.__residence = subjectTransferorLegalBasicInfo['residence']
#     # 转让方法人
#     obj.__legal = subjectTransferorLegalBasicInfo['legal']
#     # 转让方统一社会信用代码
#     obj.__unifiedSocialCreditCode = subjectTransferorLegalBasicInfo['unifiedSocialCreditCode']
#     # 转让方注册资本
#     obj.__registeredCapital = subjectTransferorLegalBasicInfo['registeredCapital']
#     # 转让方实收资本
#     obj.__paidCapital = subjectTransferorLegalBasicInfo['paidCapital']
#     # 转让方企业类型
#     obj.__enterpriseType = subjectTransferorLegalBasicInfo['enterpriseType']
#     # 转让方所属行业
#     obj.__industry = subjectTransferorLegalBasicInfo['industry']
#     # 转让方经营规模
#     obj.__businessScale = subjectTransferorLegalBasicInfo['businessScale']
#     # 转让方经济性质
#     obj.__economicType = subjectTransferorLegalBasicInfo['economicType']
#     # 转让方持有产（股）权比例（%）
#     obj.__propertyOwnership = subjectTransferorLegalBasicInfo['propertyOwnership']
#     # 转让方拟转让产（股）权比例（%）
#     obj.__transferreProperty = subjectTransferorLegalBasicInfo['transferreProperty']
#     # 产权转让行为决策文件类型
#     obj.__decisionType = subjectTransferorLegalBasicInfo['decisionType']
#     # 产权转让行为决策文件名称及文号
#     obj.__fileAndDocument = subjectTransferorLegalBasicInfo['fileAndDocument']
#     # 产权转让行为监管机构
#     obj.__regulatoryAuthority = subjectTransferorLegalBasicInfo['regulatoryAuthority']
#     # 产权转让行为国家出资企业或主管部门
#     obj.__competentDepartment = subjectTransferorLegalBasicInfo['competentDepartment']
#     # 产权转让行为统一社会信用代码
#     obj.__unifiedSocialCreditCode2 = subjectTransferorLegalBasicInfo['unifiedSocialCreditCode2']
#     # 产权转让行为批准单位
#     obj.__authority = subjectTransferorLegalBasicInfo['authority']
#     # 产权转让行为批准日期
#     obj.__approvalDate = subjectTransferorLegalBasicInfo['approvalDate']
#     # 产权转让行为批准文件类型
#     obj.__approvedFileType = subjectTransferorLegalBasicInfo['approvedFileType']
#     # 产权转让行为批准文件名称及文号
#     obj.__approveFileAndDocument = subjectTransferorLegalBasicInfo['approveFileAndDocument']
#
#     """受让方资格条件
#     """
#     # 受让方资格条件
#     obj.__transfereeQualificate = transferorBasicInfo['transfereeQualificate']
#     # 受让方是否接收联合体受让
#     obj.__isConsortiumTransfer = transferorBasicInfo['isConsortiumTransfer']
#
#     """交易条件
#     """
#     # 标的名称
#     obj.__subjectName = transferorBasicInfo['subjectName']
#     # 转让低价
#     obj.__transferLowPrice = transferorBasicInfo['transferLowPrice']
#     # 付款支付方式
#     obj.__paymentMethod = transferorBasicInfo['paymentMethod']
#     # 分期付款支付要求
#     obj.__installmentPaymentRequest = transferorBasicInfo['installmentPaymentRequest']
#     # 与转让相关的其他条件
#     obj.__otherConditions = transferorBasicInfo['otherConditions']
#     # 是否交纳交易保证金
#     obj.__isPayTradeMargin = transferorBasicInfo['isPayTradeMargin']
#     # 交易保证金交纳金额
#     obj.__amountPaid = transferorBasicInfo['amountPaid']
#     # 交易保证金交纳时间
#     obj.__payTime = transferorBasicInfo['payTime']
#     # 交易保证金处置方式
#     obj.__solveMethod = transferorBasicInfo['solveMethod']
#
#     """信息披露期
#     """
#     # 信息披露期
#     obj.__informationDisclosure = transferorBasicInfo['informationDisclosure']
#     # 信息披露期满，如未征集到意向受让方
#
#     # 公告是否刊登媒体
#     obj.__isPublicationMedia = transferorBasicInfo['isPublicationMedia']
#     # 刊登媒体
#     obj.__publicationMedia = transferorBasicInfo['publicationMedia']
#     # 竞价方式
#     obj.__biddeMethod = transferorBasicInfo['biddeMethod']
#     '''
# str = str.replace('obj', 'self')
# line = str.split('\n')
# tmp = ''
# for i in line:
#     if '=' in i:
#         print(i[0 : i.index('=') + 1] + '\'\'', end='')
#         print(tmp)
#     else:
#         tmp = i