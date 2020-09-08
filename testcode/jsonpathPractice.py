import ast
import json
from common.excelUtils import ReadExcelUtils
import jsonpath

# json_data = {
# #     "code": 0,
# #     "message": "0",
# #     "ttl": 1,
# #     "data": {
# #         "isLogin": True,
# #         "email_verified": 0,
# #         "face": "http://i1.hdslb.com/bfs/face/17061e541785832b44426c51429ddfee39.jpg",
# #         "level_info": {
# #             "current_level": 0,
# #             "current_min": 0,
# #             "current_exp": 0,
# #             "next_exp": 1
# #         },
# #         "mid": 377206,
# #         "mobile_verified": 1,
# #         "money": 0,
# #         "moral": 70,
# #         "official": {
# #             "role": 0,
# #             "title": "",
# #             "desc": "",
# #             "type": -1
# #         },
# #         "officialVerify": {
# #             "type": -1,
# #             "desc": ""
# #         },
# #         "pendant": {
# #             "pid": 0,
# #             "name": "",
# #             "image": "",
# #             "expire": 0
# #         },
# #         "scores": 0,
# #         "uname": "洒脱喽",
# #         "vipDueDate": 0,
# #         "vipStatus": 0,
# #         "vipType": 0,
# #         "vip_pay_type": 0,
# #         "vip_theme_type": 0,
# #         "wallet": {
# #             "mid": 377206,
# #             "bcoin_balance": 0,
# #             "coupon_balance": 0,
# #             "coupon_due_time": 0
# #         },
# #         "has_shop": False,
# #         "shop_url": "",
# #         "allowance_count": 0,
# #         "answer_status": 1
# #     },
# #   "uname": "潇洒哥"
# # }

# datas = json_data["data"]
# for data in datas.items():
#     print(data)

# datas = jsonpath.jsonpath(json_data, "$.data")
# for data in datas[0].items():
#     print(data)
json_data = {
  "appList": [
    {
      "appId": "19081a7b-b6d0-4c82-a213-a893538879cb",
      "name": "testfotestcopy",
      "label": "测试测试复制",
      "createTime": "2020-07-13T01:45:51.272+00:00",
      "lastModifiTime": "2020-08-20T18:30:56.954+00:00",
      "templateCode": "00168",
      "mannagerPhone": "15821372781",
      "isEmptyApp": True,
      "creater": "周唯杰",
      "personLiableNames": None,
      "personLiableIds": None,
      "isDeleted": False,
      "subAppPersonLiableInfoDto": [

      ],
      "subAppPersonLiableNames": None
    },
    {
      "appId": "015b4da9-d8c8-4370-b245-bb9fd7dfcb70",
      "name": "testapplication",
      "label": "测试测试",
      "createTime": "2020-07-08T07:21:41.5+00:00",
      "lastModifiTime": "2020-08-20T18:30:56.796+00:00",
      "templateCode": "00168",
      "mannagerPhone": None,
      "isEmptyApp": True,
      "creater": "周唯杰",
      "personLiableNames": "",
      "personLiableIds": "",
      "isDeleted": False,
      "subAppPersonLiableInfoDto": [

      ],
      "subAppPersonLiableNames": ""
    }
  ],
  "totalCount": 2,
  "isSuccess": True
}
data = jsonpath.jsonpath(json_data, '$..appId')
print(data[-1])

# json_data = {
#   "data": {
#     "type": "Bearer",
#     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ4MDM0ODIsImRhdGEiOnsiVXNlcklkIjoiNzAzNGRkNjctY2JmOS00NTY0LThiMjAtMzNmMDk3MzlkM2M4IiwiVXNlck5hbWUiOiIxNTgyMTM3Mjc4MSIsIk1vYmlsZSI6IjE1ODIxMzcyNzgxIiwiVGltZVN0YW1wIjoiMzIzMjIzNTUzMiIsIkRldmljZU5vIjpudWxsLCJBcHBJZCI6IiIsIkFjY2Vzc1Rva2VuIjpudWxsLCJQZXJtaXNzaW9ucyI6W119fQ.KAlArtjT3KzPP-V1B02e-93mpqUPWIIla_QKu1fWQHw",
#     "expires_in": 1594803482,
#     "refresh_expires_in": 1594805282,
#     "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTQ4MDUyODIsImRhdGEiOnsiYWNjZXNzX3Rva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMU9UUTRNRE0wT0RJc0ltUmhkR0VpT25zaVZYTmxja2xrSWpvaU56QXpOR1JrTmpjdFkySm1PUzAwTlRZMExUaGlNakF0TXpObU1EazNNemxrTTJNNElpd2lWWE5sY2s1aGJXVWlPaUl4TlRneU1UTTNNamM0TVNJc0lrMXZZbWxzWlNJNklqRTFPREl4TXpjeU56Z3hJaXdpVkdsdFpWTjBZVzF3SWpvaU16SXpNakl6TlRVek1pSXNJa1JsZG1salpVNXZJanB1ZFd4c0xDSkJjSEJKWkNJNklpSXNJa0ZqWTJWemMxUnZhMlZ1SWpwdWRXeHNMQ0pRWlhKdGFYTnphVzl1Y3lJNlcxMTlmUS5LQWxBcnRqVDNLelBQLVYxQjAyZS05M21wcVVQV0lJbGFfUUt1MWZXUUh3In19.oPsYcEnFIusTIboMYusKespmp7rfvJLbVZSjf8yFQ90"
#   },
#   "requestId": "6bee1907-91d1-4898-a17b-e32a03b71892"
# }
#
# datas = jsonpath.jsonpath(json_data, "$.."+'type')
# print(datas)
#
# print(type(json_data))


# data12 = 'https://admin.a.onein.cn/workflow'
#
#
# def is_json(data11):
#     try:
#         json.loads(data11)
#     except ValueError as e:
#         return False
#     return True
#
#
# print(is_json(data12))
# data1 = ReadExcelUtils('Operation').get_data()[1]
# print(ast.literal_eval(data1['期望结果']).items())

