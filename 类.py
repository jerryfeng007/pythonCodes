'''
-----------------------------------------------面向对象--------------------------------------------------------
代码(code)-->封装成函数(function)--->封装成类(class)--->模块(.py文件)--->包(package)
包和目录的区别：包是package, 目录是directory，包其实也是一个目录，但是多了一个__init__.py文件
包 = n个子包(每个包都有一个__init__.py) + n个模块(.py文件) + __init__.py文件

面向对象(OOP)-----万物皆对象，python是彻底的OOP，所有类型都是对象类型
比如, 1, 0.01, True, [1, 2, 3, 4], {'a':3, 'b':4}  都是对象
他们的类型 int float Bool list dict，都是对象类型

人：属性：(身高、体重、年龄)
    行为：(走路、吃饭、开车)

面向过程和面向对象：
都是一种解决问题的思路（思想）
面向过程，关注的是解决问题的每一个过程（步骤），亲历亲为，比如洗碗：第一步放水，第二步放洗洁精，第三步洗碗
面向对象，关注的是解决问题所需要的对象，比如洗碗：我可以让你洗碗，你又可以使用洗碗机
面向对象本身是对面向过程的封装

面向对象编程最重要的是：按照对象进行功能划分，找到对象，确定对象属性、行为

如何从面向过程过渡到面向对象？
确定每一个步骤之后，把这些步骤划分给不同的对象来处理，再确定每个对象的属性、行为

类：类名+属性+方法
属性和方法是抽象的概念，只有根据类创建的对象（实例），才有具体的属性值和方法实现

对象和类：
根据对象，抽象出类
根据类，实例化多个对象

比如，根据张三这个对象，抽象出不良青年这个类；  属性：身高、年龄；方法：吃、喝、嫖、赌
根据不良青年这个类，创建（实例化）不同的对象，比如张三、李四、王五，他们可以有不同的属性、行为
'''
# class MyStudent:
#     pass
#
# a = MyStudent()  # 创建（实例化）一个对象
# b = MyStudent()  # 创建（实例化）一个对象

print('-------------------------------------实例方法、 类方法、 静态方法-----------------------------------')


class Test:
    age = 10  # 类属性
    sex = 'male'
    name = 'student'

    def __init__(self):
        self.b = 5  # 实例属性

    def eat(self):  # 第一个参数self不用管，实例调用的时候会自动把实例自己传递过来
        print('这是实例方法, self就是实例t', self)

    @classmethod
    def drink(cls):
        print('这是类方法', cls)

    @staticmethod
    def sing():                # 没有默认参数
        print('这是静态方法')


# 调用实例方法  # 只有实例可以调用
t = Test()
t.eat()
print('t就是self', t)


# 调用类方法  # 类、实例，都可以调用
Test.drink()
t.drink()


# 调用静态方法  # 类、实例，都可以调用
Test.sing()
t.sing()


# 调用属性
print(t.age, t.sex, t.name)  # 实例调用
print(Test.age, Test.sex, Test.name)  # 类调用

print('------------------------------------------访问权限------------------------------------------------------')
# 公有属性：类内部、子类内部、模块内其他位置、跨模块， 都可以访问
# 受保护的：类内部、子类内部可以访问；模块内其他位置、跨模块访问时，要么警告，要么报错
# 私有属性：类内部可以被访问，子类内部和其他位置都不可以


class Parent:
    x = 10
    _x = 11   # 受保护的属性
    __x = 12  # 私有属性


print('-----------------------------------面向对象三大特性---封装---继承---多态--------------------------')
# 封装
# 将一些属性和相关方法封装在一个对象中，对外隐藏内部具体的实现细节

# 继承
# 子类可以使用父类资源（非私有的属性和方法）的方式之一
# 单继承、多继承

# 继承多个类  class Dog(Animal, Animals):

# 单继承链：
# 查找顺序：一直向上找

# 无重叠的多继承链：
# 查找顺序：左--左上--右--右上

# 有重叠的多继承链：
# 查找顺序： 左--右--上


class D:
    age = 'd'


class C(D):
    age = 'c'
    pass


class B(D):
    # age = 'b'
    pass


class A(B, C):
    # age = 'a'
    pass


print(A.age)


# 继承
class B():
    a = 1  # 类属性

    def __init__(self):
        self.b = 2      # 实例属性
        print('创建子类的实例时，因为子类没有构造方法，所以会调用父类的构造方法')

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


a_obj = A()      # 创建实例时，会调用构造方法，因为子类没有，所以会调用父类的构造方法
print(A.a)       # 子类没有a, 所以访问父类的类属性
print(a_obj.b)   # 子类没有b，所以访问父类的实例属性
a_obj.t1()
A.t2()
A.t3()

print(A.c)
a_obj.tt1()
A.tt2()
A.tt3()
print(a_obj.e)


# 多态
# 子类可以重写父类的方法，方法名相同，但重写了，内容可以不同
class Animal:
    def jiao(self):
        pass


class Dog(Animal):
    def jiao(self):
        print('汪汪汪')


class Cat(Animal):
    def jiao(self):
        print('喵喵喵')


def test(obj):
    obj.jiao()


d = Dog()
c = Cat()
test(d)
test(c)

# 抽象类（比如Animal）、抽象方法(比如jiao)

print('--------------------------------------------综合案例------------------------------------------')
# 综合1：封装、继承、多态


class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        print('名字为{}年龄为{}的小家伙在吃饭'.format(self.name, self.age))

    def play(self):
        print('名字为{}年龄为{}的猫在吃饭')


class Dog(Animal):
    def __init__(self, name, sex, age=1):
        super().__init__(name, age)
        self.sex = sex

    def play(self):  # 重写父类的play方法
        print('性别为{}年龄为{}的小狗在玩'.format(self.sex, self.age))
        super().eat()

    def watch(self):
        print('名字为{}年龄为{}的小狗在看家'.format(self.name, self.age))


d = Dog('小黑', '母')
d.eat()  # 调用的是父类的方法
d.play()  # 调用的是重写的父类方法
d.watch()  # 调用的是子类的方法


# 复制文件的两种方法：

# 1.使用shutil.copy
# import shutil
# shutil.copy('ccc.JPG', './归类练习/eee.JPG')

# 2.读取，再写入
# with open('ccc.JPG', 'rb') as f, open('./归类练习/fff.jpg', 'wb') as f1:
#     con = f.read()
#     f1.write(con)
