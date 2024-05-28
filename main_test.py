#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : main_test.py

from sMail.config import mail_config as config
from sMail.log import clear
from sMail.temp import send_mail
from sMail.config import log_path


def clear_log():
    if input("Are you sure you want to delete the log?(Y/n)").upper() == "Y":
        clear(log_path)
    else:
        pass


def main():
    print("Hello World!")
    send_mail()
    print("Bomb!")


if __name__ == '__main__':
    main()
