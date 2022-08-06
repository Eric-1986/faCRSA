#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author: Ruinan Zhang
Version: v1.2
LastEditTime: 2022-07-01 09:35:26
E-mail: 2020801253@stu.njau.edu.cn
Copyright (c) 2022 by Ruinan Zhang, All Rights Reserved. Licensed under the GPL v3.0.
'''
from facrsa_code.library.util.sqliteUtil import sqliteUtil
import zipfile
import os
from pathlib import Path


class interact():
    def __init__(self, uid, tid, type):
        self.uid = str(uid)
        self.tid = str(tid)
        self.info = self.get_task_info()

    def get_task_info(self):
        sql = 'select * from task where tid ="' + str(self.tid) + '"' + ' and uid ="' + str(self.uid) + '"'
        res = sqliteUtil().fetch_one(sql)
        return res

    def re_img_name(self, folder_str):
        filelist = os.listdir(folder_str + "initial")
        for img in filelist:
            with sqliteUtil() as um:
                sql = 'SELECT image FROM result WHERE re_img = ' + '"' + img + '"' + 'and tid=' + self.tid
                res = um.fetch_one(sql)
            original = folder_str + "initial/" + img
            rename = folder_str + "initial/" + res['image']
            os.rename(original, rename)

    def initial_analysis(self):
        factor = self.info['factor']
        mail = self.info['email']
        private_plugin = self.info['private_plugin']
        return factor, mail, private_plugin
