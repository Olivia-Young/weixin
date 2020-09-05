# 2020年8月29日
# 本次目标利用搜狗微信网站，进行指定公众号文章最新内容爬取。
# 以便后期调用分析。主要构思是写一个通用的类，然后将自己需要的功能方法再单独分装起来

import requests
from urllib.parse import quote
from pyquery import PyQuery as pq
import time

class Wechat(object):
    def __init__(self,name):
        self.name = name
    # 该函数获取结果页面内容
    def get_page(self,page):
        s = quote(self.name)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        }
        url = 'https://weixin.sogou.com/weixin?type=2&page={}&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_='.format(page,s)
        a = requests.get(url,headers=headers)

        return a.text

    # 找出对应公众号的文章链接和标题，因为搜狗微信只显示前10页，所以我们也只抓取前10页，找出两天类的文章并输出
    def get_article(self):
        for i in range(1,11):
            q = pq(self.get_page(i))
            lists = q('.news-list li').items()
            for list in lists:
                if list('.s-p a').text() == self.name:

                    # 获取文章的时间戳
                    t = list('.s-p').attr('t')
                    # 这里是计算当前的时间戳
                    shijian = int(time.time())
                    # 这里是将两天内的文章搜索出来,并返回

                    if (shijian - int(t)) < 172800:
                        d = list('.txt-box h3 a ').text()  # 获取文章标题
                        s = 'https://weixin.sogou.com' + list('.txt-box h3 a ').attr('href')  # 获取文章链接
                        print('%s%s'%(d,s))


    # 上面函数已经拿到文章的名字和文章链接，现在来进行文章内容分析，









h = Wechat('西安腾乐电子')

h.get_article()

