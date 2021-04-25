import json

def ZCZR(obj):
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
    #print(len(data['realEstates']))
    subjectMainInfoDTO = data['subjectMainInfoDTO']
    obj.isMortgage = subjectMainInfoDTO['isMortgage'] #标的是否存在抵押情况
    obj.isPriorityPurchase = subjectMainInfoDTO['isPriorityPurchase'] #权利人是否有意向行使优先购买

    if len(data['realEstates']) != 0:
        ###realEstates
        realEstates = data['realEstates'][0]
        obj.subjectName = realEstates['subjectName']  # 标的名称
        obj.location = realEstates['location']  # 房产坐落位置
        obj.useStatus = realEstates['useStatus']  # 房产使用现状
        obj.propertyType = realEstates['propertyType']  # 房产物业类型
        obj.improperPropertyLicenseNumber = realEstates['improperPropertyLicenseNumber']  # 房产不动产权证号
        obj.purpose = realEstates['purpose']  # 房产用途
        obj.commonSituation = realEstates['commonSituation']  # 房产共有情况
        obj.area2 = realEstates['area']  # 房产面积
        obj.natureRights = realEstates['natureRights']  # 房产权利性质
        obj.periodUse = realEstates['periodUse']  # 房产使用期限
        obj.otherDisclosures = realEstates['otherDisclosures']  # 其他披露事项

    elif len(data['ownershipCertificates']) != 0:
        ###ownershipCertificates
        ownershipCertificates = data['ownershipCertificates'][0]
        obj.subjectName = ownershipCertificates['subjectName']  # 标的名称
        obj.location = ownershipCertificates['location']  # 房产坐落位置
        obj.useStatus = ownershipCertificates['useStatus']  # 房产使用现状
        obj.propertyType = ownershipCertificates['propertyType']  # 房产物业类型
        obj.houseOwnershipCertificate = ownershipCertificates['houseOwnershipCertificate'] #房屋所有权证号
        obj.purpose = ownershipCertificates['planPurposes'] #规划用途
        obj.landUseCertificateNumber = ownershipCertificates['landUseCertificateNumber'] #土地使用证号

        obj.commonSituation = ownershipCertificates['commonSituation']  # 房产共有情况
        obj.area2 = ownershipCertificates['constructionArea']  # 房产面积

        obj.useRightType = ownershipCertificates['useRightType']  # 房产使用权类型
        obj.periodUse = ownershipCertificates['endDate']  # 房产使用期限
        obj.rightUseArea = ownershipCertificates['rightUseArea'] # 房产使用权面积
        obj.otherDisclosures = ownershipCertificates['otherDisclosures']  # 其他披露事项

    elif len(data['motorVehicles']) != 0:
        ###motorVehicles
        motorVehicles = data['motorVehicles'][0]
        obj.subjectName = motorVehicles['subjectName']#标的名称
        obj.brandAndModel = motorVehicles['brandAndModel']#品牌型号
        obj.engineNumber = motorVehicles['engineNumber']#发动机编号
        obj.purchaseDate = motorVehicles['purchaseDate']#购置日期
        obj.registrationDate = motorVehicles['registrationDate']#登记日期
        obj.kilometersTraveled = motorVehicles['kilometersTraveled']#行驶公里数
        obj.isIndicators = motorVehicles['isIndicators']#是否带指标
        obj.crossyDeadline = motorVehicles['crossyDeadline']#交强险截止日
        obj.annualValidityPeriod = motorVehicles['annualValidityPeriod']#年检有效期
        obj.location = motorVehicles['location']#所在地
        obj.otherDisclosures = motorVehicles['otherDisclosures']#其他披露

    elif len(data['equipmentSupplies']) != 0:
        ###equipmentSupplies
        equipmentSupplies = data['equipmentSupplies'][0]
        obj.subjectName = equipmentSupplies['subjectName'] #标的名称
        obj.location = equipmentSupplies['location']  # 所在地
        obj.specificationModel = equipmentSupplies['specificationModel'] #规格型号
        obj.unit = equipmentSupplies['unit'] #计量单位
        obj.quantity = equipmentSupplies['quantity'] #数量
        obj.otherDisclosures = equipmentSupplies['otherDisclosures'] #其他披露

    elif len(data['finesMaterials']) != 0:
        finesMaterials = data['finesMaterials'][0]
        obj.subjectName = finesMaterials['subjectName']  # 标的名称
        obj.location = finesMaterials['location']  # 所在地
        obj.model = finesMaterials['model']  # 规格型号
        obj.measurementUnit = finesMaterials['measurementUnit']  # 计量单位
        obj.quantity = finesMaterials['quantity']  # 数量
        obj.otherDisclosures = finesMaterials['otherDisclosures']  # 其他披露

    elif len(data['claims']) != 0:
        claims = data['claims'][0]
        obj.subjectName = claims['subjectName'] # 标的名称
        obj.totalDebtInterest = claims['totalDebtInterest'] # 债权本息合计
        obj.otherDisclosures = claims['otherDisclosures']  # 其他披露
    elif len(data['others']) != 0:
        others = data['others'][0]
        obj.otherContent = others['otherContent'] #标的其他情况

    if data['transferorLegalPersons'] is not None and len(data['transferorLegalPersons']) != 0:
        transferorLegalPersons = data['transferorLegalPersons'][0]
        ###transferorLegalPersons
        obj.transferorName = transferorLegalPersons['transferorName']  # 转让方名称
        obj.residence = transferorLegalPersons['residence']  # 转让方住所
        obj.legal = transferorLegalPersons['legal']  # 转让方法人
        obj.unifiedSocialCreditCode = transferorLegalPersons['unifiedSocialCreditCode']  # 转让方统一社会信用代码
        obj.registeredCapital = transferorLegalPersons['registeredCapital']  # 转让方注册资本
        obj.enterpriseType = transferorLegalPersons['enterpriseType']  # 转让方企业类型
        obj.industry2 = transferorLegalPersons['industry']  # 转让方所属行业
        obj.economicType = transferorLegalPersons['economicType']  # 转让方经济性质
        obj.decisionType = transferorLegalPersons['decisionType']  # 转让方内部决策类型
        obj.fileAndDocument = transferorLegalPersons['fileAndDocument']  # 内部决策文件名称及文号
        obj.competentDepartment = transferorLegalPersons['competentDepartment']  # 转让行为国家出资企业或主管部门
        obj.authority = transferorLegalPersons['authority']  # 产权转让行为批准单位
        obj.approvedFileType = transferorLegalPersons['approvedFileType']  # 产权转让行为批准文件类型
        obj.approveFileAndDocument = transferorLegalPersons['approveFileAndDocument']  # 产权转让行为批准文件名称及文号

    elif data['transferorUnincorporatedSocieties'] is not None and \
            len(data['transferorUnincorporatedSocieties']) != 0:
        ###transferorUnincorporatedSocieties
        transferorUnincorporatedSocieties = data['transferorUnincorporatedSocieties'][0]
        obj.transferorName = transferorUnincorporatedSocieties['transferorName']  # 转让方名称
        obj.residence = transferorUnincorporatedSocieties['mainBusinessSite']  # 转让方经营场所
        obj.leader = transferorUnincorporatedSocieties['leader']  # 转让方负责人
        obj.unifiedSocialCreditCode = transferorUnincorporatedSocieties['unifiedSocialCreditCode']  # 转让方统一社会信用代码
        obj.enterpriseType = transferorUnincorporatedSocieties['enterpriseType']  # 转让方企业类型
        obj.industry = transferorUnincorporatedSocieties['industry']  # 转让方所属行业
        obj.economicType = transferorUnincorporatedSocieties['economicType']  # 转让方经济性质
        obj.decisionType = transferorUnincorporatedSocieties['decisionType']  # 转让方内部决策类型
        obj.fileAndDocument = transferorUnincorporatedSocieties['fileAndDocument']  # 内部决策文件名称及文号
        obj.competentDepartment = transferorUnincorporatedSocieties['competentDepartment']  # 转让行为国家出资企业或主管部门
        obj.authority = transferorUnincorporatedSocieties['authority']  # 产权转让行为批准单位
        obj.approvedFileType = transferorUnincorporatedSocieties['approvedFileType']  # 产权转让行为批准文件类型
        obj.approveFileAndDocument = transferorUnincorporatedSocieties['approveFileAndDocument']  # 产权转让行为批准文件名称及文号

    ###assetTransferBasicInfo
    assetTransferBasicInfo = data['assetTransferBasicInfo']
    obj.transfereeQualificate = assetTransferBasicInfo['transfereeQualification']  # 受让方资格条件
    obj.isAccepteTransferConsortium = assetTransferBasicInfo['isAccepteTransferConsortium']  # 受让方是否接收联合体受让

    obj.subjectName2 = assetTransferBasicInfo['subjectName']  # 标的名称
    obj.transferReservePrice = assetTransferBasicInfo['transferReservePrice']  # 转让低价
    obj.isSetReservePrice = assetTransferBasicInfo['isSetReservePrice']  # 是否设置保留价
    obj.paymentRequest = assetTransferBasicInfo['paymentRequest']  # 付款支付方式
    obj.otherConditions = assetTransferBasicInfo['otherConditions']  # 与转让相关的其他条件

    obj.surveyContact = assetTransferBasicInfo['surveyContact']  # 踏勘安排

    obj.isPayTradingMargin = assetTransferBasicInfo['isPayTradingMargin']  # 是否交纳交易保证金
    obj.amountPaid = assetTransferBasicInfo['amountPaid']  # 交易保证金交纳金额
    obj.payTime = assetTransferBasicInfo['payTime']  # 交易保证金交纳时间
    obj.solveMethod = assetTransferBasicInfo['solveMethod']  # 交易保证金处置方式

    obj.informationDisclosure = assetTransferBasicInfo['informationDisclosure']  # 信息披露期
    obj.isPublicationMedia = assetTransferBasicInfo['isPublicationMedia']  # 公告是否刊登媒体
    obj.publicationMedia = assetTransferBasicInfo['publicationMedia']  # 刊登媒体
    obj.biddeMethod = assetTransferBasicInfo['biddeMethod']  # 竞价方式
