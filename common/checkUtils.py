import re
import ast
import requests
from common.excelUtils import ReadExcelUtils
from common.configUtils import ReadConfig



class CheckUtils:
    def __init__(self, check_response=None):
        self.ck_response = check_response
        self.ck_rules = {
            '无': self.no_check,
            'json键是否存在': self.check_key,
            'json键值对': self.check_keyvalue,
            '正则匹配': self.check_regexp
        }
        self.pass_result = {
            'code': 0,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': True,
            'message': '用例执行成功'  # 扩展作为日志输出等
        }
        self.fail_result = {
            'code': 2,
            'response_code': self.ck_response.status_code,
            'response_headers': self.ck_response.headers,
            'response_body': self.ck_response.text,
            'check_result': False,
            'message': '用例执行失败'  # 扩展作为日志输出等
        }

    def no_check(self, check_data=None):
        return self.pass_result

    def check_key(self, check_data=None):
        check_data_list = check_data.split(';')
        res_list = []  # 存放每次比较的结果
        wrong_key = []  # 存放比较失败key
        for c_data in check_data_list:
            if c_data in self.ck_response.json().keys():
                res_list.append('pass')
            else:
                res_list.append('no pass')
                wrong_key.append(c_data)
        if 'no pass' in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self, check_data=None):
        res_list = []  # 存放每次比较的结果
        wrong_items = []  # 存放比较失败 items
        for check_item in ast.literal_eval(check_data).items():
            if check_item in self.ck_response.json().items():
                res_list.append('pass')
            else:
                res_list.append('no pass')
                wrong_items.append(check_item)
        if 'no pass' in res_list:
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self, check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern, string=self.ck_response.text):
            return self.pass_result
        else:
            return self.fail_result

    def run_check(self, check_type=None, check_data=None):
        if check_type in self.ck_rules.keys():
            result = self.ck_rules[check_type](check_data)  # self.check_keyvalue(check_data)
            return result
        else:
            self.fail_result['message'] = '不支持%s判断方法' % check_type
            return self.fail_result


if __name__ == "__main__":
    step_info = ReadExcelUtils("Operation").get_data()[0]
    headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.135 Safari/537.36 "
        }
    res = requests.post(url=ReadConfig().getValue('Operation', 'Test') + step_info['请求地址'],headers=headers,data=step_info['请求参数(post)'])
    print(res.json().items())

    # result = CheckUtils(check_response=res)
    # check_type = step_info['期望结果类型']
    # check_data = step_info['期望结果']
    # print(result.check_key(check_data))
