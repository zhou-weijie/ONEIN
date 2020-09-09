# 处理从excel中读出的测试数据，提供给paramunittest
"""
paramunittest需要的参数格式是：
{'case_id': 'case01','case_info':[按步骤的case信息]}
{'case_id': 'case02','case_info':[按步骤的case信息]}
而excel读出的测试数据格式是：
[{key: value, key: value},{}]
所以需要对数据格式进行下转换
"""
from common.excelUtils import ReadExcelUtils


class DataUtils:
    def __init__(self, sheet_name):
        self.testData = ReadExcelUtils(sheet_name).get_data()

    def getTestCaseData(self):
        testCaseDict = {}
        for row_data in self.testData:
            testCaseDict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return testCaseDict

    def testCaseDataList(self):
        testCaseList = []
        for k, v in self.getTestCaseData().items():
            one_case_dict = {"case_id": k, "case_info": v}
            testCaseList.append(one_case_dict)
        return tuple(testCaseList)


# if __name__ == "__main__":
#     testData = DataUtils('Operation').getTestCaseData()
#     print(testData.items())
