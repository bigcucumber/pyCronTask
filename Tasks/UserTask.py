__author__ = 'luowen'

import time
from Utils import LogUtils, LockUtils
class UserTask:
    label = "UserTask"
    def start(self, timeStamp):
        LogUtils.LogUtils.info("UserTask Start.")
        time.sleep(3)

        if LockUtils.LockUtils.isRunning(UserTask.label):
            LogUtils.LogUtils.error("UserTask is running")
            exit(1)

        LockUtils.LockUtils.lock(UserTask.label)


        LogUtils.LogUtils.info("UserTask End.")

