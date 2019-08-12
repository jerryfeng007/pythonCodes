# 变量赋值的3种方式
name = 'jerry'            # 传统赋值
name1 = name2 = 'tom'     # 链式赋值
name3, age = 'jerry', 18  # 序列解包赋值

# 查看变量的类型
a = '34'
print(type(a))

# 查看地址
name4 = user = 'Tom'
print(id(name4))
print(id(user))
print(name4 == user)
print(name4 is user)

# is is not
# 只有当id(a) id(b) 相等的时候， a is b 才是真的

# 推荐命名方法
student_name_list = ['Tom', 'Jerry', 'Lucy']

# 变量名不要使用关键字
# 关键字列表
import keyword
print(keyword.kwlist)
