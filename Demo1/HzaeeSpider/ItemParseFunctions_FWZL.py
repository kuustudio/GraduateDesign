import json

def FWZL(obj):
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

    subjectRealtorImmovableBasicInfoDTOList = data['subjectRealtorImmovableBasicInfoDTOList']
    if len(subjectRealtorImmovableBasicInfoDTOList) > 0:
        obj.houseName = []
        obj.location = []
        obj.useStatus = []
        obj.propertyType = []
        obj.improperPropertyLicenseNumber = []
        obj.umber = []
        obj.purpose = []
        obj.commonSituation = []
        obj.area = []
        obj.natureRights = []
        obj.periodUse = []
        for building in subjectRealtorImmovableBasicInfoDTOList:
            obj.houseName.append(building['houseName'])  # 房屋名称
            obj.location.append(building['location'])  # 坐落位置
            obj.useStatus.append(building['useStatus'])  # 使用现状
            obj.propertyType.append(building['propertyType'])  # 物业类型
            obj.improperPropertyLicenseNumber.append(
                building['improperPropertyLicenseNumber'])  # 不动产权证号
            obj.purpose.append(building['purpose'])  # 用途
            obj.commonSituation.append(building['commonSituation'])  # 共有情况
            obj.area.append(building['area'])  # 面积
            obj.natureRights.append(building['natureRights'])  # 权利性质
            obj.periodUse.append(building['periodUse'])  # 使用期限

        obj.otherDisclosures = ''  # 其他披露事项

    elif len(data['subjectRealtorOwnershipBasicInfoDTOList']) > 0:
        subjectRealtorOwnershipBasicInfoDTOList = data['subjectRealtorOwnershipBasicInfoDTOList'][0]
        obj.houseName = subjectRealtorOwnershipBasicInfoDTOList['houseName']  # 房屋名称
        obj.location = subjectRealtorOwnershipBasicInfoDTOList['location']  # 房屋坐落
        obj.useStatus = subjectRealtorOwnershipBasicInfoDTOList['useStatus']  # 使用现状
        obj.propertyType = subjectRealtorOwnershipBasicInfoDTOList['propertyType']  # 物业类型
        obj.houseOwnershipCertificate = subjectRealtorOwnershipBasicInfoDTOList['houseOwnershipCertificate']  # 房屋所有权证号
        obj.commonSituation = subjectRealtorOwnershipBasicInfoDTOList['commonSituation']  # 共有情况
        obj.planPurposes = subjectRealtorOwnershipBasicInfoDTOList['planPurposes']  # 规划用途
        obj.propertyNature = subjectRealtorOwnershipBasicInfoDTOList['propertyNature']  # 房屋性质
        obj.constructionArea = subjectRealtorOwnershipBasicInfoDTOList['constructionArea']  # 建筑面积
        obj.landUseCertificateNumber = subjectRealtorOwnershipBasicInfoDTOList['landUseCertificateNumber']  # 土地使用证号
        obj.gentle = subjectRealtorOwnershipBasicInfoDTOList['gentle']  # 地类（用途）
        obj.useRightType = subjectRealtorOwnershipBasicInfoDTOList['useRightType']  # 使用权类型
        obj.endDate = subjectRealtorOwnershipBasicInfoDTOList['endDate']  # 终止日期
        obj.rightUseArea = subjectRealtorOwnershipBasicInfoDTOList['rightUseArea']  # 使用权面积

        obj.otherDisclosures = ''  # 其他披露事项

    subjectRealtorBasicInfoDTO = data['subjectRealtorBasicInfoDTO']
    obj.rentalReservePrice = subjectRealtorBasicInfoDTO['rentalReservePrice']  # 出租底价
    obj.rentalArea = subjectRealtorBasicInfoDTO['rentalArea']  # 出租面积
    obj.rentalPeriod = subjectRealtorBasicInfoDTO['rentalPeriod']  # 出租期限
    obj.rentDate = subjectRealtorBasicInfoDTO['rentDate']  # 起租日
    obj.rentFreePeriod = subjectRealtorBasicInfoDTO['rentFreePeriod']  # 免租期
    obj.rentPaymentRequest = subjectRealtorBasicInfoDTO['rentPaymentRequest']  # 租金支付条件
    obj.rentAdjustmentMethod = subjectRealtorBasicInfoDTO['rentAdjustmentMethod']  # 租金调整方式
    obj.performanceBondPaymentRequirements = subjectRealtorBasicInfoDTO[
        'performanceBondPaymentRequirements']  # 履约保证金支付要求
    obj.waterElectricityAgreement = subjectRealtorBasicInfoDTO['waterElectricityAgreement']  # 水电气物业费等费用的约定
    obj.rentalUseRequirements = subjectRealtorBasicInfoDTO['rentalUseRequirements']  # 出租用途要求
    obj.allowRenovation = subjectRealtorBasicInfoDTO['allowRenovation']  # 是否允许装修改造
    obj.otherConditions = subjectRealtorBasicInfoDTO['otherConditions']  # 与出租相关的其他条件
    obj.tenantQualification = subjectRealtorBasicInfoDTO['tenantQualification']  # 承租方资格条件
    obj.surveyContact = subjectRealtorBasicInfoDTO['surveyContact']  # 踏勘安排
    obj.isPayTradingMargin = subjectRealtorBasicInfoDTO['isPayTradingMargin']  # 交纳交易保证金
    obj.amountPaid = subjectRealtorBasicInfoDTO['amountPaid']  # 交纳金额
    obj.payTime = subjectRealtorBasicInfoDTO['payTime']  # 交纳时间
    obj.solveMethod = subjectRealtorBasicInfoDTO['solveMethod']  # 处置方式

    obj.informationDisclosure = subjectRealtorBasicInfoDTO['informationDisclosure']  # 信息披露期
    obj.isPublicationMedia = subjectRealtorBasicInfoDTO['isPublicationMedia']  # 公告是否刊登媒体
    obj.publicationMedia = subjectRealtorBasicInfoDTO['publicationMedia']  # 刊登媒体

    obj.biddeMethod = subjectRealtorBasicInfoDTO['biddeMethod']  # 竞价方式


