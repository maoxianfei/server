#-*- coding: utf-8 -*-
#python2.x email.py
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib

def email(head,tex):
    '''
    发送邮件给
    :param path: 附件路径
    :param head: 邮件主题
    :return:
    '''
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    from_addr = '1102836917@qq.com'
    password = 'bdxztldobaorgfag'
    to_addr = '1102836917@qq.com'
    # to_addr = '1102836917@qq.com'
    smtp_server = 'smtp.qq.com'
    # msg = MIMEText('hello', 'plain', 'utf-8')
    msg=MIMEMultipart()
    msg['From'] = _format_addr('千里侠骨香 <%s>' % from_addr)
    msg['To'] = _format_addr('公众号用户 <%s>' % to_addr)
    msg['Subject'] = Header(head, 'utf-8').encode()

    #邮件正文
    msg.attach(MIMEText(tex, 'plain', 'utf-8'))
    #邮件附件
    # with open(path,'rb')as f:
    #     # 设置附件的MIME和文件名，这里是png类型:
    #     mime = MIMEBase('text', 'txt', filename=path.split('/')[-1])
    #     # 加上必要的头信息:
    #     mime.add_header('Content-Disposition', 'attachment', filename=path.split('/')[-1])
    #     mime.add_header('Content-ID', '<0>')
    #     mime.add_header('X-Attachment-Id', '0')
    #     # 把附件的内容读进来:
    #     mime.set_payload(f.read())
    #     # 用Base64编码:
    #     encoders.encode_base64(mime)
    #     # 添加到MIMEMultipart:
    #     msg.attach(mime)
    try:
        server = smtplib.SMTP_SSL(smtp_server, 465)
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('send mail success')
    except:
        print('send mail fail')