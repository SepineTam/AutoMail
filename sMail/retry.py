#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : retry.py

from sMail.log import *
import time


def retry(func, *args, timeout=5):
    start_time = time.time()  # 记录开始时间
    while True:
        try:
            # result = func(*args)
            result = func(*args)
            print(func.__name__)
            write_log(f"Successfully!,{func.__name__}")
            return result
        except Exception as e:
            write_log(f"Failed!,{e}")
            if time.time() - start_time > timeout:  # 检查是否超过60秒
                write_log(f"Timeout!,function {func.__name__} took too long to succeed")
                break  # 超时，跳出循环


if __name__ == '__main__':
    print("retry function run!")


    def one():
        time.sleep(2)
        print(2+2)


    retry(one, timeout=10)
    # def wrong_func():
    #     time.sleep(1)
    #     c = 1 + str
    #
    #
    # retry(wrong_func)
    # clear('.log')
