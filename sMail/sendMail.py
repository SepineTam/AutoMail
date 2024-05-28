#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : sendMail.py

import smtplib
from email.mime.text import MIMEText
from sMail.log import write_log
from sMail.config import *


LOG_FILE = log_path


# 重试函数
def retry_until_success(func, *args):
    while True:
        try:
            result = func(*args)
            write_log(f"Successfully {func.__name__}")
            return result
        except Exception as e:
            write_log(f"Failed! {e}")


# 创建SMTP服务器连接
def init_server():
    return smtplib.SMTP_SSL(host=host, port=port)


# 登录SMTP服务器
def login(server):
    server.login(email_address, password)


# 创建邮件消息
def create_message(subject, body, to):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to
    return msg


# 发送邮件
def send_email(server, msg, to):
    server.sendmail(email_address, to, msg.as_string())


# 主函数
def send_mail(to, subject, body):
    server = retry_until_success(init_server)
    retry_until_success(login, server)

    msg = create_message(subject, body, to)
    retry_until_success(send_email, server, msg, to)

    server.quit()


if __name__ == "__main__":
    send_mail(recipient, "Test Subject", "Test Body")
