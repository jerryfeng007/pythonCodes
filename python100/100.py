# 列表转换为字典。

l = ['name', 'age', 'sex']
d = {}.fromkeys(l)
print(d)

l2 = ['name', 'age', 'sex']
value = ['jerry', 18, 'female']
dd = dict(zip(l2, value))
print(dd)
