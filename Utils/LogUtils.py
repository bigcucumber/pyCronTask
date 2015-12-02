__author__ = 'luowen'

import logging, os
import datetime

class LogUtils:
    "log utils tools"

    @staticmethod
    def configLog(logName):
        log = logging.getLogger(logName)
        log.setLevel(logging.DEBUG)

        dateString = datetime.date.today().strftime("%Y%m%d")
        logFileName = "{0:s}/Logs/{1:s}-{2}.log".format(os.path.abspath(os.curdir), logName, dateString)
        logHandle = logging.FileHandler(logFileName)

        format = logging.Formatter("[%(asctime)s]:%(levelname)s:%(name)s:%(message)s")
        logHandle.setFormatter(format)
        log.addHandler(logHandle)
        return log

    @staticmethod
    def info(message, logName = "app"):
        log = LogUtils.configLog(logName)
        log.info(message)

    @staticmethod
    def warning(message, logName = "app"):
        log = LogUtils.configLog(logName)
        log.warning(message)

    @staticmethod
    def debug(message, logName = "app"):
        log = LogUtils.configLog(logName)
        log.debug(message)

    @staticmethod
    def error(message, logName = "app"):
        log = LogUtils.configLog(logName)
        log.error(message)

