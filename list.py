# 列表的定义
# 方式1
list1 = [1, 2, 3]

# 方式2，把字符串转变为列表
list2 = list('abcde')
print(list2)

# 把列表转化为字符串
s = ''.join(list2)
print(s)

# 列表的索引
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

# 列表的修改
list2[0] = 'a'
print(list2)

# 列表的添加 append  extend  insert
list3 = [1, 2]
list3.append(3)
list3.append([11, 22, 33])
print(list3)
list3.extend('tom')  # 分别把t、o、m插入尾部
print(list3)
list3.insert(1, 'kk')
print(list3)

# 列表的删除  pop remove  del  clear
list3.pop()
print(list3)
list3.pop(5)
print(list3)
list3.remove([11, 22, 33])
print(list3)
del list3[4]
print(list3)
# del list3

# 列表的相加
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = list1 + list2
print(list3)

# 列表的计算  max  min  sum
list1 = [1, 2, 3, 4, 5]
print(max(list1))
print(min(list1))
print(sum(list1))

# 列表的查找（不同于字符串，列表只有count和index，没有find）
list3 = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
print(list3.count(1))
print(list3.index(5))  # 返回索引，如果不存在就会报错
print(6 in list3)

# 列表的排序  sort  reverse   sorted
list4 = [1, 2, 9, 4, 0]
list4.sort()  # 升序
print(list4)
list4 = [1, 2, 9, 4, 0]
list4.sort(reverse=True)  # 降序
print(list4)
list4 = [1, 2, 9, 4, 0]
print(sorted(list4))  # 不会改变存储的顺序

# 反转
list5 = [1, 2, 'a', 'b']
list5.reverse()
print(list5)

# 列表的遍历
# while
list1 = [1, 2, 3, 4]
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

# copy
l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy()
print(l1, l2, l3)  # 都等于[1, 2, 3]
print(id(l1), id(l2), id(l3))  # 但，l3，的id不一样

# 非列表推导式
list2 = []
for i in range(10):
    list2.append(i)
print(list2)

# 列表推导式---更简单，执行效率高
list1 = [i for i in range(10)]
print(list1)

# 深浅拷贝
'''
深拷贝：拷贝所有对象，包括顶级对象、嵌套对象，所有原始对象的改变不会造成深拷贝里任何子元素的改变
浅拷贝：只拷贝顶级对象，不拷贝嵌套对象，所以原始数据改变，嵌套对象会改变
'''
import copy
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