from sMail.sendMail import send_mail
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime


def main():
    # 加载环境变量
    load_dotenv()

    # 获取配置信息
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')
    recipient = os.getenv('RECIPIENT_EMAIL')
    port = int(os.getenv('SMTP_PORT'))
    host = os.getenv('SMTP_SERVER')

    # 日志文件路径
    LOG_FILE = ".log"
    send_mail(recipient, "Test Subject", "Test Body")


if __name__ == "__main__":
    main()
