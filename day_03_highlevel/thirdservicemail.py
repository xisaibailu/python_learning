"""
使用QQ邮箱作为第三方服务
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender="1611796895@qq.com"
my_pass="llnmzpipbyxcfbae"
my_user="nice_dyw@163.com"
mail_content="这是一个测试邮件"

def mail():
  ret = True
  try:
    msg = MIMEText(mail_content,'plain','utf-8')
    msg["From"]=formataddr(["雨亦奇",my_sender])  #发件人邮箱昵称，发件人邮箱账号
    msg["To"]=formataddr(["",my_user])          #收件人邮箱昵称，收件人邮箱账号
    msg["Subject"]="菜鸟发送邮件"

    server =smtplib.SMTP_SSL("smtp.qq.com",465)
    server.login(my_sender,my_pass)
    server.sendmail(my_sender,[my_user,"1611796895@qq.com"],msg.as_string()) #发件人邮箱账号，收件人邮箱账号

    #关闭连接
    server.quit()
  except Exception:
    ret=False
  return ret

#调用
ret = mail()
if ret:
  print("邮件发送成功")
else:
  print("邮件发送失败")
