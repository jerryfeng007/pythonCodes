import requests
from suds.client import Client

# 利用http完成webservice接口-----get
full_url = 'http://ws.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline'
params = {"qqCode": "270062331"}
r = requests.get(full_url, params=params)
print(r.status_code)
print(r.text)

# 利用http完成webservice接口----post
full_url = 'http://ws.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline'
data = {"qqCode": "270062331"}
r = requests.post(full_url, data=data)
print(r.status_code)
print(r.text)


# 利用suds库完成webservice接口测试
def ws(url, **params):
    # 创建webservice Client对象
    client = Client(url)
    
    # 可以打印出Client对象所有的方法
    # print(client)
    
    # client.service.方法名
    result = client.service.qqCheckOnline(**params)
    print(result)
    

# 要访问的webservice地址，地址一定是以wsdl结尾的
url1 = 'http://ws.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl'
# method1 = 'qqCheckOnline'
params1 = {'qqCode': '270062331'}
ws(url1, **params1)
