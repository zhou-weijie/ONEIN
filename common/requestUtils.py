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
from requests.exceptions import ProxyError, RequestException
from common.checkUtils import CheckUtils
from common.configUtils import ReadConfig
from common.excelUtils import ReadExcelUtils
from common.logUtils import Logger
import jsonpath

log = Logger(logger='sendRequest').getlog()


class RequestUtils:
    # 初始化一个request对象
    def __init__(self, sec, option):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.135 Safari/537.36 "
        }
        self.host = ReadConfig().getValue(sec, option)
        self.temporary_variables = {}

    # 判断是否需要补充请求头信息
    def headerUtils(self, step_info):
        if step_info['是否补充请求头']:
            self.headers['authorization'] = self.temporary_variables['type'] + ' ' + self.temporary_variables['access_token']
            # self.headers['appid'] = ReadConfig().getAppId
            # self.headers['appname'] = ReadConfig().getAppName
            # log.info('请求头信息更新，目前请求头信息为：%s' % self.headers)
        else:
            # log.info('请求头信息保持不变，目前请求头信息为：%s' % self.headers)
            pass

    # 获取响应
    def _getResponse(self, step_info):
        self._setVariable(step_info)
        url = self.host + step_info['请求地址']
        self.headerUtils(step_info)
        # log.info('请求信息为：%s %s?%s' % (step_info['请求方式'], url, step_info['请求参数(get)']))
        try:
            if step_info["请求方式"] == "GET":
                if step_info["请求参数(get)"] == '':
                    res = requests.get(
                        url=url,
                        headers=self.headers
                    )
                    res.encoding = res.apparent_encoding
                    return res
                else:
                    res = requests.get(
                        url=url,
                        headers=self.headers,
                        params=ast.literal_eval(step_info['请求参数(get)'])
                    )
                    res.encoding = res.apparent_encoding
                    return res
            elif step_info["请求方式"] == "POST":
                if step_info['请求参数(get)'] == '':
                    res = requests.post(
                        url=url,
                        headers=self.headers,
                        data=step_info['请求参数(post)']
                    )
                    res.encoding = res.apparent_encoding
                    return res
                else:
                    res = requests.post(
                        url=url,
                        headers=self.headers,
                        params=step_info['请求参数(get)'],
                        data=step_info['请求参数(post)']
                    )
                    res.encoding = res.apparent_encoding
                    return res
            elif step_info["请求方式"] == "PUT":
                res = requests.put(
                    url=url,
                    headers=self.headers,
                    params=step_info['请求参数(get)'],
                    data=step_info['请求参数(post)']
                )
                res.encoding = res.apparent_encoding
                return res
            elif step_info["请求方式"] == "DELETE":
                res = requests.delete(
                    url=url,
                    headers=self.headers
                )
                res.encoding = res.apparent_encoding
                return res
        except ProxyError as e:
            log.error('[%s]请求：代理错误异常' % (step_info["请求地址"]))
        except ConnectionError as e:
            log.error('[%s]请求：连接超时异常' % (step_info["请求地址"]))
        except RequestException as e:
            log.error('[%s]请求：Request异常，原因：%s' % (step_info["请求地址"], e.__str__()))
        except Exception as e:
            log.error('[%s]请求：系统异常，原因：%s' % (step_info["请求地址"], e.__str__()))

    # 判断响应是否是json格式
    def _isJson(self, step_info):
        res = self._getResponse(step_info)
        try:
            json.loads(res.text)
        except ValueError as e:
            return False
        return True

    # 通过传值变量获取响应中的值,存入temporary_variables字典中
    def _getTransferVariable(self, step_info):
        res = self._getResponse(step_info)
        if step_info["取值方式"] == "json取值":
            # if self._isJson(step_info):
            try:
                get_value_code_list = step_info["取值代码"].split(";")
                transfer_value_variable_list = step_info["传值变量"].split(";")
                for i in range(0, len(get_value_code_list)):
                    value = jsonpath.jsonpath(res.json(), get_value_code_list[i])[-1]
                    self.temporary_variables[transfer_value_variable_list[i]] = str(value)
            except Exception as e:
                log.error("发生错误，%s" % e)
            # else:
            #     log.error("响应非json格式，请勿使用json取值方式")
        elif step_info["取值方式"] == "正则取值":
            get_value_code_list = step_info["取值代码"].split(";")
            transfer_value_variable_list = step_info["传值变量"].split(";")
            for i in range(0, len(get_value_code_list)):
                value = re.findall(get_value_code_list[i], res.text)[-1]
                self.temporary_variables[transfer_value_variable_list[i]] = value
        elif step_info["取值方式"] == "无":
            pass

    # 替换传参中的变量
    def _setVariable(self, step_info):
        # 替换url中的变量
        url__variable_list = re.findall('\\${\w+}', step_info['请求地址'])
        if url__variable_list:
            for url__variable in url__variable_list:
                step_info['请求地址'] = step_info['请求地址'] \
                    .replace(url__variable, self.temporary_variables.get(url__variable[2:-1]))
        # 替换请求参数(get)中的变量
        getParam_variable_list = re.findall('\\${\w+}', step_info['请求参数(get)'])
        if getParam_variable_list:
            for getParam_variable in getParam_variable_list:
                step_info['请求参数(get)'] = step_info['请求参数(get)'] \
                    .replace(getParam_variable, self.temporary_variables.get(getParam_variable[2:-1]))
        # 替换请求参数(get)中的变量
        postParam_variable_list = re.findall('\\${\w+}', step_info['请求参数(post)'])
        if postParam_variable_list:
            for postParam_variable in postParam_variable_list:
                step_info['请求参数(post)'] = step_info['请求参数(post)'] \
                    .replace(postParam_variable, self.temporary_variables.get(postParam_variable[2:-1]))
        # 替换取值代码中的变量
        code_variable_list = re.findall('\\${\w+}', step_info['取值代码'])
        if code_variable_list:
            for code_variable in code_variable_list:
                step_info['取值代码'] = step_info['取值代码'] \
                    .replace(code_variable, self.temporary_variables.get(code_variable[2:-1]))

    def sendRequest(self, step_info):
        res = self._getResponse(step_info)
        self._getTransferVariable(step_info)
        result = CheckUtils(res).run_check(step_info['期望结果类型'], step_info['期望结果'])
        return result

    def request_by_step(self, step_infos):
        temp_result_list = []
        for step_info in step_infos:
            temp_result = self.sendRequest(step_info)
            temp_result_list.append(temp_result)
            print(temp_result_list)
        return temp_result_list


if __name__ == "__main__":
    case_info = ReadExcelUtils("Operation").get_data()
    RequestUtils('Operation', 'TEST').request_by_step(case_info)
