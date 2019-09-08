import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication


def send_mail(from1, to, title, content, attach=None, pic=None, type='plain'):

    # 生成包含多个邮件体的对象
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = from1
    msg['to'] = to
    msg['subject'] = title

    # 邮件正文
    txt = email.mime.text.MIMEText(content, type)
    msg.attach(txt)

    # 文件附件
    if attach is not None:
        part = MIMEApplication(open(attach, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=attach)
        msg.attach(part)

    # jpg图片附件
    if pic is not None:
        jpg_part = MIMEApplication(open(pic, 'rb').read())
        jpg_part.add_header('Content-Disposition', 'attachment', filename=pic)
        msg.attach(jpg_part)

    # 发送邮件--------------------------------------------------------

    # 链接服务器，smtp地址+端口
    # smtp = smtplib.SMTP_SSL('smtp.qq.com', '465')     # 调试通过
    with smtplib.SMTP('smtp.126.com', '25') as smtp:    # 调试通过

        # 设置为调试模式，console中显示
        smtp.set_debuglevel(1)

        # 登陆，用户名+密码，密码可能需要填写授权码
        smtp.login('fekkngchggg', 'xxxxxxxxxxxxx')

        # 发送，from+to+内容
        smtp.sendmail(from1, to, str(msg))


# 设置变量并调用发送邮件
from1 = 'fettgfrews@126.com'
to = '09h658gvcb@qq.com'
title = '你好吗哈哈哈'
content = """
Hi all,
这是一封我发给你的邮件。
你好吗
哈哈哈
有附件哦！"""
attach = 'log_log.txt'
pic = 'mail.jpg'

send_mail(from1, to, title, content, attach, pic)
