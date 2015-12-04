__author__ = 'Administrator'

from Config import main
import os

class ConfigUtils:

    @staticmethod
    def getMainConfig():
        if main.MainConfig.get('env'):
            return main.MainConfig['env']
        return 'Pro'

    @staticmethod
    def getConfig(fileNameWithoutSuffix):
        env = ConfigUtils.getMainConfig()

ConfigUtils.getConfig('go')
