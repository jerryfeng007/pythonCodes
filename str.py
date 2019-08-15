print('-----------------单引号、双引号、三单引号、三双引号---没有区别------------------------------------')

# 单行
s1 = 'i love u'
s2 = "i love u"

# 多行
s3 = '''
i love u
Do u love me?
'''

s4 = """
i love u
i love him!
"""

# 引号嵌套
s5 = "i'm a teacher"
s6 = 'the "name" is jerry'
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

print('------------------------------------------------多行注释---------------------------------------')

'''
a = 'hello'
b = ' world'
c = a + b
print(c)
'''

"""
a = 'hello'
b = ' world'
c = a + b
print(c)
"""

print('------------------------------------------------字符串拼接-------------------------------------')

# +
a = 'hello'
b = ' world'
c = a + b
print(c)

# +=            ---不用担心效率问题
s = '12'
print(id(s))
s1 = '34'
s += s1
print(s)
print(id(s))

# ''.join()
l = ['a', 'b', 'c', 'd']
s = '_'.join(l)
print(s)

print('------------------------------------------------字符串中的特殊字符-------------------------------------')

# \n 换行
# \r 回车
# \t tab
print('i\nlove\nu')

# 在特殊字符前加\，会把特殊字符转义掉
print('i\\nlove\\nu')

print('------------------------------------------------字符串格式化-------------------------------------')

name = 'tom'
age = 18
height = 1.85

# %s(字符型) %d(整型) %f(浮点型) %.2f(保留2位小数)
print('%s is %d years old' % (name, age))
print('身高为%f，保留2位小数是%.2f' % (height, height))

# {}.format()
print('{} is {} years old'.format(name, age))

# f'{}'
print(f'{name} is {age} years old')

print('------------------------------------------------字符串的索引-------------------------------------')

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

print('------------------------------------------------字符串的方法-------------------------------------')

# strip()  strip(str)
# 默认去除两边的空格，去除内容可以指定。另外有 lstrip()、rstrip()

# 场景1
# s1 = input('请输入一个数字：').strip()
# print(s1)

# 场景2
s12 = '   hello   '
s12 = s12 .strip()
print(s12)

# 分割
path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]
print(namespace)

s = 'hello world jerry'
s1 = s.split(' ', 1)  # 只分割1次
print('s1=', s1)

# 查找
# find 和 index功能类似，都是返回要找的字符的索引
# 区别是如果找不到时，find返回-1，index会报错

# find(sub, start, end)  另外有 rfind()
s3 = 'hello'
print(s3.find('o'))
print(s3.find('p'))
print(s3.find('ll', 1, 4))

# index(sub, start, end) 另外有 rindex()
print(s3.index('o'))

# 统计
print(s3.count('l'))

# 长度
s = 'jerry'
print(len(s))

# 替换
s4 = s3.replace('l', 'L')
print(s4)

# 大小写
s1 = 'heLLo'
if s1.lower() == 'hello':
    print('登录成功')
if s1.upper() == 'HELLO':
    print('登录成功')

print('------------------------------------------------字符串的判断-------------------------------------')

# 判断
s = 'helloworld123'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())  # 或字母、或数字
print(s.islower())
print(s.isupper())
print(s.startswith('h'))
print(s.endswith('d'))
print(s.isspace())

# in not in
print('w' in s)

print('------------------------------------------------字符串编码-------------------------------------')

# ASCII码
print(ord('A'))
print(chr(65))

# 编码
s = '马云非'
s1 = s.encode('gbk')
s2 = s.encode('utf8')
print(s1)
print(s2)

# 解码
s3 = s1.decode('gbk')
s4 = s2.decode('utf8')
print(s3)
print(s4)

print('--------------------------------------------input函数输入的都为字符串-------------------------------------')

# input函数输入的任何内容，都当做字符串
# num = input('请输入一个数：')
# print(type(num))  # str类型

print('------------------------------------------------str()强制转换函数---------------------------------------')

# 把其他类型转为字符串
a = 20
a = str(a)
print(type(a))

print('------------------------------------------------字符串是不可变类型---------------------------------------')
s1 = 'abcde'
print(id(s1))
# 如果想要改变s1，比如变为 'abcdef'
# 那么需要重新开辟一块内存存储
s1 = 'abcdef'
print(id(s1))  # id 变了
