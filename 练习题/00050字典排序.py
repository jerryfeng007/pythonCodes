# 给定一个字典，然后按键(key)或值(value)对字典进行排序。

d1 = {'name': 'jerry', 'sex': 'male', 'age': 'eighting'}
print(sorted(d1.items(), key=lambda x: x[0]))
print(sorted(d1.items(), key=lambda x: x[1]))


# 字典列表排序
lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]

# 通过age升序
print(sorted(lis, key=lambda x: x['age']))

# 通过age排序，再按name排序
print(sorted(lis, key=lambda x: (x['age'], x['name'])))

# 按 age 降序排序
print(sorted(lis, key=lambda x: x['age'], reverse=True))
