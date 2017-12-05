# coding=utf-8
import requests
import json


class RunMain:
    # 类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    # def __init__(self, url, method, data):
    #     self.res = self.run_main(url, method, data)

    # self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    def send_get(self, url, data):
        res = requests.get(url=url, data=data)
        return json.dumps(res)

    def send_post(self, url, json):
        res = requests.post(url=url, json=json).json()
        return res

    def run_main(self, url, method, data):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

