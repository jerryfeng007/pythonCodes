import requests

print('--------------------------------------cookies-------------------------------------------------------')

url = 'https://sso.baidu.cn/sso/ssgin'
data = {'Passwd': 'e809f', 'Passwd1': '8a19f', 'isVerifyCode': 'false', 'verifyCode': '', 'fromId': 'jrj'}

# 登录
r = requests.post(url, data=data, verify=False)
cookies = r.cookies

# 系统通知页面
url1 = 'http://i.baidu.com.cn/home/myNews'
r1 = requests.post(url1, cookies=cookies, verify=False)
print(r1.text)
