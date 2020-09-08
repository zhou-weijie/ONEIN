import json
import unittest
import warnings
import requests
from common.configUtils import ReadConfig
from common.dataUtils import DataUtils
import paramunittest
from public.loginUtils import LoginUtils

case_infos = DataUtils('Admin').testCaseDataList()


@paramunittest.parametrized(
    *case_infos
)
class APITest(paramunittest.ParametrizedTestCase):
    # 登录获取token、拼接出authorization
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_api_common_function(self):
        """测试描述"""
        self._testMethodName = self.case_info[0].get('编号')
        self._testMethodDoc = self.case_info[0].get('用例名称')
        for case_info_1 in self.case_info:
            url = ReadConfig().getValue(sec='Admin', option='TEST') + case_info_1['请求地址']
            data = case_info_1['请求参数']
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br",
                "Content-Type": "application/json; charset=utf-8",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/83.0.4103.116 Safari/537.36 ",
                "authorization": LoginUtils().getToken,
                "appid": ReadConfig().getAppId,
                "appname":ReadConfig().getAppName
            }
            res = requests.post(url=url, headers=headers, data=data.encode('utf-8'))
            print(json.loads(res.text))


if __name__ == '__main__':
    unittest.main()
