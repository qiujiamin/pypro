#! /usr/bin/env/python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
def sendmail(subject, content):
    email_host = 'smtp.163.com'     # 发送者是qq邮箱
    email_user = 'jiamin721@163.com'  # 发送者账号
    email_pwd = 'wzgl521qjm'       # 发送者密码
    maillist ='qiujm@500wan.com'    # 接收者账号，本来想写成[]list的，但是报错，还没解决！
    me = email_user

    msg = MIMEText(content, 'html', 'utf-8')    # 邮件内容，三个参数：第一个为文本内容，第二个 html 设置文本格式，第三个 utf-8 设置编码
    msg['Subject'] = subject    # 邮件主题
    msg['From'] = me    # 发送者账号
    msg['To'] = maillist    # 接收者账号列表（列表没实现）

    smtp = smtplib.SMTP(email_host) # 如上变量定义的，是qq邮箱
    smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
    smtp.sendmail(me, maillist, msg.as_string())    # 参数分别是发送者，接收者，第三个不知道
    smtp.quit() # 发送完毕后退出smtp
    print ('email send success.')

sendmail('主题', '内容')    # 调用发送邮箱的函数