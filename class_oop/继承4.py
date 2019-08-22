print('--------------------------------构造函数的调用顺序---------------------------------------------')


# super,可以召唤父类的构造方法,来保证一个类只会被初始化一次
# 如果不使用super,而使用类名来调用,那么对于菱形继承(有重叠多继承链)来说,可能会出现基类的初始化函数被调用2次
# python3中,可以直接写super(),不用添加里面的参数,super会根据上下文自动检测
# super不要和类名调用混着用

print('---------------------------------单继承链---不使用super----------------------------------------')


class A:
    def __init__(self):
        print('A的构造')


class B(A):
    def __init__(self):
        print('B的构造')
        A.__init__(self)


class C(B):
    def __init__(self):
        print('C的构造')
        B.__init__(self)


c = C()

print('---------------------------------单继承链---使用super---------------------------------------------------')


class A:
    def __init__(self):
        print('A的构造')


class B(A):
    def __init__(self):
        print('B的构造')
        super().__init__()


class C(B):
    def __init__(self):
        print('C的构造')
        super().__init__()


c1 = C()

print('---------------------------------无重叠多继承链---不使用super---------------------------------------------------')


class A:
    def __init__(self):
        print('A的构造')


class B:
    def __init__(self):
        print('B的构造')


class C(A):
    def __init__(self):
        print('C的构造')
        A.__init__(self)


class D(B):
    def __init__(self):
        print('D的构造')
        B.__init__(self)


class E(C, D):
    def __init__(self):
        print('E的构造')
        C.__init__(self)
        D.__init__(self)


e = E()

print('---------------------------------无重叠多继承链---使用super---------------------------------------------------')


class A:
    def __init__(self):
        print('A的构造')


class B:
    def __init__(self):
        print('B的构造')


class C(A):
    def __init__(self):
        print('C的构造')
        super().__init__()


class D(B):
    def __init__(self):
        print('D的构造')
        super().__init__()


class E(C, D):
    def __init__(self):
        print('E的构造')
        super().__init__()  # 为啥只走左边一条线 ??????????????????????????????????????


e1 = E()


print('----------------------------菱形继承---有重叠多继承链---不使用super---------------------------------------------------')

# D->B->A-C->A    不使用super的情况下,A被调用了2次


class A:
    def __init__(self):
        print('A的构造')


class B(A):
    def __init__(self):
        print('B的构造')
        A.__init__(self)


class C(A):
    def __init__(self):
        print('C的构造')
        A.__init__(self)


class D(B, C):
    def __init__(self):
        print('D的构造')
        B.__init__(self)
        C.__init__(self)


d = D()

print('----------------------------菱形继承---有重叠多继承链---使用super---------------------------------------------------')

# D->B->C->A    使用了super,避免了重复调用


class A:
    def __init__(self):
        print('A的构造')


class B(A):
    def __init__(self):
        print('B的构造')
        super().__init__()


class C(A):
    def __init__(self):
        print('C的构造')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D的构造')
        super().__init__()


d1 = D()
