import json

import jsonpath

from common.configUtils import ReadConfig
from common.requestUtils import RequestUtils
from common.excelUtils import ReadExcelUtils
import requests
import os
from requests.adapters import HTTPAdapter


# host = 'http://httpbin.org'
# s = requests.Session()
# s.mount(host, HTTPAdapter(max_retries=5))
#
#
# r = requests.get(url=host+'/get')
# r = requests.post(url=host+'/post', data={"key1": "value1"})
# r = requests.delete(url=host+'/delete')
# r = requests.head(url=host + '/get')
# r = requests.options(url=host+'/get')
# print(r.status_code)
# r.close()
# response1 = requests.get("https://api.github.com/events")
# print(response1.text)
# print(response1.encoding)


# auth = ReadTXT().readAuth()
# url = ReadConfig().getHost("Admin", "TEST") + ReadExcelUtils('Sheet1').get_data()[0]['请求地址']
#
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br",
#     "Content-Type": "application/json; charset=utf-8",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/83.0.4103.116 Safari/537.36 ",
#     "authorization": auth,
#     "appid": "015b4da9-d8c8-4370-b245-bb9fd7dfcb70",
#     "appname": "testapplication"
# }
# body = str(ReadExcelUtils('Sheet1').get_data()[0]['请求参数'])
# print(body)
# # #
# r = requests.post(url=url, data=body, headers=headers)
# print(r.status_code)
# print(json.dumps(r.text))

parameters = {
    'page': 1,
    'count': 7
}
re = requests.get(url='https://www.jianshu.com/shakespeare/notes/39155760/included_collections', params=parameters, headers=head)
print(re.status_code)
print(re.text)

# import xlrd
# from config import settings
# path = settings.testcasedata_path + '\\testCase.xlsx'
# wb = xlrd.open_workbook(path)
# ws = wb.sheet_by_name('Sheet1')
#
#
# def get_rows():
#     max_rows = ws.nrows
#     return max_rows
#
#
# def get_cols():
#     max_cols = ws.ncols
#     return max_cols
#
#
# print(get_rows(), get_cols())

# data = ReadExcelUtils('Sheet1').get_data()
# print(data)
# re = RequestUtils().sendRequest('Admin', 'TEST', data)
# print(re.status_code)
# print(re.text)
# headers = {
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br",
#     "Content-Type": "application/json; charset=utf-8",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/83.0.4103.116 Safari/537.36 "
# }
# headers['authorization'] = 'auth'
# headers['appid'] = 'test'
# headers['appname'] = 'tesapplication'
# print(headers)
# data = ReadExcelUtils("Sheet1").get_data()[0]
# re = RequestUtils(sec="Admin", option="TEST", step_info=data)
# res = re.sendRequest()
# v_type = re.get_key_value(res, data['传值变量1'])
# token = re.get_key_value(res, data['传值变量2'])
# print(v_type[0] + ' ' + token[0])
# auth = v_type + ' ' + token
# print(auth)




