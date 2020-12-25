# from email.mime.text import MIMEText
# import email
# import  smtplib

# msg = MIMEText('hello,send by Python','plain','utf-8')
# 构造一个最简单的纯文本邮件。第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
# 输入Email地址和口令
# from_addr = input('From: ')
# password = input('Password: ')
# 输入收件人地址：
# to_addr = input('To: ')
# 输入SMTP服务器地址：
# smtp_server = input('SMTP server: ')

# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
# server.set_debuglevel(1)
# 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# server.ehlo()
# server.starttls()
# 如果不加上面两行代码，会有如下报错：
# smtp_server.login(self.sender, self.password)  # 登录
#   File "C:\Python36\lib\smtplib.py", line 697, in login
#     "SMTP AUTH extension not supported by server.")
# smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server.
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
# SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
# ===========================================================================
# from email import encoders
# from email.header import Header
# from email.utils import parseaddr,formataddr
# from email.mime.text import MIMEText
# # import email
# import  smtplib
#
# def _format_addr(s):
#     name,addr=parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))
#
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# msg = MIMEText('hello,send by Python...','plain','utf-8')
# msg['From'] = _format_addr('Python爱好者: {}'.format(from_addr))
# msg['To'] = _format_addr('管理员：<%s>' % to_addr)
# # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
# msg['Subject'] = Header('来自SMTP的问候...','utf-8').encode()
# # 如果包含中文，需要通过Header对象进行编码。
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
# ====================================================================
# 发送附件
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import  smtplib
#
# sender = 'ruopu1989@hotmail.com'
# receivers = ['1102998123@qq.com']
# sender_password = 'X5kzxctScjn7rh!'
# smtp_sender = 'smtp-mail.outlook.com'
#
#
# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = ';'.join(receivers)
# subject = 'Python SMTP 邮件测试...'
# msg['Subject'] = Header(subject,'utf-8')
#
# # 邮件正文内容
# msg.attach(MIMEText('这是测试邮件正文内容。。。','plain','utf-8'))
#
# # 构造附件1,传送当前目录下的test.txt文件
# att1 = MIMEText(open('/home/shouyu/nohup.out','rb').read(),'base64','utf8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.nohup"'
# msg.attach(att1)
#
# try:
#     server = smtplib.SMTP(smtp_sender,25)
#     server.set_debuglevel(1)
#     server.ehlo()  # 用户认证
#     server.starttls()
#     server.login(sender,sender_password)
#     server.sendmail(sender,[receivers],str(msg))
#     server.quit()
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
# ============================================================
# 发送附件，函数
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import datetime
from urllib import request
import pathlib


# 获取昨天的日期，这是文件名的一部分
def getYesterday():
    today = datetime.date.today()
    yesterday = (today - datetime.timedelta(days=1)).strftime('%Y%m%d')
    # print(yesterday)
    return yesterday

def downloadFile():
    url = 'http://172.16.174.55:8088/hourdata/gehuavhmlp/vh_miyun/'+getYesterday()+'.zip'
    # s = request.urlopen(url).read()
    LocalPath = pathlib.Path('/tmp/'+getYesterday()+'.zip')
    try:
        request.urlretrieve(url,LocalPath)
    except:
        sender = 'miyunjike@bgctv.com.cn'
        # receivers = ['1102998123@qq.com']\
        receivers = ['zheng.yao@xor-media.tv']
        sender_password = 'My@1234'
        smtp_sender = 'smtp.exmail.qq.com'
        subject = '密云时段开机数据下载失败'
        msg = MIMEMultipart()  # 实例化email对象
        msg['From'] = sender  #
        msg['To'] = str(receivers)
        msg['Subject'] = subject

        server = smtplib.SMTP_SSL(smtp_sender, 465)
        server.set_debuglevel(1)
        server.ehlo()  # 用户认证
        # server.starttls()
        server.login(sender, sender_password)
        server.sendmail(sender, [receivers], str(msg))
        server.quit()
        print("Error: 无法下载邮件")

# print(1, s)
# 邮箱登录地址：mail.bgctv.com.cn
def send_mail(sender = 'miyunjike@bgctv.com.cn',receivers = ['1102998123@qq.com'],sender_password = 'My@1234',smtp_sender = 'smtp.exmail.qq.com', subject = '密云时段开机数据：'+getYesterday()+'.zip'):
    msg = MIMEMultipart()  #  实例化email对象
    msg['From'] = sender  #
    # msg['To'] = ';'.join(receivers)
    msg['To'] = str(receivers)
    # subject = 'Python SMTP 邮件测试...'

    msg['Subject'] = subject

# 邮件正文内容
    msg.attach(MIMEText('密云时段开机数据','plain','utf-8'))

# 构造附件1,传送当前目录下的test.txt文件
    att1 = MIMEText(open('/tmp/'+getYesterday()+'.zip','rb').read(),'base64','utf8')
    att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#     att1["Content-Disposition"] = 'attachment; filename="密云时段开机数据.zip"'  # 这种方法无法修改附件的名称
    att1.add_header('Content-Disposition','attachment',filename=getYesterday()+'.zip')
    msg.attach(att1)

    try:
        downloadFile()
        server = smtplib.SMTP_SSL(smtp_sender,465)
        server.set_debuglevel(1)
        server.ehlo()  # 用户认证
        server.starttls()
        server.login(sender,sender_password)
        server.sendmail(sender,[receivers],str(msg))
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        receivers = ['zheng.yao@xor-media.tv']
        server = smtplib.SMTP_SSL(smtp_sender, 465)
        server.set_debuglevel(1)
        server.ehlo()  # 用户认证
        server.starttls()
        server.login(sender, sender_password)
        server.sendmail(sender, [receivers], str(msg))
        server.quit()
        print("Error: 无法发送邮件")

# 下载文件
downloadFile()
send_mail()
print(getYesterday())