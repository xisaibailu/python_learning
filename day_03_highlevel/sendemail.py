"""
python 发送邮件
发信人，收件人，邮件内容，附件

报错：ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '1611796895@qq.com'     #'from@runoob.com'
receivers = ['3506677128@qq.com']

"""
三个参数：
1.第一个为文本内容
2.第二个plain置纯文本格式，还可以是html
3.第三个utf-8编码
"""
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
print('message数据格式：', type(message))

#标准邮件的三个头部信息：From、To、Subject
message['From'] = Header('菜鸟教程', 'utf-8')  # 发送者
message['To'] = Header("测试", 'utf-8')  # 接收者

subject = "Python SMTP邮件测试"
message['Subject'] = Header(subject, 'utf-8')

try:
  #实例化smtplib模块的SMTP对象smtpObj来连接SMTP
  stmpObj = smtplib.SMTP('localhost')
  #使用sendmai方法发送信息
  stmpObj.sendmail(sender, receivers, message.as_string())
  print("邮件发送成功")
except smtplib.SMTPException:
  print("Error:无法发送邮件")


