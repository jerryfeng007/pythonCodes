# 给定一个字典，然后按键(key)或值(value)对字典进行排序。

d = {'name': 'jerry', 'age': 18, 'sex': 'female'}
print(sorted(d.items(), key=lambda x: x[0]))
print(sorted(d.items(), key=lambda x: x[0], reverse=True))


d = {'name1': 20, 'name2': 18, 'name3': 30}
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=lambda x: x[1], reverse=True))

print('----------------------------------------------------------------------------------------------')
# 字典列表
lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]

print(sorted(lis, key=lambda x: x['age']))
print(sorted(lis, key=lambda x: x['name'], reverse=True))


# 先按 age 排序，再按 name 排序
print(sorted(lis, key=lambda x: (x['age'], x['name'])))
