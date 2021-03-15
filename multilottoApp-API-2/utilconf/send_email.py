import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
class SendEmail:
    global send_user
    global email_host
    global password
    global toaddrs
    global xlsFile
    # 邮箱服务，本人用163
    email_host = "smtp.163.com"
    #发送邮箱
    send_user = "jiamin721@163.com"
    # 邮箱密码
    password = ""
    # 接收人list
    toaddrs = ['onepiece721@163.com','qiujm@500wan.com']
    # 文件
    xlsFile ='../dataconfig/allios.xls'

    def senf_mail(self,user_list,sub,content):
        user = "jiamin"+"<"+send_user+">"
        # 邮件内容设置
        message = MIMEMultipart('related')
        messagetext = MIMEText(content,_subtype='plain',_charset='utf-8')
        message.attach(messagetext)
        # 添加excel附件
        msg_xlsx = MIMEText(open(xlsFile, 'rb').read(), 'base64', 'utf-8')
        # cur_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cur_time=time.strftime("%Y-%m-%d", time.localtime())
        # 设置文件在附件当中的名字
        msg_xlsx.add_header('Content-Disposition', 'attachment', filename="testResult-"+cur_time+".xls")
        message.attach(msg_xlsx)
        # 邮件主题
        message['Subject'] = sub
        # 发送方信息
        message['From'] = user
        #接收方信息
        message['To'] = ";".join(user_list)
        try:
            server = smtplib.SMTP(email_host)
            server.connect(email_host)
            server.login(send_user,password)
            server.sendmail(user,user_list,message.as_string())
            server.close()
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num
        #90%
        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result ="%.2f%%" %(fail_num/count_num*100)

        user_list= toaddrs
        sub = "接口自动化测试报告"
        # 内容以后可优化
        content = "Dear all,\n  此次一共运行接口个数%s个，通过个数为%s个，失败个数为%s，通过率为%s，失败率为%s。详情请看excel文件。\n谢谢" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.senf_mail(user_list,sub,content)

if __name__ == '__main__':
    sen = SendEmail()
    # user_list = ['onepiece721@163.com']
    # sub = "这个是测试邮件"
    # content = "这个是内容"
    # sen.senf_mail(user_list, sub, content)
    sen.send_main([1,2,3,4],[1,2])
