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

print('--------------------------------------------------集合的定义--------------------------------------------')
'''
集合用set{}表示
如果{}表示字典
无序
并且不允许重复
'''
# 方式1
set1 = {1, 2, 3}

# 方式2
set2 = set('abcde')  # 也可以是列表
print(set2)

# 空集合      注意：{}是空字典
set3 = set()

print('--------------------------------------------------集合的去重--------------------------------------------')

# 去重
set4 = {1, 1, 2, 2, 3, 3, 4}
print(set4)

# 因为set()不允许重复
# 所以可以用set()给列表、元组、字符串去重，然后再转化为列表、元组、字符串
list1 = [1, 1, 2, 2, 3]
list2 = list(set(list1))
print(list2)

# in not in
s = {1, 2, 3}
print(2 in s)

print('--------------------------------------------------集合的方法--------------------------------------------')

# add  # 当作一个
set11 = {1, 2, 3, 4}
set11.add(5)
set11.add((6, 7))
print(set11)

# update  # 当作多个
set11.update('8')
set11.update([9, 10])
set11.update((11, 12))
print(set11)

# remove
set2 = {1, 2, 3, 4, 5}
set2.remove(3)
print(set2)

# pop  # 删除最后一个，但集合无序，不知道会删除哪个，所以要慎用
set2.pop()
print(set2)

# clear
set3.clear()
print(set3)  # 显示空集合 set()

print('--------------------------------------------------集合的排序--哈哈------------------------------------------')
s = {2, 0, -3, 5}
print(sorted(s))

# 结束
# 测试1
# 测试2
