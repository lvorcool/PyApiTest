# coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global password
    global smtp_server
    global smtp_port
    # 配置信息,发邮件服务器主机地址,发邮件邮箱地址,发邮件的密码,发邮件服务器的端口号
    send_user = "发邮件邮箱地址"
    password = "发邮件的密码"
    smtp_server = '发邮件服务器主机地址'
    smtp_port = 25


    def send_mail(self, user_list, sub, content):
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("王",'utf-8')
        message['Subject'] = Header(sub,'utf-8')
        message['To'] = Header("测试","utf-8")
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.set_debuglevel(1)
        server.login(send_user, password)
        server.sendmail(send_user, user_list, message.as_string())
        server.quit()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        user_list = ['接收邮件地址']
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个,通过个数为%s,失败个数为%s,通过率为s%,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)

