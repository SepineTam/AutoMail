#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : log_export.py

import pandas as pd
from datetime import datetime


def export_log():
    # get export path
    home = "export_log"

    # get log path
    from sMail.config import log_path

    # convert ori file
    df = pd.read_csv(log_path, encoding='utf-8', decimal=',')

    # make new path
    now_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    new_name = f"{now_time}.log.csv"
    new_path = f"{home}/{new_name}"

    # save as .csv file
    df.to_csv(new_path, index=False, encoding='utf-8')


if __name__ == '__main__':
    export_log()
