__author__ = 'luowen'

import os, time
from Utils import LogUtils
class LockUtils:

    @staticmethod
    def isRunning(taskName):
        lockFile = LockUtils.getLockFile(taskName)
        if os.path.isfile(lockFile):
            fileHandle = open(lockFile, mode="rw")
            lockContent = fileHandle.readline()
            if lockContent == "":  # if file is empty write current timestamp in it
                fileHandle.write(str(time.time()))
                fileHandle.close()
                return True
            fileHandle.close()  # close file stream

            timeStamp = int(lockContent)
            currentTimeStamp = time.time()
            if currentTimeStamp - timeStamp > 3600 * 2:
                os.remove(lockFile)
                LogUtils.LogUtils.error("The lock file is expired two hours", "lock")
                return False
            return True
        else:
            return False

    @staticmethod
    def lock(taskName):
        lockFile = LockUtils.getLockFile(taskName)
        if LockUtils.isRunning(taskName):
            LogUtils.error("can not lock a task when the task is running", "lock")
            return False
        with open(lockFile, mode='w') as fileHandle:
            fileHandle.write(str(time.time()))
        return True

    @staticmethod
    def unlock(taskName):
        lockFile = LockUtils.getLockFile(taskName)
        return os.remove(lockFile)

    @staticmethod
    def getLockFile(taskName):
        return "{0}/Locks/{1}.lock".format(os.path.abspath(os.curdir), taskName)
