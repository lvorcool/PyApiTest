# coding=utf-8
from xlutils.copy import copy

import xlrd

'''
xlrd读取excel,
xlwt写入excel
'''


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '/Users/wang/PycharmProjects/PyApiTest/PyApiTest/case/case2.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets的内容,
    def get_data(self):
        # 获取文件并读取有多少行数据
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格有多少行
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据, 写入excel,row,col,value
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseid找到对应行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()
        print("case_id:",case_id)
        for col_data in clols_data:
            try:
                if case_id in col_data:
                    return num
                num += 1
            except Exception as e:
                print(e)

    # 根据行号找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_data().nrows)
    print(opers.get_cell_value(2, 3))
    print(opers.get_lines())
