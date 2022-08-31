#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Author: Ruinan Zhang
Version: v1.2
LastEditTime: 2022-07-01 12:05:33
E-mail: 2020801253@stu.njau.edu.cn
Copyright (c) 2022 by Ruinan Zhang, All Rights Reserved. Licensed under the GPL v3.0.
'''
from huey import CancelExecution
from huey.signals import SIGNAL_ERROR

from task_queue import huey

@huey.task()
def submit_task(uid, tid):
    try:
        web_action(uid, tid)
    except (PermissionError, FileExistsError, IndexError, KeyError, NameError) as e:
        raise CancelExecution()

@huey.signal()
def print_signal_args(signal, task, exc=None):
    if signal == SIGNAL_ERROR:
        print('%s - %s - exception: %s' % (signal, task.id, exc))
    else:
        print('%s - %s' % (signal, task.id))


from facrsa_code.library.analysis.main import web_action
