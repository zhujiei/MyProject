import pytest
from common.handle_excel import HandleExcel
from common.handle_path import DATAS_DIR
from common.crowd_judgment import Crowd_Judgment
from common.handle_log import log


'''
1、读取excel中每条用例，根据不同条件执行对应sql语句
2、将最后筛选出来的用户guid进行人群接口判断，将结果写入excel中
'''
t = HandleExcel(DATAS_DIR + '\人群管理用例.xlsx', '人群')
cases = t.read_data()


class TestPeopleManage:
    """测试用例批量执行"""
    @pytest.mark.parametrize('case', cases)
    def test_crowd_management(self, case):
        register_guid = Crowd_Judgment().judge_register(case['注册时间'])
        member_guid = Crowd_Judgment().judge_member_status(case['会员状态'], register_guid)
        member_order_guid = Crowd_Judgment().judge_member_order(case['是否有会员订单'], member_guid)
        experience_card_guid = Crowd_Judgment().judge_use_experience_card(case['是否使用过体验卡'], member_order_guid)
        exchange_code_guid = Crowd_Judgment().judge_use_exchange_code(case['是否使用过兑换码'], experience_card_guid)
        a = Crowd_Judgment().judge_is_found(exchange_code_guid)
        if a is False:
            t.write_data(row=case['testcase_id']+1, column=13, value="未查询到符合的guid")
        else:
            exchange_code_guid1 = exchange_code_guid[0]
            result = Crowd_Judgment().judge_is_crowd(exchange_code_guid1, case['实验组ID'])
            try:
                assert result == case['Expected'], '人群接口判断不一致'
            except Exception as e:
                log.error("人群接口判断不一致")
                raise e
            else:
                log.info("人群接口判断通过")
            finally:
                t.write_data(row=case['testcase_id']+1, column=13, value=exchange_code_guid1)


if __name__ == '__main__':
    pytest.main()


