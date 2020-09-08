from uuid import UUID
import pymongo as pm

host = '49.234.102.130'
port = 27001
user_name = 'root'
user_pwd = 'oneinroot'
dbname = 'admin'

# 连接数据库
mongo_client = pm.MongoClient('mongodb://{}:{}@{}:{}/?authSource={}'.format(user_name, user_pwd, host, port, dbname))
db = mongo_client.SmtSoft
collection = db['Smt_Apps']

# 迭代游标（cursor）并且打印文档内容
# datas = collection.find()
# for document in datas:
#     print(document)

# data = collection.find({'_id': UUID('ddde1c70-7d51-cd49-a14b-2e07562cfda4')})
# for document in data:
#     print(document)
# 删除查询出的对象
result = collection.delete_many({'_id': UUID('ddde1c70-7d51-cd49-a14b-2e07562cfda4')})
print(result.deleted_count)
