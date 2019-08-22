print('-------------------------------案例--子类没有任何资源,可以使用父类的资源-----------------')


class B:
    a = 1  # 类属性

    def __init__(self):
        self.b = 2      # 实例属性
        print('调用父类的构造方法')

    def t1(self):
        print('t1')

    @classmethod
    def t2(cls):
        print('t2')

    @staticmethod
    def t3():
        print('t3')


class A(B):
    pass


a_obj = A()      # 创建实例时，会调用子类的构造方法，会调用父类的构造方法
print(A.a)       # 子类没有a, 所以访问父类的类属性
print(a_obj.b)   # 子类没有b，所以访问父类的实例属性
a_obj.t1()
A.t2()
A.t3()

print('-------------------------------子类也可以增加自己的资源--------------------------------------')


class B:
    a = 1  # 类属性

    def __init__(self):
        self.b = 2      # 实例属性
        print('调用父类的构造方法')

    def t1(self):
        print('t1')

    @classmethod
    def t2(cls):
        print('t2')

    @staticmethod
    def t3():
        print('t3')


class A(B):
    c = 3   # A 新增的类属性

    def __init__(self):
        print('调用子类的构造方法')
        super().__init__()  # super不是父类，而是MRO链条的下一级节点， 直接写super()就可以，不用传参数
        self.e = 4

    def tt1(self):   # A新增的方法
        print('t1')
        super().t1()  # 在这里调用B的t1方法

    @classmethod
    def tt2(cls):   # A新增的方法
        print('t2')
        super().t2()   # 在这里调用B的t2方法

    @staticmethod
    def tt3():      # A新增的方法
        print('t3')


a_obj = A()      # 创建实例时，会调用子类的构造方法，会调用父类的构造方法
print(A.c)
a_obj.tt1()
A.tt2()
A.tt3()
print(a_obj.e)
