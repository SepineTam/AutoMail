#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : send_mail.py

import smtplib
from email.mime.text import MIMEText
from sMail.retry import retry


class Server:
    def __init__(self):
        self._load_config()
        self.server = None

    def _load_config(self):
        from sMail import config
        self.port = config.port
        self.host = config.host

        self.username = config.username
        self.email_address = config.email_address
        self.password = config.password

        if type(config.recipient) is list:
            self.recipients = config.recipient
        elif type(config.recipient) is str:
            self.recipients = [config.recipient]
        else:
            self.recipients = []

        self.log = config.log_path

    def start_server(self):
        if self.port == 465:
            self.server = smtplib.SMTP_SSL(
                host=self.host, port=self.port
            )
            # response = "Successfully started SMTP server on port {}".format(self.port)
        elif self.port == 587:
            self.server = smtplib.SMTP(
                host=self.host, port=self.port
            )
            # response = "Successfully started SMTP server on port {}".format(self.port)
        else:
            response = "Did not recognize port number, it is outside 465 and 587"
        # return self.server
        # write_log(response, self.log)

    def login(self):
        # print(self.server)
        self.server.login(self.email_address, self.password)

    def creat_msg(self, sub, body):
        msg = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = f'{self.username} <{self.email_address}>'
        msg['To'] = ', '.join(self.recipients)
        return msg

    def send_msg(self, msg):
        for receiver in self.recipients:
            self.server.sendmail(self.email_address, receiver, msg.as_string())

    def quit(self):
        self.server.quit()


def send_mail():
    # clear('.log')
    server = Server()

    retry(server.start_server)
    retry(server.login)
    msg = server.creat_msg(
        'Test Mail', 'This is a test message.'
    )
    retry(server.send_msg, msg)
    print('successful send mail')


if __name__ == '__main__':
    send_mail()
