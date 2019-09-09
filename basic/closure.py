"""
闭包
在函数嵌套的前提下，
内层函数引用了外层函数的变量(包括参数)，
外层函数又把内层函数当作返回值进行返回
这个内层函数+所引用的外层变量，称为闭包

# 闭包与普通函数嵌套的区别
闭包，返回的是一个函数，不是函数执行后的值
返回的函数通常赋予一个变量，后面可以继续被执行调用

# 使用闭包的好处：
和嵌套函数类似，如果开始需要做一些校验之类的额外工作，然后又需要多次调用函数，
那么就可以把这额额外的处理放到外部函数，减少多次调用带来的不必要的开销

# 装饰器也是基于闭包的一种应用场景

# 闭包，使得局部变量在函数外被访问成为可能

# 如下的例子中，cc就是一个闭包
闭包本质上是一个函数，它有两部分组成，bbb函数和变量a
闭包使得这些变量的值始终保存在内存中
"""
print('-------------------------------------------------------------简单的闭包------------------------------')


def aaa(name):
    a = 5

    def bbb():
        print(a, name)
    return bbb


cc = aaa('jerry')
cc()

print('-------------------------------------------------------------案例1-----------------------------')

# 案例：根据配置信息，生成不同的分割线函数


# 非闭包的写法
def line_config(content, length):
        print('-' * (length // 2) + content + '-' * (length // 2))


line_config('内存', 80)  # 每次都需要传2个参数
line_config('主机', 90)  # 每次都需要传2个参数
line_config('硬盘', 70)  # 每次都需要传2个参数


# 闭包的写法1

def line_config(content, length):
    def line():
        print('-' * (length // 2) + content + '-' * (length // 2))
    return line


line1 = line_config('闭包', 80)
line1()  # 以后不用传参了，直接line1()
line1()
line1()

line2 = line_config('函数', 100)
line2()  # 以后不用传参了，直接line2()
line2()

# 闭包的写法2


def line_config(length):
    def line(content):
        print('-' * (length // 2) + content + '-' * (length // 2))
    return line


line1 = line_config(80)
line1('闭包')  # 以后可以少传一个参数
line1('函数')
line1('类')

line2 = line_config(100)
line2('jerry')
line2('tom')

print('-------------------------------------------------------------案例2----------------------------------')
# 模拟不同颜色的画笔，画出不同的形状

# 不使用闭包


def pen(color, shape):
    print(color, shape)


pen('红色', '三角形')
pen('绿色', '四边形')
pen('白色', '五角形')

# 使用闭包


def pen(color, shape):
    def pen2():
        print(color, shape)
    return pen2


pen2 = pen('红色', '三角形')
pen2()
pen2()

pen3 = pen('白色', '四边形')
pen3()
pen3()

print('-------------------------------------------------------案例3：计算一个数的n次幂---------------------------')
# 不用闭包


def nnn(a1, b1):  # 计算a1的b1次幂
    print(a1 ** b1)


nnn(2, 3)  # 每次都需要传2个参数
nnn(3, 3)
nnn(4, 3)


# 使用闭包1
def nnn(a1, b1):
    def inner():
        print(a1 ** b1)
    return inner


c1 = nnn(5, 3)
c1()  # 以后不用写参数，直接c1()
# 但是感觉意义不大，因为可能需要计算很多数的不同次幂，所以还得改2个参数


# 使用闭包2
def nnn(a1):
    def inner(b1):
        print(a1 ** b1)
    return inner


c1 = nnn(2)
c1(3)  # 2的3次幂
c1(4)  # 2的4次幂
c1(5)  # 2的5次幂

# 这样应该就符合要求了，只需要传一个参数，就能够计算一个数的不同的次幂

c2 = nnn(3)
c2(2)
c2(3)
c2(4)

print('-------------------------------------------------------------修改引用的外部变量--------------------------')

# 闭包中，引用、读取外层的变量是可以的
# 但是如果要修改引用的外层变量，需要使用nonlocal声明，否则当作是闭包内新定义的变量


def a():
    num = 10

    def b():
        nonlocal num  # 闭包使用 nonlocal， 之前的全局变量使用global
        num = 666
        print(num)
    print(num)
    return b


bb = a()
bb()
