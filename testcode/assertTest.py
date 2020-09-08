from common.requestUtils import RequestUtils
from common.excelUtils import ReadExcelUtils
from common.configUtils import ReadConfig

step_info = ReadExcelUtils('Admin').get_data()
re_login = RequestUtils('Admin', 'TEST',step_info[0])
res_login = re_login.sendRequest()
token = re_login.get_key_value(res_login, step_info[0]['传值变量'])
# print(token)

re = RequestUtils('Admin', 'TEST',step_info[1])
re.headers['authorization'] = 'Bearer ' + token[0]
re.headers['appid'] = ReadConfig().getValue('App', 'AppId')
re.headers['appname'] = ReadConfig().getValue('App', 'AppName')
res = re.sendRequest()
# excpet_result = re.get_key_value(res=res, key=step_info[1]['执行结果取参'])
print(re.get_key_value(res, step_info[1]['执行结果取参'])[0])
print(step_info[1]['期望结果'])

