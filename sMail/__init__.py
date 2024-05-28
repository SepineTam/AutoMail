#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : __init__.py.py

from sMail.log import write_log
from sMail.log import clear

from sMail.retry import retry

from sMail.send_mail import Server
from sMail.send_mail import send_mail


def send():
    server = Server()
    try:
        server.start_server()
        response = "successful start server"
        print(response)
        write_log(response)

    except Exception as e:
        print(e)
        write_log(e)

    try:
        server.login()
        response = "successful login"
        print(response)
        write_log(response)

    except Exception as e:
        print(e)
        write_log(e)

    try:
        msg = server.creat_msg(
            sub='Test Mail',
            body='This is a test message.'
        )

        server.send_msg(msg)
        response = "successful send mail"
        print(response)
        write_log(response)

    except Exception as e:
        print(e)
        write_log(e)

    try:
        server.quit()
        print("successful quit")

    except Exception as e:
        print(e)
        write_log(e)
