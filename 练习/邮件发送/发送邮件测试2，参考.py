# 作者：龙小江i
# 链接：https://www.jianshu.com/p/d4aed6f32c69
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# 使用时需修改的地方标记如下：
#
# 第17行（发件人邮箱）
# 第18行（发件人邮箱授权码，注意，不是邮箱登录密码）
# 第82行（邮件主题/标题）
# 第83行（邮件正文）
# 第91行（测试用txt文件路径）
# 第93行（测试用接收人邮箱）
# 运行环境
# anaconda
# jupyter notebook
# ===============================================================================================================
'''
发送邮件函数：
    send_email(email_subject = '邮件主题', email_content = '邮件正文', email_attanchment_address = '邮件附件地址', email_receiver = '邮件接收人')
附件格式：
    xlsx, pdf, txt, jpg, mp3
参数说明：
    email_subject：邮件主题
    email_content：邮件正文
    email_attanchment_address：邮件附件地址，格式为['','',''...]
    email_receiver：邮件接收人，格式为['','',''...]
'''


def send_email(email_subject, email_content, email_attanchment_address, email_receiver):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    sender = '在这里填入发件人邮箱地址'
    passwd = '在这里填入发件人邮箱授权码，注意，部不是邮箱密码'
    receivers = email_receiver  # 邮件接收人

    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = email_subject
    msgRoot['From'] = sender

    if len(receivers) > 1:
        msgRoot['To'] = ','.join(receivers)  # 群发邮件
    else:
        msgRoot['To'] = receivers[0]

    part = MIMEText(email_content)
    msgRoot.attach(part)

    # 添加附件
    for path in email_attanchment_address:
        if '.jpg' in path:
            # jpg
            jpg_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=jpg_name)
            msgRoot.attach(part)

        if '.pdf' in path:
            # pdf
            pdf_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=pdf_name)
            msgRoot.attach(part)

        if '.xlsx' in path:
            # xlsx
            xlsx_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=xlsx_name)
            msgRoot.attach(part)

        if '.txt' in path:
            # txt
            txt_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=txt_name)
            msgRoot.attach(part)

        if '.mp3' in path:
            # mp3
            mp3_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=mp3_name)
            msgRoot.attach(part)

    try:
        s = smtplib.SMTP()
        s.connect('smtp.163.com')
        s.login(sender, passwd)
        s.sendmail(sender, receivers, msgRoot.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败')
    finally:
        s.quit()


# 发送测试邮件
email_subject = '邮件主题'
email_content = '邮件正文'
# jpg_path = ''
# pdf_path = ''
# xlsx_path = ''
# txt_path = ''
# mp3_path = ''
# file_path = [jpg_path, pdf_path, xlsx_path, txt_path, mp3_path]
# 下边两行为测试代码，将txt_path与email_receiver替换为你的txt附件地址与接收方邮箱
txt_path = 'C:\\Users\\longxiaojiangi\\Desktop\\stopwords\\chinese.txt'
email_attanchment_address = [txt_path]
email_receiver = ['1405935821@qq.com']
send_email(email_subject, email_content, email_attanchment_address, email_receiver)
