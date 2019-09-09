"""
装饰器 decorator

作用
在函数名和函数体不改变的前提下，给一个函数附加一些额外代码，从而使其增加一些额外的功能

要点：
不改变原函数---业务逻辑、功能函数的函数名、函数体的代码都不改变
额外-----------在原函数功能的基础上，再增加一些功能

使用场景
比如，去一个新公司，原来有代码，现在要实现新功能，
那么尽量不要去修改原来的业务逻辑代码、功能函数代码（函数名、函数体都不能修改）
而是新增一些函数等，使用装饰器特性，达到目的

使用场景2
日志-----------
缓存-----------
身份认证-------

装饰器的执行时间
立即执行，写完@之后就执行 func = login(func)，不是等函数调用的时候才执行

功能函数、业务逻辑，要分开来写
有三个好处：
1.业务逻辑比较清晰
2.代码可以复用
3.代码易于维护

开放封闭原则：
已经写好的代码，尽可能不要修改
如果想要新增功能，在原先代码的基础上，单独进行扩展

单一职责：
一个函数尽可能实现单一的功能，从函数名就可以看出来
"""

print('------------------------------------------------------------简单的装饰器')


def check_login(func):
    def inner():
        print('验证登陆。。。')
        func()
    return inner


# 功能函数1
@check_login  # 等同于 fss = checklogin(fss)   @（语法糖）
def fss():
    print('发说说')


# 功能函数2
@check_login  # 等同于 ftp = checklogin(ftp)
def ftp():
    print('发图片')


# 业务代码
index = 2
if index == 1:
    fss()
else:
    ftp()

print('------------------------------------------------------------装饰器叠加')
# 从上到下装饰，从下到上执行


def line(func):
    def inner():
        print('-' * 30)
        func()
    return inner


def star(func):
    def inner():
        print('*' * 30)
        func()
    return inner


@star
@line
def fss():
    print('发说说')


fss()

print('------------------------------------------------------------对有参数的函数进行装饰')
# 保证函数调用参数个数一致
# 为了通用（因为不同函数参数个数不一致），使用不定长参数，结合拆包操作进行处理


def hello(func):
    def inner(*args, **kwargs):  # 不定长参数
        print('哈哈哈')
        func(*args, **kwargs)  # 拆包
    return inner


@hello
def fss(num, num1):
    print('发说说', num, num1)


@hello
def ftp(num):
    print('发说说', num)


fss(123, num1=456)
ftp(222)

print('------------------------------------------------------------对有返回值的函数进行装饰')
# 保证函数返回值一致


def hello(func):
    def inner(*args, **kwargs):
        print('哈哈哈')
        res = func(*args, **kwargs)
        return res
    return inner


@hello
def fss():
    num = 1
    num1 = {'name': 'jerry', 'age': 20}
    return num, num1


@hello
def ftp():
    num = [1, 2, 3]
    return num


db, dc = fss()
print(db, dc)

dd = ftp()
print(dd)

print('------------------------------------------------------------带有参数的装饰器')


def ccc(char):
    def bbb(func):
        def inner(*args, **kwargs):
            print(char * 30)
            res = func(*args, **kwargs)
            return res
        return inner
    return bbb  # 这个函数的作用就是返回一个装饰器


@ccc('*')
def aaa():
    print('666')


aaa()

print('-------------------------------------------------------------------------总结')


# 不带参数的装饰器，下面的函数比较通用
def hello(func):
    def wrapper(*args, **kwargs):
        print('哈哈哈')
        res = func(*args, **kwargs)
        return res
    return wrapper


# 带参数的装饰器，下面的函数比较通用
def ccc(char):
    def bbb(func):
        def wrapper(*args, **kwargs):
            print(char * 30)
            res = func(*args, **kwargs)
            return res
        return wrapper
    return bbb


print('------------------------------------------------------------例1，只有登陆才能评论')


def login():
    flag = 1
    if flag == 1:
        return True
    else:
        return False


def zsq(func):
    def inner(*args, **kwargs):
        if login():
            func(*args, **kwargs)
        else:
            print('请先登陆才能发评论')
    return inner


@zsq
def post_comments():
    print('这是发评论函数')


post_comments()

print('------------------------------------------------------------例2，日志记录')
# 如果怀疑某些函数的耗时过长，导致整个系统的延迟增加，想在线上测试某些函数的执行时间

import time


def func_time(func):
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        t = (end - start) * 1000
        print('{}耗时{}ms'.format(func.__name__, t))
    return inner


@func_time
def func1():
    print('这是第一个函数')


@func_time
def func2():
    print('这是第二个函数')
    print('这是第二个函数')


func1()
func2()

print('------------------------------------------------------------例3，输入合理性检查')

# 不使用装饰器

# 一定要注意，每个函数只处理一个功能，这样比较简单，逻辑也比较清晰


def fcy(a, b):  # 这个函数只负责把传递过来的两个数进行求和
    print(a + b)


def check(a, b):  # 这个函数只负责把传递过来的两个数进行校验
    if a.isdigit() and b.isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        a = input('输入第一个数：')
        b = input('输入第二个数：')
        if check(a, b):
            fcy(int(a), int(b))
            break
        else:
            print('输入的不是数字，请重新输入')
            continue

# 使用装饰器

# 注意这里有个传参数的难点
# 注意这里有个传参数的难点
# 注意这里有个传参数的难点


def check(a, b):
    if a.isdigit() and b.isdigit():
        return True
    else:
        return False


def decorator(func):
    def wrapper(*args, **kwargs):
        if check(args[0], args[1]):  # 这里的参数来源是个难点,一定要注意这里啊
            func(*args, **kwargs)
        else:
            print('输入不合法')
    return wrapper


@decorator
def run(a, b):
    a = int(a)
    b = int(b)
    print(a + b)


a = input('第一个数：')
b = input('第二个数：')
run(a, b)

print('------------------------------------------------------------例4，缓存')
# 缓存装饰器，使用 lru_cache
# lru_cache会删除最久的没有访问的内容

# from functools import lru_cache
#
#
# @lru_cache
# def check_device(param1, param2):
#     print('大型公司服务端的代码，检查设备是什么型号的函数，因为某些feature只在某些设备上有')

print('-------------------------------------------------------------------------------------------类装饰器')


def verify():
    user = 'jerry'
    pwd = 123
    if user == 'jerry' and pwd == 123:
        return True
    else:
        return False


class Check:
    def __init__(self, func):  # 注意的第一点，在初始化方法里保存该函数
        self.func = func

    def __call__(self, *args, **kwargs):  # 注意的第二点，在call方法里执行该函数
        if not verify():
            raise Exception('错误了')
        print('验证成功！')
        m = self.func(*args, **kwargs)  # 在调用该函数之前， 可以增加别的功能
        return m


@Check  # 等价于 fss = check(fss)
def fashuoshuo(hello):  # 带参数
    m = 5
    print(hello)
    print('发说说')
    return m  # 有返回值


m = fashuoshuo('hello')
print(m)

print('-------------------------------------函数被装饰之后，元信息变了-----------------------------------------------')

# 函数被装饰以后，他的元信息变了，被内部函数取代了
# 通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


print(greet.__name__)
