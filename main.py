#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : main.py

from sMail import *
from sMail.config import log_path


def clear_log():
    if input("Are you sure you want to delete the log?(Y/n)").upper() == "Y":
        clear(log_path)
    else:
        pass


def main():
    print("BEGIN...")
    send()
    print("OVER...")


if __name__ == "__main__":
    main()
