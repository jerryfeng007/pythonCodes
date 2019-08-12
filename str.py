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
