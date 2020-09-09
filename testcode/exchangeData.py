# list1 = [{'a': 123}, {'a': 456},{'b': 789}]
# dic = {}
# for _ in list1:
#     for k, v in _.items():
#         dic.setdefault(k, []).append(v)
# print(dic)

from common.dataUtils import DataUtils

# case_info = DataUtils('CASE').testCaseDataList()[0]
# step_info = case_info.get('case_info')[0]
# info = step_info.get("请求参数(get)")
# if info == '':
#     print(True)
# else:
#     print(False)

case_infos = DataUtils('CASE').testCaseDataList()
print(case_infos)