"""
------------------------
Author : qichacha
Time : 2022/3/8 17:53
E-mail :981502830@qq.com
------------------------
"""
import requests
from common.handle_config import conf

url1 = conf.get('coupon_info', 'url')
headers = conf.get('coupon_info', 'headers')
params = conf.get('coupon_info', 'params')
method = conf.get('coupon_info', 'method')


class HttpRequest:

    def http_request(self, url=url1, data=None, headers=headers, http_method=method):
        if http_method.upper() == 'POST':
            try:
                res = requests.post(url, data, headers)
            except Exception as e:
                print("post请求出现了异常：{0}".format(e))
        elif http_method.upper() == 'GET':
            try:
                res = requests.get(url, data, headers)
            except Exception as e:
                print("get请求出现了异常：{0}".format(e))
        return res

if __name__ == '__main__':
    payload = {"userId": 'fcb4ab3a64929f441f5636daa385f4d9',
               "userPortraitId": "d6f181333cc5460c80cc5d025316df5d"
               }
    a = HttpRequest().http_request(data=payload)
    print(a)
    print(type(a))