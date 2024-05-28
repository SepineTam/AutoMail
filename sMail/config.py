#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : mail_config.py

import os
from dotenv import load_dotenv

load_dotenv()

log_path = '.log'

username = os.getenv('USERNAME')
email_address = os.getenv('EMAIL_USERNAME')
password = os.getenv('EMAIL_PASSWORD')
recipient = os.getenv('RECIPIENT_EMAIL')
port = int(os.getenv('SMTP_PORT'))
host = os.getenv('SMTP_SERVER')

mail_config = {
    "username": username,
    "port": port,
    "host": host,
    "email_address": email_address,
    "password": password,
    "recipient": recipient
}

