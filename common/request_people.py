import requests
import json
from common.handle_config import conf

url1 = conf.get('request', 'url')
headers = conf.get('request', 'headers')


class HttpRequest:

    def http_request(self, url=url1, data=None, headers=headers, http_method='POST'):
        if http_method.upper() == 'POST':
            try:
                res = requests.post(url, data, headers)
                data = json.loads(res.text)
                data1 = data['isSatisfy']
                print("正在进行post请求")
            except Exception as e:
                print("post请求出现了异常：{0}".format(e))
        elif http_method.upper() == 'GET':
            try:
                res = requests.get(url, data, headers)
                data = json.loads(res.text)
                data1 = data['isSatisfy']
                print("正在进行get请求")
            except Exception as e:
                print("get请求出现了异常：{0}".format(e))
        return data1

if __name__ == '__main__':
    payload = {"userId": 'fcb4ab3a64929f441f5636daa385f4d9',
               "userPortraitId": "d6f181333cc5460c80cc5d025316df5d"
               }
    a = HttpRequest().http_request(data=payload)
    print(a)
    print(type(a))
