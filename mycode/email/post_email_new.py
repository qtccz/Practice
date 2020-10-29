#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import smtplib
import sys
import time
from email.header import Header
from email.mime.text import MIMEText


# 收件人列表
mail_to_list = [
    "xxxx1@xxx.com",
    "xxxx2@xxx.com",
]

# 设置服务器
smtp_server = "smtp.163.com"
# 用户
mail_user = "xxxx@163.com"
# 口令
mail_pass = "xxxx"


def send_mail(to_list, sub, content):
    """
    :param to_list: 收件人
    :type to_list:
    :param sub: 主题
    :type sub:
    :param content: 邮件内容
    :type content:
    :return:
    :rtype:
    """
    # 使用默认plain纯文本格式创建实例对象
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = Header(sub, 'utf-8')  # 消息主题
    header = "<"+mail_user+">"      # 显示发件人
    msg['From'] = header            # 发件人
    msg['To'] = ";".join(to_list)   # 收件人
    try:
        s = smtplib.SMTP(smtp_server, 25)
        s.login(mail_user, mail_pass)      # 登陆服务器
        s.sendmail(header, to_list, msg.as_string())  # 发送邮件
        print("发件人:{}\t收件人:{}\t消息:{}".format(header, to_list, msg.as_string()))
        s.close()
    except smtplib.SMTPException as e:
        print(str(e))


def main():
    with open("data.csv", encoding="utf-8") as f:
        lines = f.readlines()
        send_msg = ""
        for line in lines:
            msg = line.strip()
            if msg != "search_source,count_num":
                source, count_num = msg.split(",")
                send_msg += "采集源:【{}】\t采集数量:【{}】条\t\n".format(source, count_num)

        if send_msg != "":
            send_mail(mail_to_list, "{}采集日报".format(time.strftime("%Y-%m-%d")), send_msg)
        else:
            send_msg = "采集源:【暂无更新】\t采集数量:【暂无更新】\t"
            send_mail(mail_to_list, "{}采集日报".format(time.strftime("%Y-%m-%d")), send_msg)
    sys.exit(0)


if __name__ == '__main__':
    main()

