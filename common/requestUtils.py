# author:Cris
# date:2020-07-06
# encode:utf-8
"""
1.依据excel用例中的请求方式完成不同的请求
2.请求头的处理（不同的请求的请求头不同，是否需要写在excel的用例中？）：
    i.accept、accept-encoding、Content-Type、user-agent是固定的
    ii.authorization是调用登录接口后获取响应中的token，再拼接而成
    iii.appid与appname是依据选择的应用不同而不同的，需要做成可配置
3.响应的处理：
    i.通过正则表达式或者jsonpath获取响应中的某些值，可作为下一个接口的入参
    ii.key放在excel中，通过key取对应的value
    iii.响应参数非json格式时的处理
4.断言
    i.响应信息中需要的业务参数的key存放再excel中，作为执行结果
    ii.期望的值填写再excel中，作为期望结果
问题：
变量入参处理
非json格式响应处理
"""
import ast
import json
import re
import requests
import time
from requests.exceptions import ProxyError, RequestException
from common.checkUtils import CheckUtils
from common.configUtils import ReadConfig
from common.excelUtils import ReadExcelUtils
from common.logUtils import Logger
import jsonpath

log = Logger(logger='sendRequest').getlog()


class RequestUtils:
    # 初始化一个request对象
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.135 Safari/537.36 "
        }
        self.temporary_variables = {}

    # 判断是否需要补充请求头信息
    def headerUtils(self, case_info):
        if case_info['是否补充请求头']:
            self.headers['authorization'] = self.temporary_variables['type'] + ' ' + self.temporary_variables['access_token']
            # log.info('请求头信息更新，目前请求头信息为：%s' % self.headers)
        else:
            # log.info('请求头信息保持不变，目前请求头信息为：%s' % self.headers)
            pass

    # 获取响应
    def _getResponse(self, case_info):
        self._addTimeStampToTemp()
        self.setVariable(case_info)
        url = ReadConfig().getValue(sec=case_info['请求服务'], option=case_info['请求环境']) + case_info['请求地址']
        self.headerUtils(case_info)
        log.info('请求方式为：%s\n请求地址为：%s?%s\n请求参数为：%s' % (case_info['请求方式'], url, case_info['请求参数(get)'], case_info['请求参数(post)']))
        try:
            if case_info["请求方式"] == "GET":
                if case_info["请求参数(get)"] == '':
                    res = requests.get(
                        url=url,
                        headers=self.headers
                    )
                    res.encoding = res.apparent_encoding
                    log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                    return res
                else:
                    res = requests.get(
                        url=url,
                        headers=self.headers,
                        params=ast.literal_eval(case_info.get('请求参数(get)'))
                    )
                    res.encoding = res.apparent_encoding
                    log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                    return res
            elif case_info["请求方式"] == "POST":
                if case_info['请求参数(post)'] == '':
                    if case_info['请求参数(get)'] == '':
                        res = requests.post(
                            url=url,
                            headers=self.headers
                        )
                        res.encoding = res.apparent_encoding
                        log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                        return res
                    else:
                        res = requests.post(
                            url=url,
                            headers=self.headers,
                            params=case_info['请求参数(get)']
                        )
                        res.encoding = res.apparent_encoding
                        log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                        return res
                else:
                    if case_info['请求参数(get)'] == '':
                        res = requests.post(
                            url=url,
                            headers=self.headers,
                            json=ast.literal_eval(case_info.get('请求参数(post)'))
                        )
                        res.encoding = res.apparent_encoding
                        log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                        return res
                    else:
                        res = requests.post(
                            url=url,
                            headers=self.headers,
                            params=case_info['请求参数(get)'],
                            json=ast.literal_eval(case_info['请求参数(post)'])
                        )
                        res.encoding = res.apparent_encoding
                        log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                        return res
            elif case_info["请求方式"] == "PUT":
                res = requests.post(
                    url=url,
                    headers=self.headers,
                    params=case_info['请求参数(get)'],
                    json=ast.literal_eval(case_info['请求参数(post)'])
                )
                res.encoding = res.apparent_encoding
                log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                return res
            elif case_info["请求方式"] == "DELETE":
                res = requests.delete(
                    url=url,
                    headers=self.headers
                )
                res.encoding = res.apparent_encoding
                log.info('响应状态码为：%s\n响应信息为：%s' % (res.status_code, res.text))
                return res
        except ProxyError as e:
            log.error('[%s]请求：代理错误异常' % (case_info["请求地址"]))
        except ConnectionError as e:
            log.error('[%s]请求：连接超时异常' % (case_info["请求地址"]))
        except RequestException as e:
            log.error('[%s]请求：Request异常，原因：%s' % (case_info["请求地址"], e.__str__()))
        except Exception as e:
            log.error('[%s]请求：系统异常，原因：%s' % (case_info["请求地址"], e.__str__()))

    # 判断响应是否是json格式
    # def _isJson(self, res):
    #     try:
    #         json.loads(res.text)
    #     except ValueError as e:
    #         return False
    #     return True

    # 蒋时间戳作为一个变量，存入temporary_variables字典中
    def _addTimeStampToTemp(self):
        timestamp = int(time.time())
        self.temporary_variables['timestamp'] = str(timestamp)

    # 通过传值变量获取响应中的值,存入temporary_variables字典中
    def _getTransferVariable(self, case_info, res):
        if case_info["取值方式"] == "json取值":
            try:
                get_value_code_list = case_info["取值代码"].split(";")
                transfer_value_variable_list = case_info["传值变量"].split(";")
                for i in range(0, len(get_value_code_list)):
                    value = jsonpath.jsonpath(res.json(), get_value_code_list[i])[-1]
                    self.temporary_variables[transfer_value_variable_list[i]] = str(value)
            except Exception as e:
                log.error("发生错误，%s" % e)
        elif case_info["取值方式"] == "正则取值":
            try:
                get_value_code_list = case_info["取值代码"].split(";")
                transfer_value_variable_list = case_info["传值变量"].split(";")
                for i in range(0, len(get_value_code_list)):
                    value = re.findall(get_value_code_list[i], res.text)[-1]
                    self.temporary_variables[transfer_value_variable_list[i]] = value
            except Exception as e:
                log.error("发生错误，%s" % e)
        elif case_info["取值方式"] == "无":
            pass

    # 替换变量
    def setVariable(self, case_info):
        # 替换url中的变量
        url__variable_list = re.findall('\\${\w+}', case_info['请求地址'])
        if url__variable_list:
            for url__variable in url__variable_list:
                case_info['请求地址'] = case_info['请求地址'] \
                    .replace(url__variable, self.temporary_variables.get(url__variable[2:-1]))
                # log.info("将%s替换为%s，替换请求地址成功！" % (url__variable, self.temporary_variables.get(url__variable[2:-1])))
        # 替换请求参数(get)中的变量
        getParam_variable_list = re.findall('\\${\w+}', case_info['请求参数(get)'])
        if getParam_variable_list:
            for getParam_variable in getParam_variable_list:
                case_info['请求参数(get)'] = case_info['请求参数(get)'] \
                    .replace(getParam_variable, self.temporary_variables.get(getParam_variable[2:-1]))
                # log.info("将%s替换为%s，替换请求参数(get)成功！" % (getParam_variable, self.temporary_variables.get(getParam_variable[2:-1])))
        # 替换请求参数(post)中的变量
        postParam_variable_list = re.findall('\\${\w+}', case_info['请求参数(post)'])
        if postParam_variable_list:
            for postParam_variable in postParam_variable_list:
                case_info['请求参数(post)'] = case_info['请求参数(post)'] \
                    .replace(postParam_variable, self.temporary_variables.get(postParam_variable[2:-1]))
                # log.info("将%s替换为%s，替换请求参数(post)成功！" % (postParam_variable, self.temporary_variables.get(postParam_variable[2:-1])))
        # 替换取值代码中的变量
        code_variable_list = re.findall('\\${\w+}', case_info['取值代码'])
        if code_variable_list:
            for code_variable in code_variable_list:
                case_info['取值代码'] = case_info['取值代码'] \
                    .replace(code_variable, self.temporary_variables.get(code_variable[2:-1]))
                # log.info("将%s替换为%s，替换取值代码成功！" % (code_variable, self.temporary_variables.get(code_variable[2:-1])))
        # 替换期望结果中的变量
        result_variable_list = re.findall('\\${\w+}', case_info['期望结果'])
        if result_variable_list:
            for result_variable in result_variable_list:
                case_info['期望结果'] = case_info['期望结果'] \
                    .replace(result_variable, self.temporary_variables.get(result_variable[2:-1]))
                # log.info("将%s替换为%s，替换期望结果成功！" % (result_variable, self.temporary_variables.get(result_variable[2:-1])))

    def sendRequest(self, case_info):
        res = self._getResponse(case_info)
        self._getTransferVariable(case_info, res)
        # log.info('此时变量有：%s' % self.temporary_variables)
        result = CheckUtils(res).run_check(case_info['期望结果类型'], case_info['期望结果'])
        return result

    def request_by_step(self, case_infos):
        temp_result_list = []
        for case_info in case_infos:
            temp_result = self.sendRequest(case_info)
            temp_result_list.append(temp_result)
            print(temp_result_list)
        return temp_result_list


# if __name__ == "__main__":
#     case_info = ReadExcelUtils("CASE").get_data()
#     RequestUtils('Operation', 'TEST').request_by_step(case_info)
