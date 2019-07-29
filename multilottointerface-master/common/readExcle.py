from xlrd import open_workbook
import os
from common.getpathInfo import get_path
import json


class ReadExcle:
    path = get_path()

    def __init__(self, excle_name, sheet_name):
        self.sheet_name = sheet_name
        self.excle_name = excle_name
    # 获取文件路径
        self.excle_path = os.path.join(self.path, "../testFile", excle_name)  # 文件定位为当前path路径的上一层的testfile/exclename
        self.file = open_workbook(self.excle_path)  # 打开excle文件
        self.sheet = self.file.sheet_by_name(sheet_name)  # 打开excle指定的sheet
    # 获取sheet的行、列数
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols

    def get_excle(self):  # 获取excle的内容，并将数据以列表的形式读取出来，不包括casename这一行
        cls = []
        for i in range(self.nrows):
            # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            if self.sheet.row_values(i)[0] != 'case_name':
                cls.append(self.sheet.row_values(i))
        return cls


if __name__ == '__main__':
    r = ReadExcle('mltest.xlsx', '工作表1')
    s = (r.get_excle())
    print(s)
    print(type(json.dumps(r.get_excle())))
    print(r.nrows)