import re
import ast
import requests

from common.configUtils import ReadConfig
from common.excelUtils import ReadExcelUtils
from common.logUtils import Logger

log = Logger(logger='checkUtils').getlog()


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
        self.key_list = []
        self.item_list = []

    def get_keys(self, dict_a):
        if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
            # 如果为字典类型，则提取key存放到key_list中
            for x in range(len(dict_a)):
                temp_key = list(dict_a.keys())[x]
                temp_value = dict_a[temp_key]
                self.key_list.append(temp_key)
                self.get_keys(temp_value)  # 自我调用实现无限遍历
        elif isinstance(dict_a, list):
            # 如果为列表类型，则遍历列表里的元素，将字典类型的按照上面的方法提取key
            for k in dict_a:
                if isinstance(k, dict):
                    for x in range(len(k)):
                        temp_key = list(k.keys())[x]
                        temp_value = k[temp_key]
                        self.key_list.append(temp_key)
                        self.get_keys(temp_value)  # 自我调用实现无限遍历
        return self.key_list

    def get_items(self, dict_b):
        if isinstance(dict_b, dict):  # 使用isinstance检测数据类型
            # 如果为字典类型，则提取key存放到key_list中
            for x in range(len(dict_b)):
                temp_key = list(dict_b.keys())[x]
                temp_value = dict_b[temp_key]
                dict_items = {temp_key: temp_value}
                self.item_list.append(dict_items)
                self.get_items(temp_value)  # 自我调用实现无限遍历
        elif isinstance(dict_b, list):
            # 如果为列表类型，则遍历列表里的元素，将字典类型的按照上面的方法提取key
            for k in dict_b:
                if isinstance(k, dict):
                    for x in range(len(k)):
                        temp_key = list(k.keys())[x]
                        temp_value = k[temp_key]
                        dict_items = {temp_key: temp_value}
                        self.item_list.append(dict_items)
                        self.get_items(temp_value)  # 自我调用实现无限遍历
        return self.item_list

    def no_check(self, check_data=None):
        return self.pass_result

    def check_key(self, check_data=None):
        check_data_list = check_data.split(';')
        res_list = []  # 存放每次比较的结果
        wrong_key = []  # 存放比较失败key
        for c_data in check_data_list:
            if c_data in self.get_keys(self.ck_response.json()):
                res_list.append('pass')
            else:
                res_list.append('no pass')
                wrong_key.append(c_data)
        # log.info('响应中的keys有：{}'.format(self.get_keys(self.ck_response.json())))
        # log.info('期望结果是{}'.format(check_data))
        if 'no pass' in res_list:
            log.error('用例执行失败，{}校验未通过'.format(wrong_key))
            return self.fail_result
        else:
            return self.pass_result

    def check_keyvalue(self, check_data=None):
        ck_data_list = check_data.split(';')
        res_list = []  # 存放每次比较的结果
        wrong_items = []  # 存放比较失败 items
        for ck_data in ck_data_list:
            if ast.literal_eval(ck_data) in self.get_items(self.ck_response.json()):
                res_list.append('pass')
            else:
                res_list.append('no pass')
                wrong_items.append(ck_data)
        log.info('响应中的items有：{}'.format(self.get_items(self.ck_response.json())))
        log.info('期望结果是{}'.format(check_data))
        if 'no pass' in res_list:
            log.error('用例执行失败，{}校验未通过'.format(wrong_items))
            return self.fail_result
        else:
            return self.pass_result

    def check_regexp(self, check_data=None):
        pattern = re.compile(check_data)
        if re.findall(pattern=pattern, string=self.ck_response.text):
            return self.pass_result
        else:
            log.error('用例执行失败，%s校验未通过' % check_data)
            return self.fail_result

    def run_check(self, check_type=None, check_data=None):
        if check_type in self.ck_rules.keys():
            result = self.ck_rules[check_type](check_data)  # self.check_keyvalue(check_data)
            return result
        else:
            self.fail_result['message'] = '不支持%s判断方法' % check_type
            log.error('错误，%s' % self.fail_result.get('message'))
            return self.fail_result


# if __name__ == "__main__":
#     step_info = ReadExcelUtils("CASE").get_data()[0]
#     headers = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Content-Type": "application/json",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                           "Chrome/84.0.4147.135 Safari/537.36 "
#         }
#     res = requests.post(url=ReadConfig().getValue('Operation', 'Test') + step_info['请求地址'],headers=headers,json=ast.literal_eval(step_info['请求参数(post)']))
#     result = CheckUtils(res).run_check(step_info['期望结果类型'], step_info['期望结果'])
#     # print(type(result.ck_response.text))
#     # items = result.get_items(result.ck_response.json())
#     # keys = result.get_keys(result.ck_response.json())
#     # check_type = step_info['期望结果类型']
#     # check_data = step_info['期望结果']
#     # print(result.check_key(check_data))
#     # print(items, '\n', keys)
#     print(result)
