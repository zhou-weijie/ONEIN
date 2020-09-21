import json
import jsonpath
import requests
import re
from common.excelUtils import ReadExcelUtils

temp_variables = {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                                  '.eyJleHAiOjE1OTg4NjQ0MDAsImRhdGEiOnsiSWQiOiIyYmViYTBiZi00NWM1LTQyNDAtOTQ1ZS0wZGEwNzA0M2Y5OTkiLCJVc2VyTmFtZSI6IjE4NjI3NTk4OTkxIiwiRW1haWwiOm51bGwsIk5hbWUiOiLlkajllK_mnbAiLCJQaG9uZU51bWJlciI6IjE4NjI3NTk4OTkxIiwiQ3JlYXRlVGltZSI6IjIwMjAtMDctMDdUMDc6MDQ6NDAuMzI0KzAwOjAwIiwiQ3JlYXRvciI6IuadqOWogSIsIklzRW5hYmxlIjp0cnVlLCJFbnRlcnByaXNlSWQiOiI1ZGVkOTBiYS00NDZjLTRjM2YtOTU0My05ZGQyNzNlYTRiYjIiLCJEZXBhcnRtZW50SWQiOiI4Y2YxZWIxNC01ZDg1LTQyNWYtYjgwMi1lZjliMDllYzc0NjIiLCJEZXBhcnRtZW50TmFtZSI6IueglOWPkemDqCIsIlJvbGVzIjpbIjZkOWJlZGI2LTIwMjgtNDYzZS05Yzc1LTI5YTYyOTE4ODU3OSIsImY1MTYyYjMyLWIwODMtNDJjYi1hNTU5LTJjMjk3MmI2YjM3YSJdLCJSb2xlc05hbWUiOlsiY2VzICIsIueuoeeQhuWRmCJdLCJQZXJtaXNzaW9ucyI6W10sIkRhdGFQZXJtaXNzaW9ucyI6W10sIk1lbnVzIjpbXSwiQWNjb3VudFR5cGUiOjIsImVmZmVjdGl2ZWRhdGUiOlsiMjAyMC0wOC0xN1QxNDo0ODowOS45MzYrMDA6MDAiLCIyMTIwLTA4LTE3VDE0OjQ4OjA5LjkzNiswMDowMCJdfX0.oy3_UN03kjhF2yeyzykFjWCqsMUtCyTIeNKal9vIuS8', 'type': 'Bearer', 'appId': '015b4da9-d8c8-4370-b245-bb9fd7dfcb70'}


def setVariable(step_info):
    # 替换取值代码中的变量
    code_variable_list = re.findall('\\${\w+}', step_info['取值代码'])
    if code_variable_list:
        for code_variable in code_variable_list:
            step_info['取值代码'] = step_info['取值代码'].replace(code_variable, temp_variables.get(code_variable[2:-1]))
            print(stpe_info)


stpe_info = ReadExcelUtils("CASE").get_data()
setVariable(stpe_info[2])



# url = 'https://api.weixin.qq.com/cgi-bin/token'
# headers = {"ContentType":"application/json;charset=utf-8"}
# param1 = '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}'
# param2 = '{"access_token":${token}}'
# data1 = '{"tag" : {"name" : "衡东8888"}}'
# session = requests.session()
# res = session.get(url=url, params=param1)
# print('响应为:%s' % res.text)
# #
# # # 正则取值
# pattern = re.compile('{"errcode":(.+?),"errmsg')
# str1 = pattern.findall(res.text)[0]
# print('str1的type是%s , str1 = %s' % (type(str1), str1))
# temp_variables['token'] = str1
# print('temp_variables = %s' % temp_variables)
# param_variable_list = re.findall('\\${\w+}', param2)
# # key = re.findall('{"access_token":\${(.+?)}}', param2)[-1]
# # print(key)
# print('param_variable_list = %s' % param_variable_list)
# if param_variable_list:
#     for param_variable in param_variable_list:
#         # print('param_variable = %s' % param_variable)
#         param2 = param2.replace(param_variable, temp_variables.get(param_variable[2:-1]))
# print('param2 = %s' % param2)

# jsonpath取值
# str1 = jsonpath.jsonpath(res.json(), '$..errcode')[0]
# # print(type(str1))
# temp_variables['token'] = str1
# # print(temp_variables)
# param_variable_list = re.findall('\\${\w+}', param2)
# # print(param_variable_list)
# if param_variable_list:
#     for param_variable in param_variable_list:
#         # print(param_variable)
#         param2 = param2.replace(param_variable, str(temp_variables.get(param_variable[2:-1])))
# print(param2)

# 确认spli方法的用法
# str1 = '$..assess_token'
# str1 = 'token,auth'
# str2 = '$..access_token,$..auth'
# str1 = """appid":"(.+?)","subapp;"subappid":"(.+?)","nex"""
# str2 = 'appid;subappid'
#
# list1 = str1.split(';')
# print(list1)
# list2 = str2.split(';')
# print(list2[0])
#
# # 存在多个值的时候替换
# dic1 = {}
# for i in range(0, len(list1)):
#     dic1[list2[i]] = list1[i]
# print(dic1)

# data = "awefaw/efwea/${appid}/fawefawef/${name}awefawef"
# url__variable_list = re.findall('\\${\w+}', data)
# print(url__variable_list)
