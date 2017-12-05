# coding=utf-8
class global_var:
    # case_id
    case_id = '0'
    url = '1'
    run = '2'
    request_way = '3'
    header = '4'
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    request_data = '8'
    expect = '9'
    result = '10'


# 获取id
def get_id():
    return global_var.case_id


# 获取URL
def get_url():
    return global_var.url


# 获取是否运行
def get_run():
    return global_var.run


# 获取请求数据
def get_run_way():
    return global_var.request_way


# 获取header信息
def get_header():
    return global_var.header


# 获取用例依赖
def get_case_depend():
    return global_var.case_depend


# 获取响应结果的字段依赖
def get_data_depend():
    return global_var.data_depend


# 获取依赖字段的值并传参
def get_field_depeng():
    return global_var.field_depend


# 获取请求数据
def get_request_data():
    return global_var.request_data


# 获取期望结果
def get_expect():
    return global_var.expect


# 获取实际结果
def get_result():
    return global_var.result


# 获取header
def get_header_value(headers):
    return global_var.headers
