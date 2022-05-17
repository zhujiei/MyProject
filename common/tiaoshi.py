from common.handle_mysql import db
from common.handle_config import conf

today0_sql = conf.get('crowd_condition', 'today0_sql')
today_0_time_stamp = db.select_one(today0_sql)[0]
print(today_0_time_stamp)
# 查询第二天0点时间戳sql
second_day0_sql = conf.get('crowd_condition', 'second_day0_sql')
second_day_0_time_stamp = db.select_one(second_day0_sql)[0]
print(second_day_0_time_stamp)
# 第一步：查询当天注册的用户guid
sql1 = "SELECT guid FROM test_qichacha.cc_user WHERE regist_time>'{}' and regist_time<'{}' and groupid=11".format(
    today_0_time_stamp, second_day_0_time_stamp)
# sql2 = "SELECT guid FROM test_qichacha.cc_user ORDER BY uid DESC limit 100;"
register_guid = db.select_all(sql1)
print(register_guid)
# guid = []
# for item in register_guid:
#     sql1 = 'SELECT "%s" FROM test_qichacha.cc_user WHERE groupid=11' % item
#     guid01 = db.select_one(sql1)
#     print(guid)
#     guid.append(guid01)
# print(guid)
# a, b, *c =register_guid
# print(c)
# print(c[0])
# for i in range(100):
#     sql1 = "SELECT * from test_qichacha.cc_order WHERE buyer_id ='%s';" % today_register_guid[i]
#     no_order_guid = db.select_one(sql1)
#     # print(no_order_guid)
#     if no_order_guid:
#         print(no_order_guid)
#         break

# payload = {"userId": today_register_guid,
#            "userPortraitId": "532c709f242f4cc6bdfda324a037caa3"
#            }
# a = HttpRequest().http_request(data=payload)
# print(a)