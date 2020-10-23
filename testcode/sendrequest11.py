import ast
import requests
from common.dataUtils import DataUtils

step_infos = DataUtils("CASE").testCaseDataList()[0].get('case_info')
header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                     '.eyJleHAiOjE2MDIyMzc4NzUsImRhdGEiOnsiSWQiOiIyYmViYTBiZi00NWM1LTQyNDAtOTQ1ZS0wZGEwNzA0M2Y5OTkiLCJVc2VyTmFtZSI6IjE4NjI3NTk4OTkxIiwiRW1haWwiOm51bGwsIk5hbWUiOiLlkajllK_mnbAiLCJQaG9uZU51bWJlciI6IjE4NjI3NTk4OTkxIiwiQ3JlYXRlVGltZSI6IjIwMjAtMDctMDdUMDc6MDQ6NDAuMzI0KzAwOjAwIiwiQ3JlYXRvciI6IuadqOWogSIsIklzRW5hYmxlIjp0cnVlLCJFbnRlcnByaXNlSWQiOiI1ZGVkOTBiYS00NDZjLTRjM2YtOTU0My05ZGQyNzNlYTRiYjIiLCJEZXBhcnRtZW50SWQiOiI4Y2YxZWIxNC01ZDg1LTQyNWYtYjgwMi1lZjliMDllYzc0NjIiLCJEZXBhcnRtZW50TmFtZSI6IueglOWPkemDqCIsIlJvbGVzIjpbIjZkOWJlZGI2LTIwMjgtNDYzZS05Yzc1LTI5YTYyOTE4ODU3OSIsImY1MTYyYjMyLWIwODMtNDJjYi1hNTU5LTJjMjk3MmI2YjM3YSJdLCJSb2xlc05hbWUiOlsiY2VzICIsIueuoeeQhuWRmCJdLCJQZXJtaXNzaW9ucyI6W10sIkRhdGFQZXJtaXNzaW9ucyI6W10sIk1lbnVzIjpbXSwiQWNjb3VudFR5cGUiOjIsImVmZmVjdGl2ZWRhdGUiOlsiMjAyMC0wOC0xN1QxNDo0ODowOS45MzYrMDA6MDAiLCIyMTIwLTA4LTE3VDE0OjQ4OjA5LjkzNiswMDowMCJdfX0.aIdiB2k3N7ihEcsdvbxv8ic-nwFvXbml8dtope_IoMs '

}
url = 'https://operation-api.a.onein.cn/operation/setapppersonliable?'
data = step_infos[7].get('请求参数(post)')
body = ast.literal_eval(data)
print(body)
# res = requests.post(url=url, headers=header, json=body)

# print(res.text)
