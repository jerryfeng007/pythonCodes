print('---------------------------------单继承链----------------------------------------------------')
'''
A
B   B继承A
C   C继承B
'''
# 查找顺序: C->B->A
# 调用的时候,如果C中没有找到某个属性或方法,那么先去父类B中找,如果B中没有,再去爷类A中找,如果再找不到,就报错


class A:
    name = 'a'
    pass


class B(A):
    # name = 'b'
    pass


class C(B):
    # name = 'c'
    pass


c = C()
print(c.name)

print('---------------------------------无重叠多继承链-----------------------------------------------------')
'''
A B
C D  C继承A,D继承B
 E   E继承C和D
'''
# 查找顺序: E->C->A->D->B
# 调用的时候,如果E中没有找到某个属性或方法
# 先去父类C中找,如果C中没有,再去爷类A中找,如果没有,再去父类D中找,如果没有,再去爷类B中找,如果找不到,就报错


class A:
    # age = 'a'
    pass


class B:
    age = 'b'
    pass


class C(A):
    # age = 'c'
    pass


class D(B):
    # age = 'd'
    pass


class E(C, D):
    # age = 'e'
    pass


e = E()
print(e.age)

print('---------------------------------有重叠多继承链-----------------------------------------------------')
'''
 A
B C  B继承A,C继承A
 D   D继承B和C
'''
# 查找顺序: D->B->C->A
# 调用的时候,如果D中没有找到某个属性或方法
# 先去父类B中找,如果没有,再去父类C中找,如果没有,再去爷类A中找,如果找不到,就报错


class A:
    age = 'a'
    pass


class B(A):
    # age = 'b'
    pass


class C(A):
    # age = 'c'
    pass


class D(B, C):
    # age = 'd'
    pass


d = D()
print(d.age)
