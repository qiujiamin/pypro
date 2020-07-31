#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# smtp =>simple mail transfer protocol  简单邮件传输协议
import smtplib
import email  # 文件名不可以和引入的库同名
from email.mime.image import MIMEImage  # 图片类型邮件
from email.mime.text import MIMEText  # MIME 多用于邮件扩充协议
from email.mime.multipart import MIMEMultipart  # 创建附件类型

HOST = "smtp.163.com"   # 调用的邮箱借借口
SUBJECT = '发送了一封测试邮件'  # 设置邮件标题
FROM = 'jiamin721@163.com'  # 发件人的邮箱需先设置开启smtp协议
TO = 'qiujm@500wan.com'  # 设置收件人的邮箱（可以一次发给多个人,用逗号分隔）
message = MIMEMultipart('related')  # 邮件信息，内容为空  #相当于信封##related表示使用内嵌资源的形式，将邮件发送给对方
# message = MIMEText(content,_subtype='plain',_charset='utf-8')
def sendmail(HOST, SUBJECT,FROM,TO,message):
    """
    发送邮件主体到对方邮箱
    :发送信息参数说明:
    1.内容必须是字符串
    2.内容形式，文本类型默认为plain
    3.内容编码使用utf-8
    :其他：
    图片和excel文件需要和本脚本一个目录下
    """

    # ===========发送信息内容=============
    # message_html = MIMEText('shuai123 消灭不开行', 'plain', 'utf-8')
    # message_html = MIMEText('<h1 style="color:red；font-size:100px">测试信息已收到</h1><img src="cid:small">', 'html', 'utf-8')
    # message.attach(message_html)

    # ===========发送图片-=============
    #发送图片-预览信息
    # image_data = open('email_demo.jpg', 'rb')
    # message_image = MIMEImage(image_data.read())
    # image_data.close()# 关闭刚才打开的文件
    # message_image.add_header('Content-ID', 'small')
    # message.attach(message_image)# 添加图片文件到邮件信息中去
    # #发送图片-附件
    # message_image = MIMEText(open('email_demo.jpg', 'rb').read(), 'base64', 'utf-8')
    # message_image['Content-disposition'] = 'attachment;filename="email_demo_change.jpg"'# 设置图片在附件当中的名字
    # message.attach(message_image)# 添加图片文件到邮件-附件中去
    # ===========发送excel-附件=============
    message_xlsx = MIMEText(open('all.xls', 'rb').read(), 'base64', 'utf-8')# 将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，对于MIMEText()来说默认的编码形式是base64 对于二进制文件来说没有设置base64，会出现乱码
    message_xlsx['Content-Disposition'] = 'attachment;filename="email_demo_change.xlsx"'# 设置文件在附件当中的名字
    message.attach(message_xlsx)# 添加excel文件到邮件-附件中去

    # ===========配置相关-=============
    message['From'] = FROM # 设置邮件发件人
    message['TO'] = TO # 设置邮件收件人
    message['Subject'] = SUBJECT # 设置邮件标题
    email_client = smtplib.SMTP_SSL()# 获取江建有奖传输协议证书
    email_client.connect(HOST, '465')# 设置发送域名，端口465
    result = email_client.login(FROM, 'wzgl521qjm')  # qq授权码
    print('登录结果', result)

    # ===========操作=============
    email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string()) #发送邮件指令
    email_client.close()# 关闭邮件发送客户端

if __name__ == '__main__':
    sendmail(HOST=HOST, SUBJECT=SUBJECT,FROM=FROM,TO=TO,message=message)