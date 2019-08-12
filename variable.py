import keyword

print('----------------------------------------------变量赋值的3种方式--------------------------------------------')

# 传统赋值
name = 'jerry'

# 链式赋值
name1 = name2 = 'tom'

# 序列解包赋值
name3, age = 'jerry', 18

print('----------------------------------------------查看变量的类型--------------------------------------------')

a = '34'
print(type(a))

print('----------------------------------------------查看地址--------------------------------------------')

# 不可变类型，比如str
name4 = 'Tom'
user = 'Tom'
print(id(name4))
print(id(user))
print(name4 == user)
print(name4 is user)

# 可变类型，比如list
# 方式1
list1 = list2 = [1, 2, 3]  # list1和list2的id相等
print(id(list1))
print(id(list2))

# 方式2
list3 = [1, 2, 3]
list4 = [1, 2, 3]          # list1和list2的id不相等
print(id(list3))
print(id(list4))

print('----------------------------------------------is is not--------------------------------------------')

# (a is b) is true only when id(a) == id(b)

print('----------------------------------------------变量的命名--------------------------------------------')

# 推荐命名方法，名字要有意义
student_name_list = ['Tom', 'Jerry', 'Lucy']

# 变量名不要使用关键字
# 关键字列表
print(keyword.kwlist)
