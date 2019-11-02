# 字典的删除

# 方式1：使用del
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
del test_dict['Zhihu']
print(test_dict)

# 方式2：使用pop
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
test_dict.pop('Zhihu')
print(test_dict)

# 移除没有的key不会报错
test_dict.pop('baidu', '不存在')
print(test_dict)

# 方式3：使用popitems
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
test_dict.popitem()
print(test_dict)

# 方式4：字典推导式？？？？？
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
# test_dict = {key: value for key, value in test_dict.items() if key != 'Zhihu'}
test_dict = {key: test_dict[key] for key in test_dict if key != 'Zhihu'}
print(test_dict)
