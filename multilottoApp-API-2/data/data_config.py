class global_var:
    #case_id 用例id,唯一标识
    Id = '0'
    # 用例名称，只用于用户查看，无功能
    case_name ='1'
    # 请求名称，待定，暂无关联.
    request_name = '2'
    # 域名，分辨dev或线上(python服务或h5app服务)，如修改可统一变更（后面可能补一个文件直接读）。当前APP仅写死四个：dev_服务,dev_h5app,线上服务，线上h5app地址
    domain = '3'
    # 除了域名外的请求地址，会组合domain作为请求url
    url_path = '4'
    # 是否执行
    run ='5'
    # 请求类型，目前仅配置post及get,其他暂时报错
    run_way = '6'
    # 请求头，暂时写死,yes时调用，无需头文件则不填写。后面会改为，类似json的定制处理
    header = '7'
    # case依赖，填写需要提前执行的caseid，当前仅支持一个，如需多个，请多写几个用例。ps.登录已特殊处理,如依赖登录请need_login填写yes
    case_depend = '8'
    # 数据依赖 执行依赖caseid后，要提取的返回数据值。后续用于该行用例执行的请求。填写提取正则。如info.syndicatename，多个字段用#分隔，对应字段依赖也需要按#分隔（登录字段可以除外）
    data_depend ='9'
    # 字段依赖
    field_depend ='10'
    # 请求数据，写个关键字，细节到json文件中写，为解决经常需要修改请求数据，但excel加密修改麻烦问题，且排版相对漂亮易读
    data = '11'
    # 是否需要登录信息，需要则读取已保存的最新登录信息（userid,usercheck），来修改该接口请求数据中的登录信息
    need_login = '12'
    # 请求数据修改，同data，为同一个接口修改data中部分参数提供修改，方便同一个接口各异常参数流准备数据。注册登录除外
    modifydata = '13'
    # 预期结果，个人一般写接口错误码
    expect ='14'
    # 实际运行结果，初始不需要填写。与预期匹配正确，写入pass;与预期有异常，写入返回结果。方便检查失败情况
    result='15'
# 获取caseid
def get_id():
    return global_var.Id
# 获取用例名称
def get_case_name():
    return global_var.case_name
# 获取名称
def get_request_name():
    return global_var.request_name
# 获取域名
def get_domain():
    return global_var.domain
# 获取url_path
def get_url_path():
    return global_var.url_path
# 获取是否执行
def get_run():
    return global_var.run
# 获取请求方式
def get_run_way():
    return global_var.run_way
# 获取头flag
def get_header():
    return global_var.header
# 获取用例数据依赖id
def get_case_depend():
    return global_var.case_depend
# 获取依赖数据
def get_data_depend():
    return global_var.data_depend
# 获取数据所属字段
def get_field_depend():
    return global_var.field_depend
# 获取请求数据
def get_data():
    return global_var.data
def get_modifydata():
    return global_var.modifydata
# 获取是否需要登录参数
def get_needlogin():
    return global_var.need_login
# 获取请求预期结果
def get_expect():
    return global_var.expect
# 获取实际结果
def get_result():
    return global_var.result
