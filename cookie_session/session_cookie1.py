import requests

print('--------------------------------------session-------------------------------------------------------')

s = requests.session()


def login():
    url = 'https://so.com.cn/sso/ssopartln'
    data = {'isPersist': 0, 'LoginID': 'xxxxxxxxxxxxxx',
            'Passwd': 'e807f1fc18ca6738a19f', 'Passwd1': 'e807f8a19f', 'verifyCode': ''}
    # 登录
    s.post(url, data=data, verify=False)


def check_login(func):
    def wrapper():
        login()
        func()
    return wrapper


@check_login
def notice():
    # 系统通知页面
    url1 = 'http://i.baidu.com.cn/home/userSetting/myNe'
    r1 = s.post(url1, verify=False)
    print(r1.text)


notice()
