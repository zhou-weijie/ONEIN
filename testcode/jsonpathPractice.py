import ast
import json
from common.excelUtils import ReadExcelUtils
import jsonpath

# json_data = {
#     "code": 0,
#     "message": "0",
#     "ttl": 1,
#     "data": {
#         "isLogin": True,
#         "email_verified": 0,
#         "face": "http://i1.hdslb.com/bfs/face/17061e541785832b44426c51429ddfee39.jpg",
#         "level_info": {
#             "current_level": 0,
#             "current_min": 0,
#             "current_exp": 0,
#             "next_exp": 1
#         },
#         "mid": 377206,
#         "mobile_verified": 1,
#         "money": 0,
#         "moral": 70,
#         "official": {
#             "role": 0,
#             "title": "",
#             "desc": "",
#             "type": -1
#         },
#         "officialVerify": {
#             "type": -1,
#             "desc": ""
#         },
#         "pendant": {
#             "pid": 0,
#             "name": "",
#             "image": "",
#             "expire": 0
#         },
#         "scores": 0,
#         "uname": "洒脱喽",
#         "vipDueDate": 0,
#         "vipStatus": 0,
#         "vipType": 0,
#         "vip_pay_type": 0,
#         "vip_theme_type": 0,
#         "wallet": {
#             "mid": 377206,
#             "bcoin_balance": 0,
#             "coupon_balance": 0,
#             "coupon_due_time": 0
#         },
#         "has_shop": False,
#         "shop_url": "",
#         "allowance_count": 0,
#         "answer_status": 1
#     },
#   "uname": "潇洒哥"
# }
# datas = json_data["data"]
# for data in datas.items():
#     print(data)
# datas = jsonpath.jsonpath(json_data, "$.data")
# for data in datas[0].items():
#     print(data)


# json_data = {
#   "appList": [
#     {
#       "appId": "19081a7b-b6d0-4c82-a213-a893538879cb",
#       "name": "testfotestcopy",
#       "label": "测试测试复制",
#       "createTime": "2020-07-13T01:45:51.272+00:00",
#       "lastModifiTime": "2020-08-20T18:30:56.954+00:00",
#       "templateCode": "00168",
#       "mannagerPhone": "15821372781",
#       "isEmptyApp": True,
#       "creater": "周唯杰",
#       "personLiableNames": None,
#       "personLiableIds": None,
#       "isDeleted": False,
#       "subAppPersonLiableInfoDto": [
#
#       ],
#       "subAppPersonLiableNames": None
#     },
#     {
#       "appId": "015b4da9-d8c8-4370-b245-bb9fd7dfcb70",
#       "name": "testapplication",
#       "label": "测试测试",
#       "createTime": "2020-07-08T07:21:41.5+00:00",
#       "lastModifiTime": "2020-08-20T18:30:56.796+00:00",
#       "templateCode": "00168",
#       "mannagerPhone": None,
#       "isEmptyApp": True,
#       "creater": "周唯杰",
#       "personLiableNames": "",
#       "personLiableIds": "",
#       "isDeleted": False,
#       "subAppPersonLiableInfoDto": [
#
#       ],
#       "subAppPersonLiableNames": ""
#     }
#   ],
#   "totalCount": 2,
#   "isSuccess": True
# }
# data = jsonpath.jsonpath(json_data, '$..appId')
# print(data[-1])


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
# datas = jsonpath.jsonpath(json_data, "$.."+'type')
# print(datas)
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

# json_data = {
#   "firstIndustryList": [
#     {
#       "id": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "酒店/餐饮/美食"
#     },
#     {
#       "id": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "家政/家居/服务"
#     },
#     {
#       "id": "9fe0fb51-1202-4f24-8077-29b0370b9d99",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "政府/党建/宗教"
#     },
#     {
#       "id": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "商业/物流/超市"
#     },
#     {
#       "id": "379f17bb-4610-464c-a26c-402b36552033",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "教育/医疗/母婴"
#     },
#     {
#       "id": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "数码/金融/IT"
#     },
#     {
#       "id": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "parentId": "00000000-0000-0000-0000-000000000000",
#       "level": 1,
#       "name": "其它"
#     }
#   ],
#   "secondIndustryList": [
#     {
#       "id": "ccadfcaf-3d54-41b7-9754-39115b308251",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "餐饮外卖"
#     },
#     {
#       "id": "ccadfcaf-3d54-41b7-9754-39115b308252",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "宾馆酒店"
#     },
#     {
#       "id": "ccadfcaf-3d54-41b7-9754-39115b308253",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "酒水饮料"
#     },
#     {
#       "id": "55bbcf78-f2bd-47ed-a28a-9370c7210ecc",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "食品"
#     },
#     {
#       "id": "353b2506-f9dc-4a5b-9a54-b69f3b99a520",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "生鲜水果"
#     },
#     {
#       "id": "70cb516e-a867-4ab9-a31b-9bf890cfe67e",
#       "parentId": "e79642b3-5f59-4639-9e66-0711b7c24cf7",
#       "level": 2,
#       "name": "小吃美食"
#     },
#     {
#       "id": "99aea2d2-7841-4e9e-9bd3-f9faace759fa",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "丽人美容"
#     },
#     {
#       "id": "7a6d543a-a6f7-4477-b2cc-89828d011967",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "运动健身"
#     },
#     {
#       "id": "62528bdb-69bd-4b47-9d86-498b84c59209",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "婚庆摄影"
#     },
#     {
#       "id": "c1b2ef8e-3efe-4dfc-bafe-dedada2e08ef",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "家居家装"
#     },
#     {
#       "id": "610b0bce-0d15-4dff-b3ea-650205c1a1cc",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "家政服务"
#     },
#     {
#       "id": "b52d55f6-c30f-4850-a186-43fb8a0903bc",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "旅游服务"
#     },
#     {
#       "id": "9129fbc6-110c-4a32-9ff6-7cd7f2bc8d00",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "养老服务"
#     },
#     {
#       "id": "5752e523-9259-434f-a44b-34dfc30cf955",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "咨询服务"
#     },
#     {
#       "id": "e243529e-7dfc-443e-b60d-e50f13bd507e",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "风水算命"
#     },
#     {
#       "id": "9a7a4d9f-fd02-4603-b8f8-8d305b2a1ea9",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "房产中介"
#     },
#     {
#       "id": "2b57f93d-b251-41c3-84e1-28ea431dbe99",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "汽车服务"
#     },
#     {
#       "id": "989bd105-704b-4bf9-bade-12a85380011b",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "生活服务"
#     },
#     {
#       "id": "39ebd035-9966-4dc1-bfee-369e5f7f171e",
#       "parentId": "5e9c0f33-f346-4bb3-bc33-7be5131ef719",
#       "level": 2,
#       "name": "健康养生"
#     },
#     {
#       "id": "5cebcf5a-2b45-4af1-bc75-fa15a22d1d34",
#       "parentId": "9fe0fb51-1202-4f24-8077-29b0370b9d99",
#       "level": 2,
#       "name": "政府机关"
#     },
#     {
#       "id": "0cd24272-324e-4469-a04e-74813a0d57de",
#       "parentId": "9fe0fb51-1202-4f24-8077-29b0370b9d99",
#       "level": 2,
#       "name": "政务党建"
#     },
#     {
#       "id": "42fa06d4-cb02-4c84-830c-7f053045f5fe",
#       "parentId": "9fe0fb51-1202-4f24-8077-29b0370b9d99",
#       "level": 2,
#       "name": "宗教文化"
#     },
#     {
#       "id": "84db0b30-7c07-49c6-bf51-4cbb856edab0",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "珠宝饰品"
#     },
#     {
#       "id": "3d4be83f-2346-41e3-92b1-89d33a538dc5",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "超市便利店"
#     },
#     {
#       "id": "37b6f37f-afdc-441d-8f63-e8c9f13b46e5",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "特色农业"
#     },
#     {
#       "id": "23eb4498-0849-4e2d-a13c-e5dbe99ecdab",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "鲜花盆栽"
#     },
#     {
#       "id": "c1a9e79d-325e-49e7-aa32-ec546ba8cbcb",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "物流配送"
#     },
#     {
#       "id": "d8815db6-bfdb-4058-ad5e-fc94a6cda34b",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "服饰箱包"
#     },
#     {
#       "id": "86fff41b-f50e-46ca-9273-8b3ea9f8c457",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "进口商品"
#     },
#     {
#       "id": "08335106-3437-42c7-ba50-745cc8f84f6b",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "景点门票"
#     },
#     {
#       "id": "e1b95f48-30e3-4697-960e-53792d17b368",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "生活百货"
#     },
#     {
#       "id": "f6e9b01e-0974-4ed4-9352-f44923ef3f94",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "宠物用品"
#     },
#     {
#       "id": "75a9315b-2003-42e4-981e-1afb98cde149",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "社区物业"
#     },
#     {
#       "id": "7b58e085-00c8-4400-95f6-d11040a02eeb",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "办公用品"
#     },
#     {
#       "id": "7970ed91-fd77-4b90-825e-3a8b262326ba",
#       "parentId": "2edc3da5-34e1-402d-bb90-8a2eafab2288",
#       "level": 2,
#       "name": "五金"
#     },
#     {
#       "id": "467daf12-fb63-430b-bc83-0a1bbdbf94ba",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "休闲娱乐"
#     },
#     {
#       "id": "14bfe68f-f825-4b17-a903-851ff6979b2d",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "教育培训"
#     },
#     {
#       "id": "9c83d77c-4f4a-48f9-8462-f0fbbf28d360",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "母婴用品"
#     },
#     {
#       "id": "8771e2c9-3aa5-4ecf-b195-3eb16fed51fd",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "茶艺茶具"
#     },
#     {
#       "id": "9ee648c4-6b91-4160-b37e-15e2c488d9aa",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "医疗医院"
#     },
#     {
#       "id": "5a0ed902-d632-44c5-b802-fc2534b2223b",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "玩具"
#     },
#     {
#       "id": "9741294f-757f-4696-b4a1-9334029b5548",
#       "parentId": "379f17bb-4610-464c-a26c-402b36552033",
#       "level": 2,
#       "name": "医药保健"
#     },
#     {
#       "id": "f563920e-1778-4ffa-ad19-afc50b4e882f",
#       "parentId": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "level": 2,
#       "name": "电子数码"
#     },
#     {
#       "id": "2678a486-29c1-40d4-af0b-7aaf86e00416",
#       "parentId": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "level": 2,
#       "name": "金融保险"
#     },
#     {
#       "id": "ab549e65-8c98-4140-9c3f-62082bcbae91",
#       "parentId": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "level": 2,
#       "name": "银行服务"
#     },
#     {
#       "id": "536f7978-0271-442a-a75d-a85b76045aa8",
#       "parentId": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "level": 2,
#       "name": "互联网科技"
#     },
#     {
#       "id": "c76d4f8b-512f-4f60-a4a4-e49dd7ecadf8",
#       "parentId": "734e9a05-9052-4c77-aaad-7ba7676a4322",
#       "level": 2,
#       "name": "AI智能"
#     },
#     {
#       "id": "45d55412-839e-4338-982a-23caacf14c6e",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "艺术收藏"
#     },
#     {
#       "id": "c347a817-dc41-47f2-aa57-8b896d815ed1",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "工业化工"
#     },
#     {
#       "id": "a7d7c97f-fcfb-44a4-8c21-0c173ec7ebd1",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "新能源环保"
#     },
#     {
#       "id": "536e3664-a9b0-434b-97a7-9543ba393656",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "家用电器"
#     },
#     {
#       "id": "48ec52d4-a46d-48b5-aefd-f3e67c55e518",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "广告传媒"
#     },
#     {
#       "id": "c0c70774-14a7-4d58-9d72-199fa2bcc448",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "工业设备"
#     },
#     {
#       "id": "8970728a-2647-4c63-ac50-7d2ba377117b",
#       "parentId": "14be58c0-1f3a-4246-b267-84579d78424a",
#       "level": 2,
#       "name": "社交"
#     }
#   ]
# }
# data = jsonpath.jsonpath(json_data, '$.firstIndustryList[0].id')
# print(data)

# json_data = {
#     "appList": [
#         {
#             "appId": "360e80c4-e962-4a51-8d79-764ab05355aa",
#             "name": "autotest1600079712",
#             "label": "自动化测试1600079712",
#             "createTime": "2020-09-14T10:35:12.988+00:00",
#             "lastModifiTime": "2020-09-14T10:35:13.463+00:00",
#             "templateCode": "00168",
#             "mannagerPhone": "18627598991",
#             "isEmptyApp": True,
#             "creater": "周唯杰",
#             "personLiableNames": "周唯杰",
#             "personLiableIds": "2beba0bf-45c5-4240-945e-0da07043f999",
#             "isDeleted": False,
#             "subAppPersonLiableInfoDto": [
#                 {
#                     "adminRoleId": [
#                         "a92f772e-c477-4f3a-a1f5-d2987d5be358"
#                     ],
#                     "appPersonLiableType": [
#                         {
#                             "type": "1",
#                             "id": "2beba0bf-45c5-4240-945e-0da07043f999",
#                             "label": "周唯杰"
#                         }
#                     ]
#                 }
#             ],
#             "subAppPersonLiableNames": "周唯杰"
#         }
#     ],
#     "totalCount": 1,
#     "isSuccess": True
# }
json_data = {
    "isSuccess": True,
    "errorMessage": 'NULL',
    "userId": "2beba0bf-45c5-4240-945e-0da07043f999",
    "returnUrl": "",
    "token": {
        "type": "Bearer",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDAxNTQ4OTksImRhdGEiOnsiSWQiOiIyYmViYTBiZi00NWM1LTQyNDAtOTQ1ZS0wZGEwNzA0M2Y5OTkiLCJVc2VyTmFtZSI6IjE4NjI3NTk4OTkxIiwiRW1haWwiOm51bGwsIk5hbWUiOiLlkajllK_mnbAiLCJQaG9uZU51bWJlciI6IjE4NjI3NTk4OTkxIiwiQ3JlYXRlVGltZSI6IjIwMjAtMDctMDdUMDc6MDQ6NDAuMzI0KzAwOjAwIiwiQ3JlYXRvciI6IuadqOWogSIsIklzRW5hYmxlIjp0cnVlLCJFbnRlcnByaXNlSWQiOiI1ZGVkOTBiYS00NDZjLTRjM2YtOTU0My05ZGQyNzNlYTRiYjIiLCJEZXBhcnRtZW50SWQiOiI4Y2YxZWIxNC01ZDg1LTQyNWYtYjgwMi1lZjliMDllYzc0NjIiLCJEZXBhcnRtZW50TmFtZSI6IueglOWPkemDqCIsIlJvbGVzIjpbIjZkOWJlZGI2LTIwMjgtNDYzZS05Yzc1LTI5YTYyOTE4ODU3OSIsImY1MTYyYjMyLWIwODMtNDJjYi1hNTU5LTJjMjk3MmI2YjM3YSJdLCJSb2xlc05hbWUiOlsiY2VzICIsIueuoeeQhuWRmCJdLCJQZXJtaXNzaW9ucyI6W10sIkRhdGFQZXJtaXNzaW9ucyI6W10sIk1lbnVzIjpbXSwiQWNjb3VudFR5cGUiOjIsImVmZmVjdGl2ZWRhdGUiOlsiMjAyMC0wOC0xN1QxNDo0ODowOS45MzYrMDA6MDAiLCIyMTIwLTA4LTE3VDE0OjQ4OjA5LjkzNiswMDowMCJdfX0.BWwlNK4AQZk4jiosnFeuMIOJG-M-9I9EVGcny3m6q78",
        "expires_in": 1600154899,
        "refresh_expires_in": 3200309798,
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjMyMDAzMDk3OTgsImRhdGEiOnsiYWNjZXNzX3Rva2VuIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SmxlSEFpT2pFMk1EQXhOVFE0T1Rrc0ltUmhkR0VpT25zaVNXUWlPaUl5WW1WaVlUQmlaaTAwTldNMUxUUXlOREF0T1RRMVpTMHdaR0V3TnpBME0yWTVPVGtpTENKVmMyVnlUbUZ0WlNJNklqRTROakkzTlRrNE9Ua3hJaXdpUlcxaGFXd2lPbTUxYkd3c0lrNWhiV1VpT2lMbGthamxsS19tbmJBaUxDSlFhRzl1WlU1MWJXSmxjaUk2SWpFNE5qSTNOVGs0T1RreElpd2lRM0psWVhSbFZHbHRaU0k2SWpJd01qQXRNRGN0TURkVU1EYzZNRFE2TkRBdU16STBLekF3T2pBd0lpd2lRM0psWVhSdmNpSTZJdWFkcU9Xb2dTSXNJa2x6Ulc1aFlteGxJanAwY25WbExDSkZiblJsY25CeWFYTmxTV1FpT2lJMVpHVmtPVEJpWVMwME5EWmpMVFJqTTJZdE9UVTBNeTA1WkdReU56TmxZVFJpWWpJaUxDSkVaWEJoY25SdFpXNTBTV1FpT2lJNFkyWXhaV0l4TkMwMVpEZzFMVFF5TldZdFlqZ3dNaTFsWmpsaU1EbGxZemMwTmpJaUxDSkVaWEJoY25SdFpXNTBUbUZ0WlNJNkl1ZWdsT1dQa2VtRHFDSXNJbEp2YkdWeklqcGJJalprT1dKbFpHSTJMVEl3TWpndE5EWXpaUzA1WXpjMUxUSTVZVFl5T1RFNE9EVTNPU0lzSW1ZMU1UWXlZak15TFdJd09ETXROREpqWWkxaE5UVTVMVEpqTWprM01tSTJZak0zWVNKZExDSlNiMnhsYzA1aGJXVWlPbHNpWTJWeklDSXNJdWV1b2VlUWh1V1JtQ0pkTENKUVpYSnRhWE56YVc5dWN5STZXMTBzSWtSaGRHRlFaWEp0YVhOemFXOXVjeUk2VzEwc0lrMWxiblZ6SWpwYlhTd2lRV05qYjNWdWRGUjVjR1VpT2pJc0ltVm1abVZqZEdsMlpXUmhkR1VpT2xzaU1qQXlNQzB3T0MweE4xUXhORG8wT0Rvd09TNDVNellyTURBNk1EQWlMQ0l5TVRJd0xUQTRMVEUzVkRFME9qUTRPakE1TGprek5pc3dNRG93TUNKZGZYMC5CV3dsTks0QVFaazRqaW9zbkZldU1JT0pHLU0tOUk5RVZHY255M202cTc4In19.kwA90g2aM1jNzjz_1r2owlv6HDaIkMyZ26E1C23dDK8"
    },
    "dateTime": "2020-09-15T06:28:19.9372973+00:00"
}
# for data_item in json_data.items():
#     print(data_item)
key_list = []
item_list = []
# print(json_data.items())


def get_dict_allkeys(dict_a):
    """
  遍历嵌套字典，获取json返回结果的所有key值
  :param dict_a:
  :return: key_list
  """
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
        # 如果为字典类型，则提取key存放到key_list中
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            dict1 = {temp_key: temp_value}
            key_list.append(dict1)
            get_dict_allkeys(temp_value)  # 自我调用实现无限遍历
    elif isinstance(dict_a, list):
        # 如果为列表类型，则遍历列表里的元素，将字典类型的按照上面的方法提取key
        for k in dict_a:
            if isinstance(k, dict):
                for x in range(len(k)):
                    temp_key = list(k.keys())[x]
                    temp_value = k[temp_key]
                    dict1 = {temp_key: temp_value}
                    key_list.append(dict1)
                    get_dict_allkeys(temp_value)  # 自我调用实现无限遍历
    return key_list


if __name__ == '__main__':
    items = get_dict_allkeys(json_data)
    item = ReadExcelUtils("CASE").get_data()[0].get('期望结果')
    if ast.literal_eval(item) in items:
        print(True)
    else:
        print(False)
    # print(type(items[0]))
