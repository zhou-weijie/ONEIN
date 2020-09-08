"""
登录运营平台，通过运营平台的免登接口进入设计平台
"""
from common.excelUtils import ReadExcelUtils
from common.requestUtils import RequestUtils


class LoginUtils:
    def __init__(self):
        self.sec = "Operation"
        self.option = "Test"
        self.step_infos = ReadExcelUtils(self.sec).get_data()
        self.re = RequestUtils(sec=self.sec, option=self.option)

    @property
    def getCode(self):
        for step_info in self.step_infos:
            res = self.re.sendRequest(step_info)
        code = self.re.temporary_variables.get('code')
        return code


if __name__ == '__main__':
    login = LoginUtils()
    print(login.getCode)
