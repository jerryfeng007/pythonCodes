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

# index
# 不同于字符串，列表只有index，没有find
list3 = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
print(list3.index(5))  # 返回索引，如果不存在就会报错

# count
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

print('-------------------------------------------深浅拷贝--------------------------------------------------')

'''
深拷贝：拷贝所有对象，包括顶级对象、嵌套对象，所有原始对象的改变不会造成深拷贝里任何子元素的改变
浅拷贝：只拷贝顶级对象，不拷贝嵌套对象，所以原始数据改变，嵌套对象会改变
'''
a = [1, 2, 3, [4, 5]]
b = copy.deepcopy(a)
c = copy.copy(a)
print(a, b, c)              # 虽然都相等
print(id(a), id(b), id(c))  # 但既然是copy，id都不一样

a.append(7)  # 既不影响浅拷贝，也不影响深拷贝
a[3].append(6)  # 会影响浅拷贝，不会影响深拷贝
print(a)
print(b)
print(c)

print('-------------------------------------------如何理解列表的可变--------------------------------------------------')

# 场景1
l8 = [1, 3, 4]
print(id(l8))
# 如果想改变l8，比如变为 [1, 3, 4, 5]
# 直接在后面append即可，但是id是不变的
l8.append(5)
print(l8)
print(id(l8))

# 场景2
l1 = [1, 2, 3]
l2 = [1, 2, 3]  # l1和l2的 id不一样
print(id(l1), id(l2))

# 场景3
l3 = l4 = [5, 1, 'a', 3, 4]  # l3和l4的id一样
print(id(l3), id(l4))
l3.extend('ab')
print(l4)       # l4也会变，因为和l3是一个地址

# 场景4
l5 = [1, 2, 3]
l6 = l5
l7 = l5.copy()
print(id(l5), id(l6), id(l7))  # l5和l6的id一样，但与l7的id不一样
l5.append(4)
print(l6)  # l6也变了， 因为l6和l5是一个地址
print(l7)  # l7没变，因为l7地址不一样

print('-------------------------------------------列表嵌套元组--------------------------------------------------')

l12 = [1, 2, (3, 4, 5), 6]
print(id(l12))
l12[2] = (0, 1)
print(id(l12))   # 操作之后，id不会变

print('-------------------------------------------列表嵌套列表--------------------------------------------------')

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

print('----------------------------------列表生成式、列表推导式-------------------------------------')
# 列表生成式
l = range(1, 1000, 20)
print(l)

# 列表推导式(最简单)
l = list(x*2 for x in [1, 2, 3])
print(l)

# 或者
l = [x * 2 for x in [1, 2, 3]]  # 映射解析，一对一
print(l)

# 等价于(使用了匿名函数)
l = [(lambda x: x * 2)(x) for x in [1, 2, 3]]
print(l)

# 等价于(笨方法)
ll = []
for x in [1, 2, 3]:
    ll.append(x * 2)
print(ll)

# 以下都是列表推导式
l = [x * 2 for x in [1, 2, 3] if x % 2 != 0]  # 只有if，没有else
print(l)

l = [i * 2 if i > 2 else i * 3 for i in [1, 2, 3]]  # 有if，有else
print(l)

l = [x * j for x in [1, 2] for j in [2, 3]]  # 嵌套循环
print(l)

l = [x * j for x in [1, 2] for j in [2, 3] if j < 3]
print(l)

print('----------------------------------enumerate方法的使用，取索引和元素-------------------------------------')

# 可以是字符串、列表、元组
l = [1, 2, 3, 4]
for index, item in enumerate(l):
    print(index, item)

# 案例
# 给定一个list和一个指定的数字，求这个数字在list中的位置
# 注意，列表中可能有多个相同的元素


# 方法1
def jjj(l, num):
    ll = []
    for i in range(len(l)):
        if l[i] != num:
            continue
        ll.append(i)
    return ll


ll = jjj([1, 2, 3, 2, 2, 2, 2], 2)
print(ll)


# 方法2
def mmm(l, num):
    index_list = []
    for index, item in enumerate(l):
        if item == num:
            index_list.append(index)
    return index_list


lll = mmm([1, 2, 3, 2, 2, 2, 2], 2)
print(lll)
