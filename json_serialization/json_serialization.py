import json

print('----------------------------------------json序列化、反序列化-------------------------------------------------')

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

print('-----------------------------------输出字符串到文件、从文件再读取json字符串-------------------------------------------------')

# 应用场景
# 当开发一个第三方应用程序时，可以通过 JSON 将用户的个人配置输出到文件，方便下次程序启动时自动读取

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

# 备注：如果是文件操作，就使用dump和load，而不是dumps和loads
with open('params.json', 'w') as fout:
    json.dump(params, fout)  # 注意这里是 dump，不是dumps

with open('params.json', 'r') as fin:
    original_params = json.load(fin)     # 注意这里是 load，不是loads

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

# print('-------------------------------------格式优美---------------------------------------------------')
#
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# n = json.dumps(data)
# print(n)
#
# # 使用indent=4
# o = json.dumps(data, indent=4)
# print(o)
