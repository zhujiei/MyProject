from common.handle_mysql import db
from common.handle_config import conf

class Handle_Opreation:

    def is_register(self, guid):
        # 判断用户是否注册过
        sql0 = "SELECT * FROM test_qichacha.cc_user WHERE guid='%s'" % guid
        rows = db.select_one(sql=sql0)
        if len(rows) == 0:
            print("用户暂未注册")

    def guid_endnumber(self, guid, endnumber):
        '''endnumber导入config文件中的[guid_info]的section值
        通过conf.get('guid_info', 'guid_endnumberlist001')获取'''
        # 更改用户guid尾号
        sql = "SELECT phone from test_qichacha.cc_user WHERE guid='%s'" % guid
        rows_phone = (db.select_one(sql))[0]
        aa = guid.endswith(endnumber)
        if not aa:
            new_guid = guid[::-1].replace(guid[-1], endnumber[0], 1)[::-1]
            sql = "UPDATE test_qichacha.cc_user SET guid='%s' WHERE phone='%s'" % (new_guid, rows_phone)
            db.update(sql)
            # sql1 = "SELECT phone from test_qichacha.cc_user WHERE guid='%s'" % new_guid
            # rows = (db.select_one(sql1))[0]
            # print(rows)
            sql2 = "SELECT guid from test_qichacha.cc_user WHERE phone='%s'" % rows_phone
            rows = (db.select_one(sql2))[0]
            assert rows[-1] == endnumber[0], "更改guid尾号失败"
            guid = new_guid
        return guid


    def delete_order(self, guid):
        # 查询此用户是否存在订单
        sql = "SELECT * from test_qichacha.cc_order WHERE buyer_id='%s'" % guid
        rows = db.select_all(sql)
        list_rows = list(rows)
        if len(list_rows) > 0:
            # 删除用户下所有订单
            sql1 = "DELETE FROM test_qichacha.cc_order WHERE buyer_id='%s'" % guid
            db.delete(sql=sql1)
            sql2 = "SELECT * FROM test_qichacha.cc_order WHERE buyer_id='%s'" % guid
            rows = db.select_all(sql=sql2)
            list_rows = list(rows)
            assert len(list_rows) == 0, "删除订单失败"

    def change_regist_time(self, regist_time, guid):
        # 更改注册时间为当天
        sql = "UPDATE test_qichacha.cc_user SET regist_time='%s' " \
              "WHERE guid='%s'" % (regist_time, guid)
        db.update(sql=sql)
        # 验证注册时间是否更改
        sql1 = "SELECT regist_time FROM test_qichacha.cc_user WHERE guid='%s'" % guid
        rows = db.select_one(sql=sql1)
        get_regist_time = list(rows)[0]
        assert regist_time == get_regist_time, "设置注册时间失败"

    def get_user_info(self, guid):
        # 获取用户userid和groupid
        sql5 = "SELECT * FROM test_qichacha.cc_user WHERE guid='%s'" % guid
        rows = list(db.select_one(sql=sql5))
        list_rows = list(rows)
        result = {'userId': list_rows[1]}
        result1 = list(result.values())[0]
        return result1

    def use_experience_card(self, guid):
        # 查看用户是否使用体验卡，若没使用则使用
        sql = "SELECT * FROM test_qichacha.cc_user_coupon WHERE user_id='%s'" % guid
        rows = db.select_all(sql=sql)
        list_rows = list(rows)
        if len(list_rows) == 0:
            # 添加使用体验卡记录
            sql1 = "UPDATE test_qichacha.cc_user_coupon SET user_id='%s' WHERE user_coupon_status=3 LIMIT 1" % guid
            db.update(sql=sql1)
            # 验证体验卡记录是否增加
            sql2 = "SELECT * FROM test_qichacha.cc_user_coupon WHERE user_id='%s'" % guid
            rows = db.select_all(sql=sql2)
            assert len(list(rows)) == 1, "体验卡记录添加失败"

    def use_exchange_code(self, guid):
        # 查看用户是否使用兑换码，若没使用则使用
        sql = "SELECT * FROM test_qichacha.cc_cdkey_user WHERE user_id='%s'" % guid
        rows = db.select_all(sql=sql)
        list_rows = list(rows)
        if len(list_rows) == 0:
            # 添加使用兑换码记录
            sql1 = "UPDATE test_qichacha.cc_cdkey_user SET user_id='%s' WHERE status=1 LIMIT 1" % guid
            db.update(sql=sql1)
            # 验证体验卡记录是否增加
            sql2 = "SELECT * FROM test_qichacha.cc_cdkey_user WHERE user_id='%s'" % guid
            rows = db.select_all(sql=sql2)
            assert len(list(rows)) == 1, "兑换码记录添加失败"

opreation = Handle_Opreation()

if __name__ == '__main__':
    a = Handle_Opreation().change_regist_time(1631499780, '9fff7ed1205367a6ef3a0f86f0c68141')
    print(a)