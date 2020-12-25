# 发送附件，函数
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
from urllib import request
import urllib
from urllib import parse
import pathlib


# 获取昨天的日期，这是文件名的一部分
def getYesterday():
    today = datetime.date.today()
    yesterday = (today - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    # print(yesterday)
    return yesterday

def downloadFile():
    #url1 = 'http://172.16.174.55:8088/hourdata/gehuavhmlp/send_report/2020-09-07歌华三款盒子开机人次统计.csv'
    url1 = 'http://172.16.174.55:8088/hourdata/gehuavhmlp/send_report/'+getYesterday()+'歌华三款盒子开机人次统计.csv'
    urlbefore = url1.split("//")[0]
    urlafter = url1.split("//")[1]
    url = urlbefore + "//" + parse.quote(urlafter)
    #url = 'http://172.16.174.55:8088/hourdata/gehuavhmlp/send_report/'+getYesterday()+'歌华三款盒子开机人次统计.csv'
    # s = request.urlopen(url).read()
    LocalPath = pathlib.Path('D:\\no_delete_task_data\\BigSampleData\\'+getYesterday()+'歌华三款盒子开机人次统计.csv')
    #print(url)
    #LocalPath = pathlib.Path('D:\\no_delete_task_data\\BigSampleData\\2020-09-07歌华三款盒子开机人次统计.csv')
    request.urlretrieve(url,LocalPath)

# print(1, s)

def send_mail(sender = 'ziwei.zhang@xor-media.tv',receivers = ['1411002380@qq.com'],sender_password = 'ICE0JCIJBdP5qvtD',smtp_sender = 'mail.xor-media.tv', subject = '开机人次数据汇总：'+getYesterday()):
    msg = MIMEMultipart()  #  实例化email对象
    msg['From'] = sender  #
    msg['To'] = ','.join(receivers)
    # msg['To'] = str(receivers)
    # subject = 'Python SMTP 邮件测试...'

    msg['Subject'] = subject

# 邮件正文内容
    msg.attach(MIMEText('开机人次数据汇总','plain','utf-8'))

# 构造附件1,传送当前目录下的test.txt文件
    att1 = MIMEText(open('D:\\no_delete_task_data\\BigSampleData\\' + getYesterday() + '歌华三款盒子开机人次统计.csv','rb').read(),'base64','utf8')
    att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#     att1["Content-Disposition"] = 'attachment; filename="密云时段开机数据.zip"'  # 这种方法无法修改附件的名称
    att1.add_header('Content-Disposition','attachment',filename=getYesterday()+'歌华三款盒子开机人次统计.csv')
    msg.attach(att1)

    try:
        server = smtplib.SMTP(smtp_sender,25)
        ###server.set_debuglevel(1)
        server.ehlo()  # 用户认证
        server.starttls()
        server.login(sender,sender_password)
        server.sendmail(sender,msg['To'].split(','),str(msg))
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

# 下载文件
downloadFile()
#send_mail()