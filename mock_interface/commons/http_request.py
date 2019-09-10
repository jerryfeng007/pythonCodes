import json
import urllib3
import requests

# 去掉运行时的Warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_form(url, path, params):
    print('Get-Form请求完整url=', url + path)
    try:
        r = requests.get(url=url+path,
                         params=params,
                         verify=False)
        return r.json(), r.elapsed.total_seconds(), r.status_code
    except Exception as e:
        print('Get-Form请求出现了异常!', str(e))


def post_form(url, path, data):
    print('Post-Form请求完整url=', url+path)
    try:
        r = requests.post(url=url+path,
                          data=data,
                          verify=False)
        return r.json(), r.elapsed.total_seconds(), r.status_code
    except Exception as e:
        print('Post-Form请求出现了异常!', str(e))


def post_json(url, path, data):
    print('Post-Json请求完整url=', url+path)
    headers = {'content-type': 'application/json'}
    # 把字典格式的data，转化为json格式的str类型的数据
    # ensure_ascii = False，解决中文编码
    data = json.dumps(data, ensure_ascii=False)
    try:
        r = requests.post(url=url+path,
                          data=data,
                          headers=headers,
                          verify=False)
        return r.json(), r.elapsed.total_seconds(), r.status_code
    except Exception as e:
        print('Post-Json请求出现了异常!', str(e))
