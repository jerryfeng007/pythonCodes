# 移除字典键值(key/value)对
d = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
del d['Zhihu']
print(d)


d = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
d.pop('Zhihu')
print(d)


d = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
d.popitem()
print(d)


d = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
d = {k: v for k, v in d.items() if k != 'Zhihu'}
print(d)
