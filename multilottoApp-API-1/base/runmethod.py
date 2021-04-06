import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        """
        post方法执行
        :param url: 请求url
        :param data: 请求数据
        :param header: 请求头
        :return: 字典类型的响应结果
        """
        res = None
        if header !=None:
            res = requests.post(url =url,data=data,headers=header)
        else:
            res = requests.post(url =url,data=data)
        return res.json()
    def get_main(self,url,data=None,header=None):
        """
        get方法：目前没用到
        :param url:请求url，一般包含参数
        :param data:请求数据，一般为None
        :param header:请求头
        :return:字典类型的响应结果
        """
        res = None
        if header !=None:
            # res = requests.get(url =url,dataconfig=dataconfig,headers=header).json()
            res = requests.get(url =url,data=data,headers=header,verify=False)
        else:
            res = requests.get(url =url,data=data,verify=False)
        return res.json()
    def run_main(self,method,url,data=None,header=None):
        """
        按传入方法（post/get）执行
        :paget_maenram method: 方法名（仅支持post/get）
        :param url: 请求url
        :param data: 请求数据
        :param header: 请求头
        :return:json字符串的响应结果
        """
        res = None
        if method  == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)







