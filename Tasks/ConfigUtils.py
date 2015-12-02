__author__ = 'luowen'

from Config.main import MainConfig
from pathlib import Path
class ConfigUtils:
    @staticmethod
    def getConfig(file):
        mainConfig = ConfigUtils.getMainConfig()

        if mainConfig.get('env'):
            print('ok')
    @staticmethod
    def getMainConfig():
        return MainConfig



ConfigUtils.getConfig("hah")