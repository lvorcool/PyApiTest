# coding=utf-8
import json
from PyApiTest.base.runmethod import RunMethod
from PyApiTest.data.dependent_data import DependdentData
from PyApiTest.data.get_data import GetData
from PyApiTest.util.common_util import CommonUtil
from PyApiTest.util.operation_json import OperationJson
from PyApiTest.util.operationheader import OperationHeader


class RunTestCase:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    # 程序执行入口
    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                expect = self.data.get_expcet_data(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #   获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #    获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data

                if header == 'write':
                    res = json.loads(self.run_method.run_main(method,url,request_data))
                    op_header = OperationHeader(res)
                    op_header.write_token()

                elif header == 'yes':
                    op_json = OperationJson("/Users/wang/PycharmProjects/PyApiTest/PyApiTest/dataconfig/cookie.json")
                    cookie = op_json.get_data('token')
                    headers = {
                        'X-XSRF-TOKEN':cookie
                    }
                    res = self.run_method.run_main(method,url,request_data,headers)
                else:
                    res = self.run_method.run_main(method,url,request_data)

                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, 'fail')
                    fail_count.append(i)
        print(len(pass_count))
        print(len(fail_count))


if __name__ == '__main__':
    run = RunTestCase()
    res = run.go_on_run()
