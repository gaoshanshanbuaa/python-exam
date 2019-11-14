import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def read_csv(filename):
    with open(filename,"r") as f:
        next(f)
        reader = csv.reader(f)
        address_list = dict()
        for line in reader:
            username = line[0]
            email = line[1]
            address_list[username] = email
        return address_list

def email_serve(mail_host, mail_user, mail_pass, sender, receivers):
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("测试程序", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == "__main__":
    filename = 'data.csv'
    address_list = read_csv(filename)
    keys = address_list.keys()

    mail_host = "smtp.xxx.cn"  # 设置服务器
    mail_user = "xxxxx@xxxx.cn"  # 用户名
    mail_pass = "xxxxx"  # 口令

    sender = 'xxxx@xxxx.cn'   #发送邮件的邮箱地址
    usernames = ['xxxx', 'xxxx']  #接收邮件的邮箱地址
    receivers = []
    for username in usernames:
        if username in keys:
            receivers.append(address_list[username])

    email_serve(mail_host, mail_user, mail_pass, sender, receivers)





