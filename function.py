print('-----------------------------函数分类、形参、实参------------------------------------------')

# 函数分类：
# 内置函数(比如sorted()、len()、enumerate())
# 三方函数
# 自定义函数


# 形参、实参
def aaa(n):  # 形参
    print(n)


aaa(5)  # 实参

print('---------------------------------------------------简单的函数------------------------------------------')

# 给一个列表，计算他的最大值
# 方法1


def get_max(l):
    if not isinstance(l, list):
        print('传入的不是列表')
        return
    if len(l) == 0:
        print('列表长度为0')
        return

    l.sort()
    print('最大值为：', l[-1])


get_max([1, 0, 5, -3])

# 方法2


def get_max(l):
    if not isinstance(l, list):
        print('传入的不是列表')
        return
    if len(l) == 0:
        print('列表长度为0')
        return
    large = l[0]
    for i in l:
        if i > large:
            large = i
    print('最大值为：', large)


get_max([1, 0, 5, -3])

print('---------------------------------------------------函数的返回值------------------------------------------')


# 例1
def a1(aa, bb):
    return aa + bb


c = a1(1, 2)
print(c)


# 例2
# 返回一个函数
def a2(aa, bb):
    def a3():
        return aa + bb
    return a3()


c1 = a2(2, 2)
print(c1)


# 例3
# 返回一个函数对象
def a4(aa, bb):
    def a5():
        return aa + bb

    def a6():
        return aa - bb

    if aa > bb:
        return a5
    else:
        return a6


c2 = a4(3, 4)
c3 = c2()
print(c3)

print('---------------------------------------------------参数传递------------------------------------------')

# 形参和实参一一对应传递


def aaa(m, n):  # 传过来的5给m, 6给n
    print(m, n)


aaa(5, 6)

# 关键字参数


def aaa(m, n):
    print(m, n)


aaa(n=5, m=6)  # 可以不用按照顺序来


# 缺省参数
def aaa(a, b=5):  # 如果不传这个参数，默认为5； b=5这种形式必须要写在所有非缺省参数的后面
    print(a, b)


aaa(1)
aaa(1, 3)

print('---------------------------------------------------不定长参数------------------------------------------')
# 场景：
# 如果函数体中，需要处理的数据，不确定长度，那么可以以不定长参数的方式接收数据


# 方式1：
# 一个*，代表元组
# 为啥不以列表的形式传递? 涉及到列表和元组的区别
def aaa(*t):  # 一个*，表示以元组的形式接收参数
    print(t)  # t是一个元组（没有拆包）


aaa(1)
aaa(1, 2, 3)


# 方式2：
# 两个*，代表字典
def bbb(**m):  # 两个*，表示以字典的形式接收参数
    print(m)   # m是一个字典（没有拆包）


bbb(age=2, name='jerry')  # 注意：这里必须以关键字参数传递

print('---------------------------------------------------装包和拆包------------------------------------------')
# 装包：把传递的参数包装成一个集合，使用 *args， **kwargs
# 拆包：把集合参数，再次分解成单独的个体
# 怎么装的就怎么拆，还是使用 *args， **kwargs


# 参数的装包和拆包1
def mysum(a, b, c, d):
    print(a + b + c + d)


def aaa(*args):
    print(args)   # args是一个元组

    # 拆包
    print(*args)  # 分解成了单独的个体

    # 调用mysum函数
    mysum(*args)  # 如果传args会报错，因为没有解包


aaa(1, 2, 3, 4)


# 参数的装包和拆包2
def myccc(y, z):  # 参数必须是y和z，跟bbb(y='male', z='jerry')保持一致，否则报错
    print(y)
    print(z)


def bbb(**kwargs):
    print(kwargs)   # args是一个字典

    # 拆包
    # print(**kwargs)  # 直接打印会报错，但是可以去用
    myccc(**kwargs)  # 拆包之后为：y='male', z='jerry'，所以myccc的参数也必须是y和z，否则报错


bbb(y='male', z='jerry')

print('---------------------------------------------------匿名函数------------------------------------------')
# 跟普通函数的区别
# 匿名函数是一个表达式，不是一个语句，并且是单行的，不能扩展成多行
# 用途-->可以用作某些函数的参数，比如sorted()函数中key的值
# 使用场景：程序中需要使用一个函数完成一个简单的功能，并且该函数只调用一次

# lambda 参数1, 参数2... : 表达式

# 例1
ss = lambda x, y: x + y
print(ss(1, 2))

# 例2 --- 用在列表内部
l = [(lambda x: x*2)(x) for x in [1, 2, 3]]
print(l)

# 例3
d = {'name': 'jerry', 'age': 'small', 'sex': 'male'}
print(sorted(d.items(), key=lambda x: x[0]))  # 按照key排序
print(sorted(d.items(), key=lambda x: x[1], reverse=True))  # 按照value排序

# 例4
d = [{'name': 'hello', 'age': 10}, {'name': 'tom', 'age': 20}, {'name': 'jack', 'age': 0}]
print(sorted(d, key=lambda x: x['name']))
print(sorted(d, key=lambda x: x['age'], reverse=True))

# 例5
l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort()
print(l)  # 默认按照key排序

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
print(sorted(l))  # 默认按照key排序

# 使用lambda
l = [(1, 20), (3, 0), (9, 10), (2, -1)]
l.sort(key=lambda x: x[1], reverse=True)
print(l)

l = [(1, 20), (3, 0), (9, 10), (2, -1)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=lambda x: x[1], reverse=True))

print('------------------------------------------匿名函数与列表推导式------------------------------------------')

# 案例：对列表中的所有元素做平方
l = [1, 2, 3, 4]

# 使用匿名函数
l1 = [(lambda x: x**2)(x) for x in l]
print(l1)

# 使用匿名函数 + map
l2 = list(map(lambda x: x**2, l))
print(l2)

# 使用列表推导式
l3 = [x**2 for x in l]
print(l3)

# 可以看出，使用列表推导式更简单

print('---------------------------------------------------函数嵌套------------------------------------------')

# 函数嵌套的好处：
# 1，一定程度上保证了内层函数的隐私，比如把数据库的用户名密码封装在内层，只有外层函数能调用，避免暴露在全局作用域
# 2，函数开头需要做一些额外工作，而又需要多次调用这个函数，
#    那么将这些额外代码放在外部函数，就可以减少多次调用带来的不必要的开销

# 例1


def a():
    print('hello')

    def b():
        print('world')
    b()


a()


# 例2：递归求一个数的阶乘
# 使用嵌套函数，避免了每次递归都要校验数据的合法性
def get_jie(n):
    if not isinstance(n, int):
        raise Exception('输入必须为整数')
    if n <= 0:
        raise Exception('输入的必须大于0')

    def inner_jie(n):
        if n == 1:
            return 1
        return n * inner_jie(n - 1)
    return inner_jie(n)


a = get_jie(5)
print('阶乘为：', a)


# 如果不使用嵌套函数
# 每次递归都需要判断n是否符合条件，效率低
def get_jie(n):
    if not isinstance(n, int):
        raise Exception('输入必须为整数')
    if n <= 0:
        raise Exception('输入的必须大于0')
    if n == 1:
        return 1
    return n * get_jie(n - 1)


print('---------------------------------------------------值传递、引用传递------------------------------------------')
# 值传递
# 传递过来的，是一个数据的副本
# 修改副本，不会对原值产生影响

# 引用传递
# 传递过来的，是一个变量的地址
# 通过地址，可以操作同一份原件

# 在python中，没得选，是对象的引用传递（地址传递）。但是：
# 如果数据类型是可变的，那么可以改变原件
# 如果数据类型是不可变，那么不可改变原件


# 例1：
def a(n):
    print(id(n))  # 两个地址是一样的，说明是引用传递（地址传递）
    print(n)


n = 10
print(id(n))
a(n)


# 例2：
def b(n):
    print(id(n))  # 两个地址是一样的，说明是引用传递（地址传递）
    n = 12
    print(id(n))  # 这里就不一样了，因为n是不可变的，所以只能开辟一块新的内存区域
    print('函数内部的局部变量应该为12', n)


n = 11
print(id(n))
b(n)
print('n最初是11，现在还应该是11', n)


# 例3：
def c(n):
    print(id(n))  # 两个地址是一样的，说明是引用传递（地址传递）
    n.append(4)
    print(id(n))  # 这里仍然一样，因为n是可变的，所以还是原来的地址，并没有开辟一个新区域
    print('n应该为[1,2,3,4]', n)


n = [1, 2, 3]
print(id(n))
c(n)
print('n最初为[1,2,3],现在应该为[1,2,3,4]', n)


# 例4：
# 在例2中，n最初为11，到最后还是11，那么怎样让他改变呢
def b(n):
    print(id(n))  # 两个地址是一样的，说明是引用传递（地址传递）
    n = 12
    print(id(n))  # 这里就不一样了，因为n是不可变的，所以只能开辟一块新的内存区域
    print('函数内部的局部变量应该为12', n)
    return n


n = 11
print(id(n))
n = b(n)
print('n最初是11，现在接收函数返回值，应该是12了', n)
print('n的新地址', id(n))


# 例5：
# 跟例3有区别
def c(n):
    print(id(n))  # 两个地址是一样的，说明是引用传递（地址传递）
    n = n + [4]
    print(id(n))  # 这里就不一样了，开辟了一个新区域为这个局部变量，但外面的还是不变
    print('局部变量n应该为[1,2,3,4]', n)


n = [1, 2, 3]
print(id(n))
c(n)
print('n最初为[1,2,3],现在还是[1,2,3]', n)  # 如果想要外面的也改变，那么只要函数return就可以了

print('---------------------------------------------------总结--------------------------------------')
# 如果想通过一个函数来修改某个变量的值，有两种方法：
# 一，直接将可变数据类型（列表、字典、集合）当作参数传入，直接在其上修改
# 二，第二则是创建一个新变量，保存修改后的值，然后return给原变量
# 第二种工作中更常用

print('---------------------------------------------------函数变量的作用域------------------------------------------')
# 局部变量：在函数内部定义，只在函数内部有效，外部无法访问
# 全局变量：在文件内的任何地方可以被访问，包括函数内部

# 作用范围：local --->内嵌空间（嵌套函数）---> global--->内建空间
# 如果是全局变量，查找顺序为 global--->内建空间
# 如果是局部变量，查找顺序为 local --->内嵌空间（嵌套函数）---> global--->内建空间

# 函数内部可以访问全局变量，但不能随便更改全局变量的值

# 如果需要修改：
# 对于可变类型的，可以直接在函数内修改，
# 对于不可变类型，需要加：global（如果是嵌套函数，需要在内层函数加：nonlocal）

# 如果函数内部局部变量和全局变量同名，那么在函数内部，局部变量会覆盖全局变量

# 例1
a = 5


def aa():
    a = 6


aa()
print(a)

# 例2
a = 5


def aa():
    global a  # 添加global，就说明这里的a是函数外的全局变量
    a = 6


aa()
print(a)

# 例3
a = [1, 2]


def aa():
    a.append(3)


aa()
print(a)


# 例4

def aaa():
    x = 'local'

    def bbb():
        nonlocal x  # 嵌套函数，添加nonlocal，才能修改外层函数的变量
        x = 'nonlocal'
        print('内部x:', x)
    bbb()
    print('外部x:', x)


aaa()


# 例5

def fff():
    x = [1, 2, 3]

    def eee():
        nonlocal x
        x.append(4)  # 如果是可变类型，无需加nonlocal，但也可以加
        print('内部x:', x)
    eee()
    print('外部x:', x)


fff()