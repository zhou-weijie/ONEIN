import unittest
from common import HTMLTestReportCN
from common.pathUtils import PathUtils
import os
# 将当前路径添加为python的临时环境变量
cur_path = os.path.dirname(os.path.realpath(__file__))
os.putenv("PYTHONPATH", cur_path)


class RunCase:
    def __init__(self):
        self.case_path = PathUtils().case_path
        self.report_path = PathUtils().report_path
        self.title = '万应工厂自动化测试报告'
        self.describe = '万应工厂用户端接口自动化测试报告'
        self.tester = 'Chris'

    def load_testsuite(self):
        discover = unittest.defaultTestLoader.discover(
            start_dir=self.case_path,
            pattern='testbase.py',
            top_level_dir=self.case_path
        )
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        return all_suite

    def run(self):
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_file_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title=self.title,
            description=self.describe,
            tester=self.tester
        )
        runner.run(self.load_testsuite())
        fp.close()
        return report_file_path


if __name__ == '__main__':
    report_path = RunCase().run()
