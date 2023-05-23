import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class SEND:
    def __init__(self):
        self.Sender = '1154622707@qq.com'

    def Send_Email_C(self, User):
        ret = True
        msg_detail = '简洁新闻提醒您，投稿成功！ '
        try:
            msg = MIMEText(msg_detail, 'plain', 'utf-8')
            msg['From'] = formataddr(["简洁新闻", self.Sender])
            msg['To'] = formataddr(["receive@163.com", User])
            msg['Subject'] = "通知消息"

            server = smtplib.SMTP("smtp.qq.com", 25)
            server.login(self.Sender, "vqluncjpkkpggeid")
            server.sendmail(self.Sender, [User], msg.as_string())
            server.quit()

        except Exception as e:
            ret = False

        return ret

    def Send_Email_U(self, User):
        ret = True
        msg_detail = '简洁新闻提醒您，订阅成功！ '
        try:
            msg = MIMEText(msg_detail, 'plain', 'utf-8')
            msg['From'] = formataddr(["简洁新闻", self.Sender])
            msg['To'] = formataddr(["receive@163.com", User])
            msg['Subject'] = "通知消息"

            server = smtplib.SMTP("smtp.qq.com", 25)
            server.login(self.Sender, "vqluncjpkkpggeid")
            server.sendmail(self.Sender, [User], msg.as_string())
            server.quit()

        except Exception as e:
            ret = False

        return ret
