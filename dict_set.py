# 字典--------------------------------------------------------------------------------------------------------------字典
# 字典的定义
# 方式1
dict1 = {'a': 1, 'b': 2}
print(dict1)

# 方式2
dict2 = {}.fromkeys('abcde')
print(dict2)
dict3 = {}.fromkeys('abcde', 'hello')
print(dict3)

# 方式3，使用dict()
zip1 = zip('abcdefg', '12345')
dict4 = dict(zip1)
print(dict4)

# key不可以重复，但value可以重复
# 如果同一个key有多个，那么以最后一个为准
dict5 = {'aa': 11, 'bb': 22, 'cc': 33, 'cc': 44}
print(dict5)

# 字典的方法
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.keys())
print(dict1.values())

# in
dict5 = {'aa': 11, 'bb': 22, 'cc': 33}
print('bb' in dict5)  # 只判断key值是否在

# 字典的方法
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1.update({'a': 1})  # 不变
print(dict1)
dict1.update({'a': 11})  # 修改
print(dict1)
dict1.update({'x': 1})  # 不存在x键，会创建一个
print(dict1)

# update: 拼接
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4}
dict1.update(dict2)
print(dict1)

# 字典的添加
dict4 = {'a': 1, 'b': 2, 'c': 3}
dict4['d'] = 'tom'  # 没有该键，就新增一个

# 字典的修改
dict3['c'] = 'jerry'
print(dict3)

# 字典的删除
# del
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
del dict4['b']
print(dict4)

# pop  根据key删除
dict4.pop('f')
print(dict4)

# popitem  删除键值对，默认最后一个
dict4.popitem()
print(dict4)

# clear 清空
dict4.clear()
print(dict4)

# 字典的取值
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])      # 返回该键值, 取不到时，会报错

print(dict1.get('d'))  # 返回该键值, 取不到时，不会报错

print(dict1.get('d', 'ff'))  # 返回该键值, 取不到时，给一个默认值，编程中经常用的一种情况，但dict1不变
print(dict1)

print(dict1.setdefault('nn'))  # 返回该键值，取不到时，不会报错

dict1.setdefault('e')  # 如果没有该键，加一个，默认值None
print(dict1)

dict1.setdefault('f', '贾跃亭')  # 如果没有该键，加一个，并设默认值，dict1会变
print(dict1)

# 可以for循环去遍历keys和values
for key in dict1.keys():
    print(key, dict1[key])

# for in 遍历
dict6 = {'aa': 11, 'bb': 22, 'cc': 33}
for i in dict6:
    print(i, dict6[i])

# items()
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.items())

l = tuple(dict1.items())  # 把键和值都放入了一个元组
print(l)

ll = list(dict1.items())  # 把键和值都放入了一个列表
print(ll)

dict1 = {'a': 1, 'b': 2, 'c': 3}
lll = list(dict1)  # 把所以键放入一个列表
print(lll)

# len()
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(len(dict1))

# copy
# 属于浅拷贝

# 集合-----------------------------------------------------------------------------------------------------------------------
'''
集合用{}表示，set表示，跟字典一样，都是无序的，并且不允许重复
'''
# 定义
set1 = {1, 2, 3}
print(set1)
set2 = set('abcde')
print(set2)

# 空集合
# 使用set()， 而不是{}， 后者是空字典

# 去重
set3 = {1, 1, 2, 2, 3, 3, 4}
print(set3)

# 因为set()不允许重复，所以可以用set()给列表、元组、字符串去重，然后再转化为列表、元组、字符串
list1 = [1, 1, 2, 2, 3]
list2 = list(set(list1))
print(list2)

# 字符串、列表、元组、集合的转换
str1 = 'hello'
list1 = list(str1)
print(list1)
tuple1 = tuple(str1)
print(tuple1)
set1 = set(str1)
print(set1)

# 集合操作
# 添加
set1 = {1, 2, 3, 4}
set1.add(5)
print(set1)

set1.update('67')
set1.update({7, 8})
set1.update([9, 10])
set1.update((11, 12))
print(set1)

# 删除
set2 = {1, 2, 3, 4, 5}
set2.remove(3)
print(set2)

set2.pop()
print(set2)

set3.clear()
print(set3)  # 显示空集合 set()