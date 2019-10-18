#!/usr/bin/env python
import threading
import time
import urllib.request
import ssl
import json
class ioscomments():
    def __init__(self,country,productid,star):
        self.country=str(country)
        self.page = 1
        self.productid=str(productid)
        self.star = star
        self.items = []
        self.stop = False

    # 设置集合
    def set(self,author="",version="",star="",title="",content=""):
        item = {"author":author,"version":version,"star":star,"title":title,"content":content}
        self.items.append(item)

    # 获取数据
    def get(self):
        if self.items:
            return self.items.pop(0)
        elif self.stop == False:
            return 0
        else:
            self.stop = False
            return -1

    def run(self):
        url = 'https://itunes.apple.com/' + self.country + '/rss/customerreviews/page=' + str(self.page) + '/id=' + self.productid + '/sortby=mostrecent/json'
        header = {
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1"
        }
        context = ssl._create_unverified_context()
        request = urllib.request.Request(url, headers=header)
        try:
            res = urllib.request.urlopen(request, context=context)
            result = res.read().decode("utf8")

            # self.dell(result)
            th1 = threading.Thread(target=ioscomments.dell ,args=(self,result))
            th1.start()
            th1.join()
            time.sleep(1)
            self.page = self.page + 1
            self.run()

        except Exception as e:
            self.stop = True
            print(e)
            return

    def dell(self,result):
        try:
            result = json.loads(result,encoding='utf-8')
            if result['feed']['entry']:
                for entry in result['feed']['entry']:
                    author  = entry['author']['name']['label']
                    version = entry['im:version']['label']
                    star    = entry['im:rating']['label']
                    title   = entry['title']['label']
                    content = entry['content']['label']
                    self.set(author,version,star,title,content)
        except Exception as e:
            print(e)
