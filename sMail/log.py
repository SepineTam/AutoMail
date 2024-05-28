#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : log.py

from datetime import datetime


def write_log(response, LOG_FILE='.log'):
    with open(LOG_FILE, 'a') as log_file:
        current_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        log_file.write(f"{current_time},{response}\n")


def clear(path):
    try:
        # 使用写入模式打开文件，这会自动清空文件内容
        with open(path, 'w') as file:
            pass
        print(f"{path} 文件已成功清空。")
    except Exception as e:
        print(f"清空文件时出错: {e}")


if __name__ == '__main__':
    resp = 'test'
    write_log(resp)
