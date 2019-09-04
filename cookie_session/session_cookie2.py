import requests

print('--------------------------------------cookies-------------------------------------------------------')

url = 'https://sso.jrj.com.cn/sso/ssopassportlogin'
data = {'ReturnURL': 'http://www.jrj.com.cn', 'isPersist': 0, 'LoginID': '18601931298',
        'Passwd': 'e807f1fcf82d132f9bb018ca6738a19f', 'Passwd1': 'e807f1fcf82d132f9bb018ca6738a19f',
        'Password': '1234567890', 'isVerifyCode': 'false', 'verifyCode': '', 'fromId': 'jrj'}

# 登录
r = requests.post(url, data=data, verify=False)
cookies = r.cookies

# 系统通知页面
url1 = 'http://i.jrj.com.cn/home/userSetting/myNews'
r1 = requests.post(url1, cookies=cookies, verify=False)
print(r1.text)
