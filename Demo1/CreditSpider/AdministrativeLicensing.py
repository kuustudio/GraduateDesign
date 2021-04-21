"""
    行政许可
"""
class AdminLicense():
    def __init__(self, adminLicenseInfo):
        assert type(adminLicenseInfo).__name__ == 'dict'
        entity = adminLicenseInfo['entity']

        self.__wsh = entity['xk_wsh']  # 行政许可决定文书号
        self.__xkws = entity['xk_xkws']  # 行政许可决定文书名称
        self.__xkzs = entity['xk_xkzs']  # 许可证书名称
        self.__xklb = entity['xk_xklb']  # 许可类别
        self.__xkbh = entity['xk_xkbh']  # 许可编号
        self.__jdrq = entity['xk_jdrq']  # 许可决定日期
        self.__yxqz = entity['xk_yxqz']  # 有效期自
        self.__yxqzi = entity['xk_yxqzi']  # 有效期至
        self.__nr = entity['xk_nr']  # 许可内容
        self.__xkjg = entity['xk_xkjg']  # 许可机关
        self.__xkjgdm = entity['xk_xkjgdm']  # 许可机关统一社会信用代码
        self.__lydw = entity['xk_lydw']  # 数据来源单位
        self.__lydwdm = entity['xk_lydwdm']  # 数据来源单位统一社会信用代码
