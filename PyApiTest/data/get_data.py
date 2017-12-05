# coding=utf-8
from PyApiTest.data import data_config
from PyApiTest.util.operation_excel import OperationExcel
from PyApiTest.util.operation_json import OperationJson


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 获取case总数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取case是否运行的数据
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取URL
    def get_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_request_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 写入执行结果
    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    # 获取返回结果的依赖字段
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depeng())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data
