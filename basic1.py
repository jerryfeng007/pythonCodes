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
# 三单引号、三双引号可以写多行
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
# 字符串的索引
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
# 字符串的方法--strip()
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
# 列表的查找（不同于字符串，列表只有count和index，没有find）
list3 = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
print(list3.count(1))
print(list3.index(5))  # 返回索引，如果不存在就会报错
# 列表的排序
list4 = [1, 2, 9, 4, 0]
list4.sort()  # 升序
# list4.sort(reverse=True)  # 降序
print(list4)
list5 = [1, 2, 'a', 'b']
list5.reverse()  # 反转
print(list5)
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
'''
字符串是有序的，不可修改的
列表是有序的，可修改的
元组是有序的，不可修改的
字典是无序的，可修改的

总结：
只有字典是无序的
因为字典无序，所以没有索引
数字、字符串、元组不可修改，列表、字典可修改

字典的特点：
因为字典是无序的，所以字典没有索引值
因为字典没有索引值，所以字典以键取值
因为字典以键取值，所以字典的键唯一且不可修改
因为字典的键不可修改，所以列表和字典不可以给字典做键
'''
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
# 可以把keys和values转化为列表，然后for循环去遍历
keys = list(dict1.keys())
values = list(dict1.values())
print(keys)
print(values)
for key in keys:
    print(key, dict1[key])

# 字典的取值
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])      # 取不到时，会报错
print(dict1.get('d'))  # 取不到时，不会报错
# 字典的方法
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict1.update({'a': 1})
print(dict1)
dict1.update({'a': 11})
print(dict1)
dict1.update({'x': 1})  # 不存在x键，会创建一个
print(dict1)
# update方法一般做什么用呢？----拼接
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4}
dict1.update(dict2)
print(dict1)


