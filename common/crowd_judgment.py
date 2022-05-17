from common.handle_config import conf
from common.handle_mysql import db
from common.request_people import HttpRequest
from common.handle_log import log


class Crowd_Judgment:

    '''根据注册时间进行判断'''
    def judge_register(self, register_time):
        try:
            if register_time == 'Today':
                # 当天0点的时间戳
                today_0_time_stamp = conf.get('crowd_condition', 'today0_sql')
                today_0_time_stamp = db.select_one(today_0_time_stamp)[0]
                # 第二天0点的时间戳
                second_day_0_time_stamp = conf.get('crowd_condition', 'second_day0_sql')
                second_day_0_time_stamp = db.select_one(second_day_0_time_stamp)[0]
                # 第一步：查询当天注册的用户guid
                sql = "SELECT guid FROM test_qichacha.cc_user WHERE regist_time>'{}' and regist_time<'{}'".format\
                    (today_0_time_stamp, second_day_0_time_stamp)
                today_register = db.select_all(sql)
                today_register_guid = []
                for i in range(len(today_register)):
                    p = lambda x: x[i][0]
                    today_register_guid.append(p(today_register))
                if len(today_register_guid) == 0:
                    today_register_guid = None
                return today_register_guid
            elif register_time == 'TodayBefore':
                """由于数据量太大，查询前1天的数据"""
                # 当天0点的时间戳
                today_0_time_stamp = conf.get('crowd_condition', 'today0_sql')
                today_0_time_stamp = db.select_one(today_0_time_stamp)[0]
                before_1day_time_stamp = today_0_time_stamp - 86400*1
                # 第一步：查询当天注册的用户guid
                sql = "SELECT guid FROM test_qichacha.cc_user WHERE regist_time>'{}' and regist_time<'{}'".format\
                    (before_1day_time_stamp, today_0_time_stamp)
                today_register = db.select_all(sql)
                today_register_guid = []
                for i in range(len(today_register)):
                    p = lambda x: x[i][0]
                    today_register_guid.append(p(today_register))
                if len(today_register_guid) == 0:
                    today_register_guid = None
                return today_register_guid
            else:
                log.info("暂未找到对应注册条件")
        except Exception as e:
            log.error("查询注册用户失败")
            raise e
        else:
            log.info("查询注册用户成功")

    '''根据会员状态进行判断'''
    def judge_member_status(self, member_status, today_register_guid):
        try:
            if today_register_guid is None:
                member_guid = None
                return member_guid
            else:
                if member_status == 'P':
                    member_status_pu = conf.getint('crowd_condition', 'member_status_pu')
                    # 查询会员状态为普通用户的guid
                    member_guid = []
                    member_guid_none = []
                    for item in today_register_guid:
                        sql = "SELECT * FROM test_qichacha.cc_user WHERE guid='%s' AND groupid='%s';" % (item, member_status_pu)
                        guid = db.select_one(sql)
                        if len(guid) == 0:
                            member_guid.append(item)
                        else:
                            member_guid_none = None
                    if len(member_guid) > 0:
                        return member_guid
                    else:
                        return member_guid_none
                elif member_status == 'V':
                    member_status_vip = conf.getint('crowd_condition', 'member_status_vip')
                    # 查询会员状态为普通用户的guid
                    member_guid = []
                    member_guid_none = []
                    for item in today_register_guid:
                        sql = "SELECT * FROM test_qichacha.cc_user WHERE guid='%s' AND groupid='%s'" % (item, member_status_vip)
                        guid = db.select_all(sql)
                        if len(guid) != 0:
                            member_guid.append(item)
                        else:
                            member_guid_none = None
                    if len(member_guid) != 0:
                        return member_guid
                    else:
                        return member_guid_none
                elif member_status == 'S':
                    member_status_svip = conf.getint('crowd_condition', 'member_status_svip')
                    # 查询会员状态为普通用户的guid
                    member_guid = []
                    member_guid_none = []
                    for item in today_register_guid:
                        sql = "SELECT * FROM test_qichacha.cc_user WHERE guid='%s' AND groupid='%s';" % (item, member_status_svip)
                        guid = db.select_one(sql)
                        if len(guid) == 0:
                            member_guid.append(item)
                        else:
                            member_guid_none = None
                    if len(member_guid) > 0:
                        return member_guid
                    else:
                        return member_guid_none
                elif member_status == 'NO':
                    member_guid = today_register_guid
                    return member_guid
                else:
                    log.info("暂未找到对应注册条件")
        except Exception as e:
            log.error("查询会员状态用户失败")
            raise e
        else:
            log.info("查询会员状态用户成功")

    '''根据是否有会员订单进行判断'''
    def judge_member_order(self, member_order_status, member_guid):
        try:
            if member_guid is None:
                member_order_guid = None
                return member_order_guid
            else:
                if member_order_status == 'N':
                    member_order_guid = []
                    member_order_guid_none = []
                    for item in member_guid:
                        sql = "SELECT * from test_qichacha.cc_order WHERE buyer_id='%s' AND pay_status ='2';" % item
                        guid = db.select_all(sql)
                        if len(guid) == 0:
                            member_order_guid.append(item)
                        else:
                            member_order_guid_none = None
                    if len(member_order_guid) != 0:
                        return member_order_guid
                    else:
                        return member_order_guid_none
                elif member_order_status == 'Y':
                    member_order_guid = []
                    member_order_guid_none = []
                    for item in member_guid:
                        sql = "SELECT * from test_qichacha.cc_order WHERE buyer_id='%s' AND pay_status ='2';" % item
                        guid = db.select_all(sql)
                        if len(guid) != 0:
                            member_order_guid.append(item)
                        else:
                            member_order_guid_none = None
                    if len(member_order_guid) != 0:
                        return member_order_guid
                    else:
                        return member_order_guid_none
                elif member_order_status == 'NO':
                    member_order_guid = member_guid
                    return member_order_guid
                else:
                    print("暂未找到对应注册条件")
        except Exception as e:
            log.error("查询会员订单用户失败")
            raise e
        else:
            log.info("查询会员订单用户成功")

    '''根据是否有使用过体验卡进行判断'''
    def judge_use_experience_card(self, experience_card, member_order_guid):
        try:
            if member_order_guid is None:
                experience_card_guid = None
                return experience_card_guid
            else:
                if experience_card == 'N':
                    experience_card_guid = []
                    experience_card_guid_none = []
                    for item in member_order_guid:
                        sql = "SELECT * FROM test_qichacha.cc_user_coupon WHERE user_id='%s' AND user_coupon_status!=3" % item
                        guid = db.select_one(sql)
                        if guid != None:
                            experience_card_guid.append(item)
                        else:
                            experience_card_guid_none = None
                    if len(experience_card_guid) > 0:
                        return experience_card_guid
                    else:
                        return experience_card_guid_none
                elif experience_card == 'Y':
                    experience_card_guid = []
                    experience_card_guid_none = []
                    for item in member_order_guid:
                        sql = "SELECT * FROM test_qichacha.cc_user_coupon WHERE user_id='%s' AND user_coupon_status=3" % item
                        guid = db.select_one(sql)
                        if len(guid) != 0:
                            experience_card_guid.append(item)
                        else:
                            experience_card_guid_none = None
                    if len(experience_card_guid) > 0:
                        return experience_card_guid
                    else:
                        return experience_card_guid_none
                elif experience_card == 'NO':
                    experience_card_guid = member_order_guid
                    return experience_card_guid
                else:
                    print("暂未找到对应注册条件")
        except Exception as e:
            log.error("查询体验卡用户失败")
            raise e
        else:
            log.info("查询体验卡用户成功")

    '''根据是否有使用过兑换码进行判断'''
    def judge_use_exchange_code(self, exchange_code, experience_card_guid):
        try:
            if experience_card_guid is None:
                exchange_code_guid = None
                return exchange_code_guid
            else:
                if exchange_code == 'N':
                    exchange_code_guid = []
                    exchange_code_guid_none = []
                    for item in experience_card_guid:
                        sql = "SELECT * FROM test_qichacha.cc_cdkey_user WHERE user_id='%s' AND status!=1;" % item
                        guid = db.select_one(sql)
                        if len(guid) != 0:
                            exchange_code_guid.append(item)
                        else:
                            exchange_code_guid_none = None
                    if len(exchange_code_guid) > 0:
                        return exchange_code_guid
                    else:
                        return exchange_code_guid_none
                elif exchange_code == 'NO':
                    exchange_code_guid = experience_card_guid
                    return experience_card_guid
                elif exchange_code == 'Y':
                    exchange_code_guid = []
                    exchange_code_guid_none = []
                    for item in experience_card_guid:
                        sql = "SELECT * FROM test_qichacha.cc_cdkey_user WHERE user_id='%s' AND status=1;" % item
                        guid = db.select_one(sql)
                        if len(guid) != 0:
                            exchange_code_guid.append(item)
                        else:
                            exchange_code_guid_none = None
                    if len(exchange_code_guid) > 0:
                        return exchange_code_guid
                    else:
                        return exchange_code_guid_none
                elif exchange_code == 'NO':
                    exchange_code_guid = experience_card_guid
                    return exchange_code_guid
                else:
                    print("暂未找到对应注册条件")
        except Exception as e:
            log.error("查询兑换码用户失败")
            raise e
        else:
            log.info("查询兑换码用户成功")

    '''根据UserID尾号进行判断'''
    # def judge_userid_number(self, end_number, exchange_code_guid):
    #     if end_number == 'None':
    #         end_number_guid = exchange_code_guid
    #         return end_number_guid
    #     elif end_number == '1':
    #         end_number_guid = []
    #         for item in exchange_code_guid:
    #             sql = "SELECT '{}' FROM test_qichacha.cc_user WHERE guid LIKE '%1';".format(item)
    #             guid = db.select_one(sql)
    #             end_number_guid.append(guid)
    #         return end_number_guid

    '''判断是否查询到guid'''
    def judge_is_found(self, guid_tuple):
        if guid_tuple == None:
            return False
        else:
            return True

    '''判断是否符合人群接口'''
    def judge_is_crowd(self, userId, userPortraitId):
        payload = {"userId": userId,
                   "userPortraitId": userPortraitId
                   }
        result = HttpRequest().http_request(data=payload)
        return result


if __name__ == '__main__':
    t = Crowd_Judgment().judge_register('Today')
    print(t)
