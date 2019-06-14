# 申建明课程---Python入门精讲视频课程

# python基本数据类型---数字
# int、float
a = 20
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)     # 注意，这里是4.0，不是4
print(a//b)    # 整除
print(a % b)   # 取余/取模
print(a**3)    # 幂，a的3次方
# 字符串--------------------------------------------------------------------------------------------------字符串
# 字符串的定义：单引号、双引号、三单引号、三双引号
# 三单引号、三i双引号可以写多行
s1 = 'i love u'
s2 = "i love u"
s3 = '''
i love u
Do u love me?
'''
s4 = """
i love u
i love him!
"""
s5 = "i'm a teacher"
s6 = 'the "name" is jerry'
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

# str()函数，把其他类型的转为字符串
a = 20
print(type(a))
a = str(a)
print(type(a))

# 三单引号/三双引号可以用来做注释，多行注释
'''
这是三单引号，
这是注释，
不会被执行
'''
"""
这是三双引号，
也是注释，
也不会被执行
"""

# 字符串的拼接
a = 'hello'
b = ' world'
c = a + b
print(c)

# 字符串的分割
s = 'hello_world_jerry'
s1 = s.split('_')
print('s1=', s1)
s = 'hello world jerry'
s1 = s.split(' ')
print('s1=', s1)

# 字符串中的特殊字符
# \n 换行  \r 回车
print('i\nlove\nu')

# 在特殊字符前加\，会把特殊字符转义掉
print('i\\nlove\\nu')

# 字符串格式化操作，主要有4种：%s  %d   %f   %.2f
name = 'tom'
age = 18
f1 = 1.85
print('%s is %d years old' % (name, age))
print('身高为%f，保留2位小数是%.2f' % (f1, f1))
# 还可以使用format
print('{} is {} years old'.format(name, age))
print(f'{name} is {age} years old')

# 字符串的索引
'''
h    e    l     l    o
0    1    2     3    4
-5   -4  -3    -2   -1
'''
s = 'hello'
print(s[0])
print(s[-1])
print(s[:])
print(s[::])
print(s[::2])
print(s[::-1])  # 反转
print(s[4:1:-1])  # -代表从右往左，从4开始，取的1的前一位
print(s[-1:-4:-1])  # -代表从右往左，从-1开始，取的-4的前一位
print(s[4:1:1])  # 空，因为取不到

# 字符串的方法--strip()  默认去除两边的空格，去除内容可以指定
# s1 = input('请输入一个数字：').strip()
# print(s1)
s2 = '   hello   '.strip()
print(s2)

# 字符串的方法--查找
# find 和 index功能类似，都是返回要找的字符的索引，区别是如果找不到时，find返回-1，index会报错
s3 = 'hello'
print(s3.count('l'))
print(s3.find('o'))
print(s3.index('o'))
print(s3.find('p'))
# print(s3.index('p'))

# 字符串的方法--替换
print(s3.replace('l', 'L'))

# 字符串的方法--大小写
s1 = 'heLLo'
if s1.lower() == 'hello':
    print('登录成功')
if s1.upper() == 'HELLO':
    print('登录成功')

# 字符串的方法--判断
s = 'helloworld123'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('h'))
print(s.endswith('d'))
print(s.isspace())

# 字符串的编码、解码
# ASCII码
print(ord('A'))
print(chr(65))

s = '马云非'
s1 = s.encode('gbk')
s2 = s.encode('utf8')
print(s1)
print(s2)
s3 = s1.decode('gbk')
s4 = s2.decode('utf8')
print(s3)
print(s4)

# 字符串长度
s = 'jerry'
print(len(s))

# input() ------用户输入的任何内容，都当做字符串
# name = input('请输入您的姓名：')
# print(name)

# 变量------------------------------------------------------------------------------------------------------
# 赋值的3种方式
name = 'jerry'            # 传统赋值
name1 = name2 = 'tom'     # 链式赋值
name3, age = 'jerry', 18  # 序列解包赋值

# 查看变量的类型
a = '34'
print(type(a))

# 查看地址
name = user = 'Tom'
print(id(name))
print(id(user))

# is is not
'''
只有当id(a) id(b) 相等的时候， a is b 才是真的
'''
print('哈哈哈！', name is user)

# 关键字列表
import keyword
print(keyword.kwlist)

# 推荐命名方法
student_name_list = ['Tom', 'Jerry', 'Lucy']

# 列表-----------------------------------------------------------------------------------------------------------列表
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

# 列表的添加
list3 = [1, 2]
list3.append(3)
list3.append([11, 22, 33])
print(list3)
list3.extend('tom')  # 分别把t、o、m插入尾部
print(list3)
list3.insert(1, 'kk')
print(list3)

# 列表的删除
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

# 列表的查找（不同于字符串，列表只有count和index，没有find）
list3 = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
print(list3.count(1))
print(list3.index(5))  # 返回索引，如果不存在就会报错
print(6 in list3)

# 列表的排序
list4 = [1, 2, 9, 4, 0]
list4.sort()  # 升序
# list4.sort(reverse=True)  # 降序
print(list4)

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

# 元组-------------------------------------------------------------------------------------------------------------元组
# 元组的定义
# 方式1
tuple1 = (1, 2, 3, 4)

# 方式2，把字符串转化为元组
tuple2 = tuple('abcde')
print(tuple2)

# 把元组转化为字符串，跟列表转化为字符串一样，也是用''.join()函数
s = ''.join(tuple2)
print(s)

# 元组的索引
tuple3 = tuple('hello')
print(tuple3[0])
print(tuple3[-1])
print(tuple3[:])
print(tuple3[::])
print(tuple3[::2])
print(tuple3[::-1])  # 反转
print(tuple3[4:1:-1])
print(tuple3[-1:-4:-1])
print(tuple3[4:1:1])
'''
列表的索引，和字符串的索引不完全一样，因为可以通过列表的索引来修改列表
元组的索引，和字符串的索引完全一样，因为字符串和元组都是不可修改的
'''
# 元组的特性
# 不加括号，默认是元组
a = 1, 2
print(a)
# 如果元组只有一个元素，也需要加逗号
b = 1
c = 1,
d = (1)
e = (1,)
print(b, c, d, e)
'''
因为元组的方法比较少，而且元组不可以被修改，所以他的安全性和稳定性比较好，经常被作为配置文件的一部分
如果只有一个元素，一定不要忘记加逗号， path = （pathname,）
'''
# 元组的方法
tuple4 = ('a', 'b', 'c', 'a', 'e')
print(tuple4.count('a'))
print(tuple4.index('a'))  # 返回索引，如果不存在则报错
'''
字符串有index和find方法，列表和元组只有index
index如果找不到会报错，find找不到返回-1
'''
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

# 字典的方法
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.keys())
print(dict1.values())

# 可以for循环去遍历keys和values
for key in dict1.keys():
    print(key, dict1[key])

# in
dict5 = {'aa': 11, 'bb': 22, 'cc': 33}
print('bb' in dict5)  # 只判断值是否在

# for in 遍历
dict6 = {'aa': 11, 'bb': 22, 'cc': 33}
for i in dict6:
    print(i, dict6[i])

# 字典的方法
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1.update({'a': 1})  # 不变
print(dict1)
dict1.update({'a': 11})  # 修改
print(dict1)
dict1.update({'x': 1})  # 不存在x键，会创建一个
print(dict1)

# update方法一般做什么用呢？----拼接
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4}
dict1.update(dict2)
print(dict1)

# 字典的添加
dict3 = {'a': 1, 'b': 2, 'c': 3}
dict3['d'] = 'tom'  # 没有该键，就新增一个

# 字典的修改
dict3['c'] = 'jerry'
print(dict3)

# 字典的删除
# del
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
del dict4['b']
print(dict4)

# pop
dict4.pop('f')
print(dict4)

# popitem
dict4.popitem()
print(dict4)

# clear
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

'''总结----------------------------------------------------------------------------------------------------------------------
字符串是有序的，不可修改的
列表是有序的，可修改的
元组是有序的，不可修改的
字典是无序的，可修改的
集合是无序的，可修改的，不允许重复的

总结：
字典、集合是无序的
因为字典、集合无序，所以没有索引
数字、字符串、元组不可修改，列表、字典、集合可修改

字典的特点：
因为字典是无序的，所以字典没有索引值
因为字典没有索引值，所以字典以键取值
因为字典以键取值，所以字典的键唯一且不可修改
因为字典的键不可修改，所以列表和字典不可以给字典做键

数据类型主要有：数字、字符串、列表、元组、字典、集合
不可变类型：数字、字符串、元组
可变类型：列表、字典、集合
'''

# python运算--------------------------------------------------------------------------------------------------------------
# bool
# true: 非0、非空
# false：0、空、none
# 逻辑运算符  and   or   not
# 先后顺序： 非 且 或

# 自增运算
a = 10
a += 1
a -= 1
a *= 1
a /= 1
a **= 1
a //= 1
a %= 1

# 比较运算符
'''
>  <   ==   >=    <=   !=
'''

# 流程控制三兄弟：if for while ---------------------------------------------------------------------------------------------
# if语句：注意，要减少不必要的判断，比如以下：
a = 5
if a > 4:
    print('a大于4')
elif a > 3:
    print('a大于3')
else:
    print('a大于2')

# 第一种方式，满足if条件之后，就不会再判断elif和else了
'''
if xxx:
    xxxx
elif xxx:
    xxxx
else:
    xxxx
'''

# 第二种方式，每一个if都会判断
'''
if xxx:
    xxxx
if xxxxx:
    xxxxxx
if xxxxx:
    xxxxxxx
'''

# for循环
# 使用range
for i in range(3):
    print(i)

for i in range(2, 10):
    print(i, end='_')  # print函数，使用了end

print()  # 换行

# 不使用range
for i in [1, 2, 3]:
    print(i, end=' ')

print()   # 换行

# 可迭代对象
# 字符串、列表、元组、集合

# 特殊的for循环
a = [(1, 2), (3, 4)]
# 方式1
for i in a:
    print(i[0])

# 方式2  类似序列解包赋值？ a, b = 1, 2
for i, j in a:
    print('i=', i, 'j=', j)

# 嵌套循环
for i in range(3):
    for j in range(2):
        print(i, j)

# while循环---------------------------------------------------------------------------------------------------------------
'''
while循环是深度循环，只要条件满足就会一直执行下去，直到不满足；for循环是广度循环
如果while循环一直满足条件，那么就成了死循环
'''
# 死循环
# while True:
#     print('111111111111')

# 普通循环
i = 0
while i < 5:
    print(i)
    i += 1

# 流程控制词：pass  continue   break--------------------------------------------------------------------------------------------
# pass  占位
for i in range(3):
    pass

# break 跳出循环
name = 'jerry'
for i in name:
    if i == 'e':
        break
    print(i)

a = 0
while a < 5:
    a += 1
    if a == 3:
        break
    print(a)

# continue # 结束本次循环，继续进行下一次循环
name = 'jerry'
for i in name:
    if i == 'e':
        continue
    print(i)

a = 0
while a < 5:
    a += 1
    if a == 3:
        continue
    print(a)

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

# 导入模块basic2
import basic2
v3 = basic2.add(4, 6)
print(v3)
















