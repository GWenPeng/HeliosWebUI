import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class Send_email_HTML:
    def config(self):
       smtpserver='smtp.partner.outlook.cn'
       user='wenpeng.gu@huilianyi.com'
       password='12240Peng'
       sender='wenpeng.gu@huilianyi.com'
       receiver='1509328341@qq.com'
       subject='test report'

       msg=MIMEText('<html><h1>test repost!!!!</h1></html>','html','utf-8')
       msg['subject']=Header(subject,'utf-8')

       #连接邮件，发送邮件
       try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver, 587)
        smtp.ehlo()
        smtp.starttls()

        smtp.login(user,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        print("邮件发送成功")
        smtp.quit()
       except smtplib.SMTPException:
         print("邮件发送失败")
class Send_email_Attachment:
    def __init__(self):
        self.smtpserver = 'smtp.partner.outlook.cn'
        self.user = 'wenpeng.gu@huilianyi.com'
        self.password = '12240Peng'
        self.sender = 'wenpeng.gu@huilianyi.com'
        self.receiver = '1509328341@qq.com'
        self.subject = '邮件主题！！'
        self.sendfile=open("./testresult.html",'rb').read()
    def attach_setup(self):
        att=MIMEText(self.sendfile,'html','utf-8')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment;filename="testresult.html"'
        msgRoot=MIMEMultipart('related')
        msgRoot['Subject']=Header('自动化测试报告','utf-8')
        msgRoot.attach(att)
        return msgRoot.as_string()

    def Send_email(self):
      try:
        smtp=smtplib.SMTP()
        smtp.connect(self.smtpserver,587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.user,self.password)
        smtp.sendmail(self.sender,self.receiver,self.attach_setup())
        smtp.quit()
      except smtplib.SMTPException:
          print("邮件发送失败！！")



if __name__ == '__main__':
    # Send=Send_email_HTML()
    # Send.config()
     send=Send_email_Attachment()
     send.Send_email()