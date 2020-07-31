
#载入需要的包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1.邮件主题：包含邮件正文+excel附件
def main_email(text,xlsx_path, xlsx_name):
    '''
    *text->str: 要发送的邮件正文*
    *xlsx_path: excel文件所在的路径*
    *xlsx_name：excel文件，例如a.xlsx*
    '''
    msg = MIMEMultipart()

    # 添加纯文本，text为需要输入的文本，字符串格式
    text_msg = MIMEText(text)
    msg.attach(text_msg)

    def add_excel(xlsx_file, xlsx_name):  # 添加excel附件
        # 将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，对于MIMEText()来说默认的编码形式是base64 对于二进制文件来说没有设置base64，会出现乱码
        msg_xlsx = MIMEText(open(xlsx_file, 'rb').read(), 'base64', 'utf-8')
        # 设置文件在附件当中的名字
        msg_xlsx.add_header('Content-Disposition', 'attachment', filename=xlsx_name)
        return msg_xlsx

    msg_xlsx = add_excel(xlsx_path + xlsx_name, xlsx_name)
    msg.attach(msg_xlsx)
    return msg

    # 2、登录邮箱
def login_email(smtpsever, username, pwd):
    '''
    *smtpsever: 邮箱服务器*
    *username: 邮箱地址*
    *pwd: 邮箱登陆密码*
    '''
    #连接邮箱服务器
    sever = smtplib.SMTP(smtpsever)
    #登陆邮箱
    result = sever.login(username, pwd)
    print('登陆结果：', result)
    return sever
    #3、发送邮件
def send_email(title, sender, to_receiver, cc_receiver,  sever, msg):
    '''
    Subject邮件主体，对应要发送的邮件名，对应值title为字符串
    From发件人地址，对应值sender为发送人邮箱地址
    To收件人邮箱地址，Cc抄送人邮箱地址

    to_receiver-> list
    cc_receiver-> list，可批量发送
    sever: 第2步函数返回sever
    msg: 第1步函数返回邮件主体
    '''
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = ';'.join(to_receiver)
    msg['Cc'] = ';'.join(cc_receiver)
    receiver = ';'.join(to_receiver + cc_receiver)
    receiver.split(";")
    sever.sendmail(sender, receiver.split(";"), msg.as_string())
    print('收件人', receiver)