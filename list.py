import copy

print('-------------------------------------------列表的定义---------------------------------------------------')
# 方式1
list1 = [1, 2, 3]  # 相比方式2，效率更高

# 方式2
# 把字符串转变为列表
list2 = list('abcde')
print(list2)

print('-------------------------------------------列表转化为字符串--------------------------------------------------')

s = ''.join(list2)
print(s)

print('-------------------------------------------列表的索引--------------------------------------------------')

list2 = [1, 2, 3, 4, 5]
print(list2[0])
print(list2[-1])
print(list2[:])
print(list2[::])
print(list2[::2])
print(list2[::-1])  # 反转
print(list2[4:1:-1])
print(list2[-1:-4:-1])
print(list2[4:1:1])  # 空，因为取不到

print('-------------------------------------------列表的修改--------------------------------------------------')

list2[0] = 'a'
print(list2)

print('-------------------------------------------列表的添加--------------------------------------------------')

# append
list3 = [1, 2]
list3.append(3)
list3.append([11, 22, 33])
print(list3)

# extend
list3.extend('tom')  # 分别把t、o、m插入尾部
print(list3)

# insert
list3.insert(1, 'kk')  # 索引为1的地方插入kk
print(list3)

print('-------------------------------------------列表的删除--------------------------------------------------')

# pop 删除最后一个
list3.pop()
print(list3)
list3.pop(5)
print(list3)

# remove
list3.remove([11, 22, 33])
print(list3)

# clear
l4 = [1, 3, 5]
l4.clear()     # 清空列表 {}
print(l4)

# del
del list3[4]
print(list3)
# del list3  # 删除这个列表对象

print('-------------------------------------------列表的拼接--------------------------------------------------')

list4 = [1, 2, 3]
list2 = [4, 5]
list3 = list4 + list2
print(list3)

print('-------------------------------------------列表的方法--------------------------------------------------')

# max  min  sum
list5 = [1, 2, 3, 4, 5]
print(max(list5))
print(min(list5))
print(sum(list5))

# 查找
# 不同于字符串，列表只有index，没有find
list3 = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
print(list3.index(5))  # 返回索引，如果不存在就会报错

# 统计
print(list3.count(1))

# in  not in
print(6 in list3)

print('-------------------------------------------列表的排序--------------------------------------------------')

# sort
list4 = [1, 2, 9, 4, 0]
list4.sort()  # 默认升序
print(list4)  # 改变了原列表

list4 = [1, 2, 9, 4, 0]
list4.sort(reverse=True)  # 降序
print(list4)

# sorted
list4 = [1, 2, 9, 4, 0]
print(sorted(list4))  # 不会改变原列表
print(list4)

# reverse 反转
list5 = [1, 2, 'a', 'b']
list5.reverse()
print(list5)

print('-------------------------------------------列表的遍历--------------------------------------------------')

# while
list6 = [1, 2, 3, 4]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# for
for i in list1:
    print(i)

# for
for i in range(len(list1)):
    print(list1[i])

print('-------------------------------------------列表的拷贝--------------------------------------------------')

# copy
l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy()
print(l1, l2, l3)  # 都等于[1, 2, 3]
print(id(l1), id(l2), id(l3))  # l1和l2的id一样，但与l3的id不一样

# 深浅拷贝
'''
深拷贝：拷贝所有对象，包括顶级对象、嵌套对象，所有原始对象的改变不会造成深拷贝里任何子元素的改变
浅拷贝：只拷贝顶级对象，不拷贝嵌套对象，所以原始数据改变，嵌套对象会改变
'''
a = [1, 2, 3, [4, 5]]
b = copy.deepcopy(a)
c = copy.copy(a)
print(b)
print(c)

a[3].append(6)  # 会影响浅拷贝，不会影响深拷贝
a.append(7)  # 既不影响浅拷贝，也不影响深拷贝
print(a)
print(b)
print(c)

print('-------------------------------------------列表的嵌套--------------------------------------------------')

# [['语文', '数学', '英语'], ['语文', '数学', '英语'], ['语文', '数学', '英语']]
student = ['张三', '李四', '王五']
kecheng = ['语文', '数学', '英语']
l = []
for s in student:
    temp = []
    for k in kecheng:
       temp.append(k)
    l.append(temp)
print(l)

print('-------------------------------------------列表推导式--------------------------------------------------')

# 非列表推导式
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 列表推导式---更简单，执行效率高
list1 = [i for i in range(10)]
print(list1)
