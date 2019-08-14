import json

print('----------------------------------------json序列化-------------------------------------------------')

'''
你可以把它简单地理解为两种黑箱：
第一种，输入些杂七杂八的信息，比如 Python 字典，输出一个字符串
第二种，输入这个字符串，可以输出包含原始信息的 Python字典

序列化：把 dict转换为json格式的str， 使用json.dumps()
反序列化：把json格式的str转换为dict，使用json.loads()
'''

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

# dict类型 ---> json格式的str类型
params_str = json.dumps(params)
print('after json serialization')
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

# str类型 ---> dict类型
original_params = json.loads(params_str)
print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
