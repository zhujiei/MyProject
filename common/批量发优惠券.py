"""
------------------------
Author : qichacha
Time : 2022/3/5 22:33
E-mail :981502830@qq.com
------------------------
"""
from common.request_coupon import HttpRequest
from common.handle_config import conf


url1 = conf.get('coupon_info', 'url')
headers = conf.get('coupon_info', 'headers')
method = conf.get('coupon_info', 'method')
params = eval(conf.get('coupon_info', 'params'))


class HandleParams:
    params = eval(conf.get('coupon_info', 'params'))

    @classmethod
    def handle_coupon_params(cls, usable_range, coupon_title, coupon_description, user_id='9d08fb822378b28925b6d19da3f11ffe'):
        cls.params["user_id"] = user_id
        cls.params["usable_range"] = usable_range
        cls.params["coupon_title"] = coupon_title
        cls.params["coupon_description"] = coupon_description
        return cls.params

if __name__ == '__main__':
    params1 = HandleParams.handle_coupon_params(6, 'VIP1年优惠券', 'VIP1年优惠券')
    HttpRequest().http_request(data=params1)
    params2 = HandleParams.handle_coupon_params(7, 'VIP2年优惠券', 'VIP2年优惠券')
    HttpRequest().http_request(data=params2)
    params3 = HandleParams.handle_coupon_params(17, 'VIP3年优惠券', 'VIP3年优惠券')
    HttpRequest().http_request(data=params3)
    params4 = HandleParams.handle_coupon_params(31, 'SVIP1年优惠券', 'SVIP1年优惠券')
    HttpRequest().http_request(data=params4)
    params5 = HandleParams.handle_coupon_params(32, 'SVIP2年优惠券', 'SVIP2年优惠券')
    HttpRequest().http_request(data=params5)
    params6 = HandleParams.handle_coupon_params(33, 'SVIP3年优惠券', 'SVIP3年优惠券')
    HttpRequest().http_request(data=params6)
    params7 = HandleParams.handle_coupon_params(0, 'VIP/SVIP通用优惠券', 'VIP/SVIP通用优惠券')
    HttpRequest().http_request(data=params7)

