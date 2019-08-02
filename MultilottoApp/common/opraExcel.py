#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from xlrd import open_workbook
import xlwt
import xlrd
import os
from MultilottoApp.common.getpathInfo import get_path
import json
from xlutils.copy import copy

class OpraExcel:
    path = get_path()

    def __init__(self,excel_name=None,sheet_id=None):
        if excel_name:
            self.excel_name = excel_name
            self.sheet_id = sheet_id
            print(self.path)
            self.excel_path = os.path.join(self.path, "../testFile",excel_name)  # 文件定位为当前path路径的上一层testfile/excelname
        else:
            self.excel_name ='mltesttest.xlsx'
            print(self.excel_name)
            self.sheet_id = 0
            print(self.path)
            print("##################")
            self.excel_path = os.path.join(self.path, "../testFile", self.excel_name)
            print(self.excel_path)
        self.data = self.get_data()
#     获取文件路径
#         self.excel_path = os.path.join(self.path,"..\\testFile", excel_name) #文件定位为当前path路径的上一层testfile/excelname
#         self.file = open_workbook(self.excel_path) # 打开excel文件
#         self.sheet = self.file.sheet_by_name(sheet_name) #打开excel指定的sheet
#获取sheet的行，列数
        # self.nrows = self.sheet.nrows
        # self.ncols = self.sheet.ncols
    # 获取excel内容
    def get_data(self):
        data = xlrd.open_workbook(self.excel_path)
        tables = data.sheets()[self.sheet_id]
        return tables
#     获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
#     获取单元格内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
#  写入数据
    def write_value(self,row,col,value):
        """

        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data = xlrd.open_workbook(self.excel_path)
        write_data =copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

# 根据对应的caseid找到对应行的内容
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
#     def get_excel(self): #获取excel的内容，并将数据以列表的形式读取出来，不包含casename这一行
#         cls = []
#         for i in range(self.nrows):
# #             如果这个excel的这个sheet的第i行的第 一列不等于case_name，那么我们把这行的数据添加到csl[]
#             if self.sheet.row_values(i)[0] != 'case_name':
#                 cls.append(self.sheet.row_values(i))
#         return cls

if __name__ == '__main__':
    # r = ReadExcel('mltest7.xlsx','工作表1')
    # s = (r.get_excel())
    # print(type(json.dumps(r.get_excel())))
    # print(r.nrows)

    # opers = ReadExcel('mltest.xlsx',0)
    opers =  OpraExcel()
    # opers.get_data()
    # print(opers.get_data().nrows)
    # print(opers.get_lines())
    # print(opers.get_cell_value(1,9))
    print(opers.get_row_num('mm-01'))
    print(opers.get_row_values(2))
    print(opers.get_rows_data('mm-01'))
    print(opers.get_cols_data())
    # 当前仅仅拿到数据，最好实例化类的时候就拿到数据。类实例化的时候调用构造函数