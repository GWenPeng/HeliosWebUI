import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import logging
import  common.mainModule
module_logger=logging.getLogger('mainModule.run')
class Send_email_HTML:
    def config(self):
       smtpserver='smtp.partner.outlook.cn'
       user='wenpeng.gu@huilianyi.com'
       password='12240peng'
       sender='wenpeng.gu@huilianyi.com'
       receiver=''
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
    def __init__(self,sendfile="../report/201810301853-result.html"):
        # self.smtpserver ="smtp.partner.outlook.cn"
        self.smtpserver = "smtpdm.aliyun.com"
        self.port=80
        self.user = 'notice@service.huilianyi.com'
        # self.user = 'wenpeng.gu@huilianyi.com'
        self.password = 'ZhenHui2017'
        self.sender = 'notice@service.huilianyi.com'
        self.receivers =[
                        # "yan.huang03@hand-china.com",
                         'wenpeng.gu@huilianyi.com'
                         # "yuxiong.ding@huilianyi.com",
                         # "gang.liu@huilianyi.com",
                         # "ziao.shen@huilianyi.com",
                         # "changyuan.tang@huilianyi.com",
                         # "chuanlin.li@huilianyi.com"
                         ]
        self.subject = '邮件主题！！'
        self.sendfile=open(sendfile,'r',encoding="utf-8").read()
        # htmlf = open('E:\\test2.html', 'r', encoding="utf-8")
        # htmlcont=htmlf.read()
        # self.msg = MIMEText('<html><h1>stage 环境自动化测试报告汇总，请查看附件</h1></html>', 'html', 'utf-8')
        # self.msg['subject'] = Header(self.subject, 'utf-8')

    def attach_setup(self):
        att=MIMEText(self.sendfile,'html','utf-8')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment;filename="Web_UI_Report_result.html"'
        msg = MIMEText(self.sendfile,_subtype='html',_charset='utf-8')
        msg['Subject']=Header('自动化报告','utf-8')
        # msg['Content-Type'] = 'application/octet-stream'
        # 以附件的形式发送邮件
        # msg['Content-Disposition'] = 'attachment;filename="Web_UI_Report_result.html"'

        #添加邮件正文
        #msgRoot=MIMEMultipart('related')
        #对于multipart类型，下面有三种子类型：mixed、alternative、related
        # multipart/mixed可以包含附件。
        #
        # multipart/related可以包含内嵌资源。
        #
        # multipart/alternative 纯文本与超文本共存
        msgRoot=MIMEMultipart("alternative")
        # msgRoot['Subject']=Header('自动化报告','utf-8')
        # msgRoot.attach(att)
        msgRoot.attach(msg)
        # msg.attach(self.sendfile)


        return msg.as_string()

    def Send_email(self):
      try:
        smtp=smtplib.SMTP()
        smtp.connect(self.smtpserver,port=self.port)
        smtp.ehlo()
        # smtp.starttls()
        smtp.login(self.user,self.password)
        smtp.sendmail(self.sender,self.receivers,msg=self.attach_setup())

        smtp.quit()

      except smtplib.SMTPException :
          module_logger.exception("邮件发送失败！！",exc_info=True)
      else:
          module_logger.info("邮件发送成功！！")




if __name__ == '__main__':
#     # Send=Send_email_HTML()
#     # Send.config()
     send=Send_email_Attachment()
     send.Send_email()