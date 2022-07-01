#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author: Ruinan Zhang
Version: v1.2
LastEditTime: 2022-07-01 09:35:08
E-mail: 2020801253@stu.njau.edu.cn
Copyright (c) 2022 by Ruinan Zhang, All Rights Reserved. Licensed under the GPL v3.0.
'''
from taskQueue import huey


@huey.task()
def submit_task(uid, tid):
    web_action(uid, tid)
    return tid


from facrsa_code.library.analysis.main import web_action
