from Demo1.TYCSpider.Verification.Chaojiying import Chaojiying_Client
from Demo1.TYCSpider.Verification.verificationSettings import *
from Demo1.config import *
import Demo1.config as config
from selenium import webdriver
from selenium.webdriver import ActionChains
import base64
import random

class TYCVerifier():
    def __init__(self):
        self.__chaojiying = Chaojiying_Client(CJY_USERNAME, CJY_PASSWORD, CJY_SOFT_ID)
        self.__cookies = config.Cookie_init_tyc_list
        for cookie in self.__cookies:
            if "sameSite" in cookie.keys():
                del cookie['sameSite']

        self.__url_domain = 'https://www.tianyancha.com/'

    def __open(self, url):
        self.__browser = webdriver.Chrome()
        self.__browser.get(self.__url_domain)
        for cookie in self.__cookies:
            self.__browser.add_cookie(cookie)

        self.__browser.get(url)

    def __bannedForVerify(self, url):
        self.__open(url)
        if ('antirobot' in self.__browser.current_url):
            return True
        return False

    """
        @brief:刷新Verifier中的Cookie，同时也更新全局Cookie
    """
    def __refreshCookie(self):
        self.__cookies = self.__browser.get_cookies()

        for dict_new in self.__cookies:
            for dict_old in config.Cookie_init_tyc_list:
                if dict_new['name'] == dict_old['name'] and \
                        dict_new['value'].lower() != dict_old['value'].lower():
                    print('=========================================')
                    print(dict_old)
                    dict_old['value'] = dict_new['value']
                    print('刷新为')
                    print(dict_old)
                    print('=========================================')

        for cookie in config.Cookie_init_tyc_list:
            if "sameSite" in cookie.keys():
                del cookie['sameSite']
        self.__cookies = config.Cookie_init_tyc_list

        config.cookieSetter.changed(config.Cookie_init_tyc_list)
        global Cookie_init_tyc
        Cookie_init_tyc = config.cookieSetter.strCookie

        self.__browser.close()

    """
        @brief:完成验证动作
    """
    def verify(self, url, failFlag = False, count = 1):
        if failFlag == False:
            if not self.__bannedForVerify(url):
                print('没有被验证码禁！', url)
                self.__browser.close()
                return False

        print('网页：', url, '开始进行验证码验证')
        print('验证url为：', self.__browser.current_url)

        self.__browser.fullscreen_window()

        if 'anti' not in self.__browser.current_url:
            print('验证完成！', '跳转到：', self.__browser.current_url)
            self.__refreshCookie()
            return True

        try:
            img_verify = self.__browser.find_element_by_xpath('//div[@class="new-box94"]')
            img_b64 = img_verify.screenshot_as_base64
            img_bytes = base64.b64decode(img_b64)
        except:
            print('验证完成！', '跳转到：', self.__browser.current_url)
            self.__refreshCookie()
            return True

        response = self.__chaojiying.PostPic(img_bytes, IMG_TYPE_GETPOSITION)
        positions = response['pic_str'].split('|')
        actions = ActionChains(self.__browser)

        for i in positions:
            posi = i.split(',')
            x = int(posi[0])
            y = int(posi[1])
            actions.move_to_element_with_offset(img_verify, x, y).click().perform()
            # time.sleep(random.random())

        button = self.__browser.find_element_by_xpath('//div[@id="submitie"]')
        button.click()

        time.sleep(1)

        if 'anti' not in self.__browser.current_url:
            print('验证完成！', '跳转到：', self.__browser.current_url)
            self.__refreshCookie()
            return True
        else:
            if count >= 3:
                print('验证失败！')
                self.__browser.close()
                return False
            else:
                print('重新验证！')
                self.__browser.refresh()
                return self.verify(url, failFlag = True, count = count + 1)

# if __name__ == '__main__':
#     tycVerifier = TYCVerifier()
#     url = 'https://www.tianyancha.com/search/oc44/p2?base=szh&areaCode=320583'
#     print(tycVerifier.verify(url))
tycVerifier = TYCVerifier()