# list = [{'a': 123}, {'a': 456},{'b': 789}]
# dic = {}
# s = []
# for _ in list:
#     for k, v in _.items():
#         dic.setdefault(k, []).append(v)
# print(dic)
# print(s)


# testdata = [{'测试用例编号':'case01',"caseinfo":{'step1':"123"}},
#          {'测试用例编号':'case02',"caseinfo":{'step1':"123"}},
#          {'测试用例编号':'case02',"caseinfo":{'step2':"456"}}]
#
# data_dict = {}
# for data in testdata:
#     data_dict.setdefault(data['测试用例编号'],[]).append(data)
#
# print(data_dict)


case_infos = [{'编号': 1.0, '用例名称': '创建实例目录', '步骤': 'SETP01', '请求方式': 'POST', '补充请求头': 1, '请求地址': '/apps/v1/schemacategorys/', '请求参数': '{"categoryName":"自动化分类1","parentId":"00000000-0000-0000-0000-000000000000"}', '传值变量': '', '期望结果': '未分配权限', '执行结果取参': 'message'}, {'编号': 1.0, '用例名称': '创建实例目录', '步骤': 'SETP02', '请求方式': 'GET', '补充请求头': 1, '请求地址': '/apps/v1/schemacategorys/', '请求参数': '', '传值变量': '', '期望结果': '未分配权限', '执行结果取参': 'message'}, {'编号': 1.0, '用例名称': '创建实例目录', '步骤': 'SETP03', '请求方式': 'GET', '补充请求头': 1, '请求地址': '/apps/v1/schemacategorys/schemacount', '请求参数': '', '传值变量': '', '期望结果': '015b4da9-d8c8-4370-b245-bb9fd7dfcb70', '执行结果取参': 'appId'}]
for case_info in case_infos:
    print(type(case_info), case_info)
