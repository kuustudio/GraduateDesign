import re
from Demo1.config import *

class PurchaseItem():
    item_url = ""

    title = ''

    brief = ''

    time = ''
    buyer = ''
    agent = ''
    bidType = ''
    place = ''

    html_text = ''

    details = ''

    def __init__(self, htmltxt):
        self.html_text = htmltxt


    """
    @brief: 进入每个Item的详细信息网页
    """
    def getDetails(self):
        response = requests.get(self.item_url, headers=headers_purchase)
        if (response.status_code == 200):
            detail_txt = response.content.decode()
        else:
            detail_txt = ''
        self.details = detail_txt

    """
        @:param num代表这个item是本页的第几项
    """
    def analyseItem(self):

        pattern_link_url = '.*?<a\shref="(.*?)".*?</a>'
        self.item_url = re.search(pattern_link_url, self.html_text, re.S).group(1)

        pattern_title = 'blank">(.*?)<font color=red>(.*?)</font>(.*?)</a>'
        self.title = re.search(pattern_title, self.html_text, re.S).group(1).lstrip() + \
              re.search(pattern_title, self.html_text, re.S).group(2) + \
              re.search(pattern_title, self.html_text, re.S).group(3).rstrip()
        pattern_brief = '<p>(.*?)</p>'
        self.brief = re.search(pattern_brief, self.html_text, re.S).group(1)

        pattern_time = '<span>(.*?)\s(.*?)\s'
        self.time = re.search(pattern_time, self.html_text, re.S).group(1) + \
                    " " + \
                    re.search(pattern_time, self.html_text, re.S).group(2)

        pattern_buyer_agent = '\|(.*?)\|(.*?)<br/>'
        self.buyer = re.search(pattern_buyer_agent, self.html_text, re.S).group(1).strip()
        self.agent = re.search(pattern_buyer_agent, self.html_text, re.S).group(2).strip()

        pattern_bidType = '<strong.*?>(.*?)</strong>'
        self.bidType = re.search(pattern_bidType, self.html_text, re.S).group(1).strip()

        pattern_place = '\|\s*<a\shref.*?>(.*?)<'
        self.place = re.search(pattern_place, self.html_text, re.S).group(1).strip()

        self.getDetails()
        print('\t分析每项：' + self.title)