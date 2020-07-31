#! /usr/bin/env/python
# -*- coding:utf-8 -*-
from xlrd import open_workbook
import os
from MultilottoApp.common.getpathInfo import get_path
import json

class ReadExcel:
    path = get_path()
    print(path)

    def __init__(self,excel_name,sheet_name):
        self.sheet_name = sheet_name
        self.excel_name = excel_name
#     获取文件路径
        self.excel_path = os.path.join(self.path, "../testFile", excel_name) #文件定位为当前path路径的上一层testfile/excelname
        print(self.excel_path)
        self.file = open_workbook(self.excel_path) # 打开excel文件
        self.sheet = self.file.sheet_by_name(sheet_name) #打开excel指定的sheet
#获取sheet的行，列数
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols

    def get_excel(self): #获取excel的内容，并将数据以列表的形式读取出来，不包含casename这一行
        cls = []
        for i in range(self.nrows):
#             如果这个excel的这个sheet的第i行的第 一列不等于case_name，那么我们把这行的数据添加到csl[]
            if self.sheet.row_values(i)[0] != 'case_name':
                cls.append(self.sheet.row_values(i))
        return cls

if __name__ == '__main__':
    r = ReadExcel('mltest.xlsx','工作表1')
    s = (r.get_excel())
    print(type(json.dumps(r.get_excel())))
    print(r.nrows)