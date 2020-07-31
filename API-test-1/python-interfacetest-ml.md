#### python接口自动化测试

参考文档来源：https://blog.csdn.net/iam_emily/article/details/82670540

代码git:

#####  1、接口方法的实现和封装：runmethod

requests库可以很好的帮助我们实现HTTP请求，[API参考文档](http://docs.python-requests.org/zh_CN/latest/api.html#id5)，这里我创建了runmethod.py，里面包含RunMethod类：

```python
import requests
import json
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header !=None:
            res = requests.post(url =url,data=data,headers=header)
        else:
            res = requests.post(url =url,data=data)
        return res.json()
    def get_main(self,url,data=None,header=None):
        res = None
        if header !=None:
            res = requests.get(url =url,data=data,headers=header,verify=False)
        else:
            res = requests.get(url =url,data=data,verify=False)
        return res.json()
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method  == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
```

这里需要注意就是python默认参数和可选参数要放在必选参数后面.对于相应数据使用json格式进行返回。参数verify=false表示忽略对 SSL 证书的验证。

##### 2 组织测试与生成报告

待定

##### 3、测试数据处理

这一部分主要包括设计测试数据，数据提取和参数化，以及解决数据依赖。

###### 1、excel配置

![1572341456394](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572341456394.png)

基本描述如上，每一列对应值含义在data-data_config.py文件

![1572341700108](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572341700108.png)

###### 2、操作表格

操作Excel的模块，主要包含了对Excel表格的操作，获取表单、行、列、单元格内容等。

其中写数据用于将运行结果写入Excel文件（result:通过写pass,不通过写返回值），先用copy复制整个文件，通过get_sheet()获取的sheet有write()方法。

![1572342278426](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572342278426.png)

###### 3、json读取处理

为解决数据展示统一和excel加密不好修改数据情况，请求参数原始值（data）及修改参数（modifydata项）或其他特殊处理(如登录信息保存)，提供根据关键字进行json文件读，获取，写等操作的方法operation_json.py

读写操作使用的是`json.load(),json.dump()` 传入的是文件句柄。

数据以字典格式处理，common即为关键字，如图。

![1572342993492](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572342993492.png)

![1572342909485](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572342909485.png)

###### 4、获取测试数据并做对应处理

在定义好Excel和json操作及data配置模块后，我们将其应用于我们的测试表单，定义一个获取数据模块：

该模块将Excel操作类实例化后用于操作测试表单，分别获得测试运行所需的各种条件。

![1572343922059](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572343922059.png)

![1572344064151](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572344064151.png)

![1572344140810](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572344140810.png)

![1572344257938](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572344257938.png)

![1572344351393](C:\Users\Administrator.QIUJM-PC\AppData\Roaming\Typora\typora-user-images\1572344351393.png)

###### 5、数据依赖



