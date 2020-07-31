import json
# 加载文件基础
# with open('../dataconfig/logininfo.json','r') as f:
#     dataconfig = json.load(f)
# f = open('../dataconfig/logininfo.json',encoding='utf-8')
# dataconfig = json.load(f)
# print(dataconfig['login'])

class OperationJson:
    def __init__(self,file_path=None):
        if file_path ==None:
            self.file_path = '../dataconfig/all.json'
            print(file_path)
        else:
            self.file_path = file_path
        self.data =self.read_data()
    # 读取json文件
    def read_data(self):
        # fp = open(path)
        # fp.close()
# 为了防止忘记关闭，使用with
#         with open('../dataconfig/login1.json') as fp:
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
    # 根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        return self.data[id]
#    写json
#     def write_data(self,data):
#         with open('../dataconfig/cookie.json','w') as fp:
#             fp.write(json.dumps(data))
# 写/覆盖json
    def write_data(self,filepath,key,userdata):
        # 需要获取到数据
        # redata = self.get_data(jsonname)
        #
        self.data[key]= userdata
        print(self.data)
        with open(filepath,'w') as fp:
            fp.write(json.dumps(self.data))
        print("写入成功")
        fp.close()
        # json.dump(userdata,open(filepath),'a')
    #    获取coockie
    # def get_cookie(self):


if __name__ == '__main__':
    # opjson = OperationJson('../dataconfig/all.json')
    # print(opjson.get_data('login'))
    logininfo= {
        "usercheck":"aaaaa",
        "userid":"99999"
    }
    filepath = '../dataconfig/logininfo.json'
    opjson = OperationJson(filepath)
    # getdata = opjson.get_data('logininfo')
    opjson.write_data(filepath,'logininfo',logininfo)
    # print(opjson.get_data('logininfo'))
    # opjson = OperationJson('../dataconfig/cookie.json')
    # print(opjson.get_data('header'))



