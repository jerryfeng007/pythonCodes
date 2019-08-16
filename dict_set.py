print('----------相对于列表和元组，字典的性能更优，特别是对应查找、添加、删除---------------------------------------')

print('--------------------------------------------------字典定义--------------------------------------------')

# 方式1
dict1 = {'a': 1, 'b': 2}  # 性能比 dict()高

# 方式2
dict11 = dict([('c', 3), ('d', 4)])
print(dict11)

# 方式3
dict12 = dict(name='jerry', age=18)
print(dict12)

# 方式4
dict2 = {}.fromkeys('abcde')  # 可以是字符串、列表、元组
print(dict2)

dict3 = {}.fromkeys('abcde', 'hello')
print(dict3)

# ------------------------------------fromkeys举例--------------------------------------------------

con = ['a', 'b', 'c', 'b', 'name', 'a', 'name']  # 列表有重复的元素
d = {}.fromkeys(con)
print(d)  # {'a': None, 'b': None, 'c': None, 'name': None} 虽然列表中有重复的元素，但生成字典却没有重复的key

# 方式5 --------这个估计很有用
zip1 = zip('abcde', '12345')  # 都是字符串
dict4 = dict(zip1)
print(dict4)

zip2 = zip(['张三', '李四'], ['数学', '英语'])  # 都是列表
dict5 = dict(zip2)
print(dict5)

zip3 = zip(('张三', '李四'), ('数学', '英语'))  # 都是元组
dict6 = dict(zip3)
print(dict6)

print('--------------------------------------------------key和value--------------------------------------------')

# key不可以重复，但value可以重复
# 如果key有重复，那么以最后一个为准
# key只能为不可变类型，不能为列表、字典等
dict5 = {'aa': 11, 'bb': 22, 'cc': 33, 'cc': 44}
print(dict5)

# key列表、value列表
dict6 = {'a': 1, 'b': 2, 'c': 3}
print(dict6.keys())
print(dict6.values())

print('--------------------------------------------------字典的取值--------------------------------------------')

# 一般
dict2 = {'a': 1, 'b': 2, 'c': 3}
print(dict2['a'])      # 返回该键值, 取不到时，会报错

# 使用get
print(dict2.get('d'))  # 返回该键值, 取不到时，不会报错，返回None
print(dict2.get('d', 'ff'))  # 返回该键值, 取不到时，给一个默认值，编程中经常用的一种情况，但dict2不变

# 使用setdefault
print(dict2.setdefault('nn'))  # 返回该键值，取不到时，不会报错，返回None

print('--------------------------------------------------更新字典--------------------------------------------')

# 单个更新字典
dict5 = {'a': 1, 'b': 2, 'c': 3}
dict5['c'] = 'jerry'  # 修改
print(dict5)

dict5['d'] = 'tom'  # 没有该键，就新增一个
print(dict5)

# update  # 批量更新字典
dict6 = {'a': 1, 'b': 2, 'c': 3}
dict6.update({'a': 1})  # 不变
print(dict6)

dict6.update({'a': 11})  # 修改
print(dict6)

dict6.update({'x': 1})  # 不存在x键，会创建一个
print(dict6)

print('------------------------------------案例：把数据加到一个空字典--------------------------------------------')

# 方式1
con = [1, 2, 3, 2, 1, 4]  # 这个列表有重复的元素
d = {}  # 定义一个空字典
for key in con:
    if key not in d:  # 避免重复key  个人认为最好还是要加这个判断，避免额外的计算、赋值、去重
        d[key] = con.count(key)
print(d)

# 方式2
con = [1, 2, 3, 2, 1, 4]
d = {}
for key in con:
    d[key] = con.count(key)  # 即使不判断，字典也不会允许存在重复的key，会过滤
print(d)

print('--------------------------------------------------删除字典--------------------------------------------')

# del
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
del dict4['b']
print(dict4)

# del dict4  # 删除这个字典对象

# pop  根据key删除
dict4.pop('f')
print(dict4)

# popitem  删除键值对，默认最后一个
dict4.popitem()
print(dict4)

# clear 清空
dict4.clear()
print(dict4)

print('--------------------------------------------------遍历字典--------------------------------------------')

# 直接遍历--遍历的是key
dict6 = {'aa': 11, 'bb': 22, 'cc': 33}
for i in dict6:
    print(i, dict6[i])

# 遍历keys()
for key in dict1.keys():
    print(key, dict1[key])

# 遍历items()
dict1 = {'a': 1, 'b': 2, 'c': 3}
for k, v in dict1.items():
    print(k, v)

print('--------------------------------------------------字典的方法--------------------------------------------')

# len()
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(len(dict1))

# in  not in--------判断key值是否在
dict5 = {'aa': 11, 'bb': 22, 'cc': 33}
print('bb' in dict5)

print('--------------------------------------------------字典的拷贝--------------------------------------------')
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = d1
d3 = d1.copy()
print(id(d1), id(d2), id(d3))  # 前两个id一样，后一个不一样

d1['d'] = 4

print(d1)  # 变
print(d2)  # 变
print(d3)  # 不变

print('---------------------------------------------字典的排序------------------------------------------------------')

# sorted
d = {'b': 4, 'a': 9, 'f': 0, 's': 2}
print(sorted(d.items(), key=lambda x: x[0]))
print(sorted(d.items(), key=lambda x: x[0], reverse=True))
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
