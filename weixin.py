# 2020年8月29日
# 本次目标利用搜狗微信网站，进行指定公众号文章最新内容爬取。
# 以便后期调用分析。主要构思是写一个通用的类，然后将自己需要的功能方法再单独分装起来

import requests
from urllib.parse import quote
from pyquery import PyQuery as pq

class Wechat(object):
    def __init__(self,name):
        self.name = name
    # 该函数获取结果页面内容
    def get_page(self):
        s = quote(self.name)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400',
        }
        url = 'https://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_='.format(s)
        a = requests.get(url,headers=headers)

        return a.text

    # 找出对应名字的文章链接和标题
    def get_article(self,html):
        q = pq(html)
        lists = q('.news-list li').items()
        for list in lists:
            if list('.s-p a').text() == self.name:
                print(list)





h = Wechat('Victory九幽')
c = h.get_page()
h.get_article(c)