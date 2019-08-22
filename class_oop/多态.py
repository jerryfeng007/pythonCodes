print('-------------------------------------------------------多态----------------------------------------')

# 不同的子类调用父类的同一个方法(方法名相同),但是各子类可以进行重写,去实现不同的内容
# 比如,Animal类,有个方法jiao,但是狗类和猫类继承之后,再进行重写,因为狗和猫叫声不一样


class Animal:
    def jiao(self):
        raise Exception('此方法未实现，子类需要重写这个方法')


class Dog(Animal):
    def jiao(self):
        print('汪汪汪')


class Cat(Animal):
    def jiao(self):
        print('喵喵喵')


# 这个写法不错
def test(obj):
    obj.jiao()


d = Dog()
c = Cat()
test(d)
test(c)

print('-------------------------综合案例-----封装、继承、多态----------------------------------------')


class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        print('名字为{}年龄为{}的小家伙在吃饭'.format(self.name, self.age))

    def play(self):
        raise Exception('方法未实现，需要子类重写')


class Dog(Animal):
    def __init__(self, name, sex, age=1):
        super().__init__(name, age)
        self.sex = sex

    # 重写父类的play方法
    def play(self):
        print('性别为{}年龄为{}的小狗在玩'.format(self.sex, self.age))
        super().eat()

    def watch(self):
        print('名字为{}年龄为{}的小狗在看家'.format(self.name, self.age))


d = Dog('小黑', '母')
d.eat()  # 调用的是父类的方法
d.play()  # 调用的是子类重写的父类方法
d.watch()  # 调用的是子类的方法
