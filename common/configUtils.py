import configparser
from common.logUtils import Logger
from common.pathUtils import PathUtils

# 定义日志变量
log = Logger(logger='readConfig').getlog()


class ReadConfig:
    file_name = PathUtils().config_path + '\\config.ini'

    # 读取config.ini中的信息
    def __init__(self):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(self.file_name, encoding='utf-8')
            # log.info('打开文件:' + self.file_name + '成功！')
        except FileNotFoundError as e:
            log.error('未找到文件:' + self.file_name + '!')

    # 依据输入值读取config.ini中的host地址，并返回
    def getValue(self, sec, option):
        host = self.config.get(sec, option)
        return host

    @property
    def getAppName(self):
        return self.config.get('App', 'AppName')

    @property
    def getAppId(self):
        return self.config.get('App', 'AppId')

# if __name__ == '__main__':
#     config = ReadConfig()
#     host = config.getHost('Admin', 'Test')
#     print(type(host))
