import ast
import json
import re

import jsonpath
import requests
from common.configUtils import ReadConfig
from common.excelUtils import ReadExcelUtils
from common.requestUtils import RequestUtils

# module_name = input('请输入要执行测试的模块:\n')
# evn_name = input('请输入测试环境：\n')
stpe_info = ReadExcelUtils("Operation").get_data()
# print(stpe_info)
# print(type(stpe_info[0]['请求参数(post)']), stpe_info[0]['请求参数(post)'])

re_login = RequestUtils(sec='Operation', option='Test')
res_login = re_login.sendRequest(stpe_info[3])
app_id = re_login.sendRequest(stpe_info[4])
code = re_login.sendRequest(stpe_info[5])
print(re_login.temporary_variables)

# url__variable_list = re.findall('\\${\w+}', stpe_info[0]['请求地址'])
# print(url__variable_list)

# token = re_login.get_key_value(res=res_login, key=stpe_info[0]['传值变量'])
# authorization = 'Bearer ' + token[0]
# appid = ReadConfig().getValue(sec="App", option="AppId")
# appname = ReadConfig().getValue(sec="App", option="AppName")

# data = ReadExcelUtils("Admin").get_data()
# print(data[1]['请求参数'])
# url = ReadConfig().getValue("Admin", "TEST") + data[1]['请求地址']
# print(url)
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br",
#     "Content-Type": "application/json; charset=utf-8",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/83.0.4103.116 Safari/537.36 ",
#     "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ4MjY1NjMsImRhdGEiOnsiVXNlcklkIjoiZDljYTJmZGYtMGM3OS00ZmY4LThkNzQtYmQ2NDlhMTcxMjVjIiwiVXNlck5hbWUiOiIxODYyNzU5ODk5MSIsIk1vYmlsZSI6IjE4NjI3NTk4OTkxIiwiVGltZVN0YW1wIjoiMjg4NjcyOTcyOSIsIkRldmljZU5vIjpudWxsLCJBcHBJZCI6IjAxNWI0ZGE5LWQ4YzgtNDM3MC1iMjQ1LWJiOWZkN2RmY2I3MCIsIkFjY2Vzc1Rva2VuIjpudWxsLCJQZXJtaXNzaW9ucyI6W3siQXBwSWQiOiIwMTViNGRhOS1kOGM4LTQzNzAtYjI0NS1iYjlmZDdkZmNiNzAiLCJJZGVudGl0eSI6IkFkbWluIiwiUGVybWlzc2lvblZhbHVlIjpbIm9uZWluLmFwcHMuMDE1YjRkYTktZDhjOC00MzcwLWIyNDUtYmI5ZmQ3ZGZjYjcwLioiXX1dfX0.VZ06kK1pt01Ht8kPaMuqw0NSKr5N6KpIgH9rujsRvXk",
#     "appid": "015b4da9-d8c8-4370-b245-bb9fd7dfcb70",
#     "appname": "testapplication"
# }
#
# res = requests.post(url=url, headers=headers, data=data[1]['请求参数'].encode("utf-8"))
# print(res.text)

# data = ReadExcelUtils("Admin").get_data()
# print(data[0]['请求参数'])
# url = ReadConfig().getValue("Admin", "TEST") + data[0]['请求地址']
# print(url)
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br",
#     "Content-Type": "application/json; charset=utf-8",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/83.0.4103.116 Safari/537.36 "
# }
# json_data = data[0]['请求参数']
# json_data = json_data.encode("utf-8")
# res = requests.post(url=url, headers=headers, data=json_data)
# print(json.loads(res.text))

# head = {
#             "Accept": "application/json, text/plain, */*",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Content-Type": "application/json",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                           "Chrome/84.0.4147.135 Safari/537.36 ",
#             "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTg4NzYyMjEsImRhdGEiOnsiSWQiOiIyYmViYTBiZi00NWM1LTQyNDAtOTQ1ZS0wZGEwNzA0M2Y5OTkiLCJVc2VyTmFtZSI6IjE4NjI3NTk4OTkxIiwiRW1haWwiOm51bGwsIk5hbWUiOiLlkajllK_mnbAiLCJQaG9uZU51bWJlciI6IjE4NjI3NTk4OTkxIiwiQ3JlYXRlVGltZSI6IjIwMjAtMDctMDdUMDc6MDQ6NDAuMzI0KzAwOjAwIiwiQ3JlYXRvciI6IuadqOWogSIsIklzRW5hYmxlIjp0cnVlLCJFbnRlcnByaXNlSWQiOiI1ZGVkOTBiYS00NDZjLTRjM2YtOTU0My05ZGQyNzNlYTRiYjIiLCJEZXBhcnRtZW50SWQiOiI4Y2YxZWIxNC01ZDg1LTQyNWYtYjgwMi1lZjliMDllYzc0NjIiLCJEZXBhcnRtZW50TmFtZSI6IueglOWPkemDqCIsIlJvbGVzIjpbIjZkOWJlZGI2LTIwMjgtNDYzZS05Yzc1LTI5YTYyOTE4ODU3OSIsImY1MTYyYjMyLWIwODMtNDJjYi1hNTU5LTJjMjk3MmI2YjM3YSJdLCJSb2xlc05hbWUiOlsiY2VzICIsIueuoeeQhuWRmCJdLCJQZXJtaXNzaW9ucyI6W10sIkRhdGFQZXJtaXNzaW9ucyI6W10sIk1lbnVzIjpbXSwiQWNjb3VudFR5cGUiOjIsImVmZmVjdGl2ZWRhdGUiOlsiMjAyMC0wOC0xN1QxNDo0ODowOS45MzYrMDA6MDAiLCIyMTIwLTA4LTE3VDE0OjQ4OjA5LjkzNiswMDowMCJdfX0.R5fxjXNBc3O1QLImZdYKE7wE__JjiSch_33LyfKQWXI"
#         }
# url = 'http://operation-api.a.onein.cn/operation/directlogin/015b4da9-d8c8-4370-b245-bb9fd7dfcb70?'
# res = requests.get(url=url,headers=head,params=json.dumps(stpe_info[2]['请求参数(get)']))
# print(res.text)

# list1 = ['1']
# for i in range(0,len(list1)):
#     value = list1[i]
#     print(value)

# get_value_code_list = stpe_info[2]["取值代码"].split(";")
# transfer_value_variable_list = stpe_info[2]["传值变量"].split(";")
# print(get_value_code_list, transfer_value_variable_list, len(get_value_code_list))
# value = re.findall(get_value_code_list[0], res.text)
# re_login.temporary_variables[transfer_value_variable_list[0]] = value

# for i in range(0, len(get_value_code_list)):
#     value = re.findall(get_value_code_list[i], res.text)[-1]
#     re_login.temporary_variables[transfer_value_variable_list[i]] = value
# print(re_login.temporary_variables)


