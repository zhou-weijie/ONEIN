import unittest
import warnings
from common.requestUtils import RequestUtils
from common.logUtils import Logger
import paramunittest
from common.dataUtils import DataUtils

# 初始化一个日志对象
log = Logger(logger='TestBase').getlog()

case_infos = DataUtils('CASE').testCaseDataList()


@paramunittest.parametrized(
    *case_infos
)
class TestBase(paramunittest.ParametrizedTestCase):
    # 登录获取token、拼接出authorization
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_run(self):
        log.info("测试用例[ %s ]开始执行" % (str(self.case_info[0].get("测试用例编号"))+self.case_info[0].get("测试用例名称")))
        self._testMethodName = self.case_info[0].get('编号')
        self._testMethodDoc = self.case_info[0].get('用例名称')
        results = RequestUtils().request_by_step(self.case_info)
        for result in results:
            self.assertTrue(result.get('check_result'), result.get('message'))


if __name__ == '__main__':
    unittest.main()
