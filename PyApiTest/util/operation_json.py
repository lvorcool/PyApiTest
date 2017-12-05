# coding=utf-8
import json


class OperationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '/Users/wang/PycharmProjects/PyApiTest/PyApiTest/dataconfig/testdata.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path,encoding = "utf8") as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

    # 写json
    def write_data(self, data):
        with open('/Users/wang/PycharmProjects/PyApiTest/PyApiTest/dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('login1'))
