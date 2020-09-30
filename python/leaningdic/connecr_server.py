__author__ = "MUT6 Sch01aR"
import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许链接不再know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 链接服务器
ssh.connect(hostname='103.6.128.6',port=50022,username='malta',password='50o##Ma1TA$$')
# 执行命令并获取命令结果
stdin,stdout,srderr = ssh.exec_command('whoami')
res,err = stdout.read(),srderr.read()
result = res if res else err
print(result)
ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='5.79.104.95',port=49150,username='wei.shu',password='ZpsYxecT8VRC')
stdin,stdout,srderr = ssh.exec_command('whoami')
res1,err1 = stdout.read(),srderr.read()
result1 = res if res else err
print(result1)
ssh.close()
ssh1.close()