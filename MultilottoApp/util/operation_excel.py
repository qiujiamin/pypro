#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import xlrd
from xlutils.copy  import copy
# data = xlrd.open_workbook('../dataconfig/mltest-qjm(2).xlsx')
# tables = data.sheets()[0]
# # 统计总共行数
# print (tables.nrows)
# # 打印二行3列数据
# print(tables.cell_value(1,9))

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        # 传进来的时候就用
        # self.data = self.get_data(file_name,sheet_id)
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
            # self.data = self.get_data(file_name,sheet_id)
        else:
            self.file_name = '../dataconfig/mltest-qjm3.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()
    # 拿出excel数据
    # 获取sheets的内容
    def get_data(self):
        # data = xlrd.open_workbook('../dataconfig/mltest-qjm(2).xlsx')
       data =  xlrd.open_workbook(self.file_name)
        # tables = data.sheets()[0]
       tables = data.sheets()[self.sheet_id]
       return tables
    # 获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    # 获取某个单元格的内容
    def get_cell_value(self,row,col):
        # return self.data.cell_value(row,col)
        return self.data.cell_value(row,col)
#     写入数据
    def write_value(self,row,col,value):
        '''
        写入excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        # xlrd.open_workbook('../dataconfig/mltest.xlsx')
        read_data= xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

#   根据对应的caseid找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data
#     根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()
        # print(cols_data)
        for col_data in cols_data:
            if case_id in col_data:
            # if case_id in cols_data:
                return num
            num = num + 1
        # return num
#     根据行号，找到该行内容
    def get_row_values(self,row):
        tables= self.data
        row_data = tables.row_values(row)
        return row_data
#     获取某列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
           cols = self.data.col_values(col_id)
        else:
            cols =self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    # opers.get_data()
    # print(opers.get_data().nrows)
    # print(opers.get_lines())
    # print(opers.get_cell_value(1,9))
    # print(opers.get_row_num('mm-01'))
    # print(opers.get_row_values(2))
    print(opers.get_rows_data('mm-01'))
    # print(opers.get_cols_data())
    # 当前仅仅拿到数据，最好实例化类的时候就拿到数据。类实例化的时候调用构造函数