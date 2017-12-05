# coding=utf-8
import pickle

import requests
import json
from requests import utils

from PyApiTest.util.operation_json import OperationJson


class OperationHeader:
    def __init__(self,response):
        self.response = response

    def get_response_token(self):
        #获取登录返回的返回结果,其中有token值
        res = self.response
        return res

    def write_token(self):
        # 把cookie值写入cookie.json文件中
        token = self.get_response_token()
        op_json = OperationJson()
        op_json.write_data(token)


