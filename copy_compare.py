print('-------------------------------------------------==和is-------------------------------------------------')

# ==  比较的是：值
# is  比较的是：id

# 例1
a = 1257
b = 1257
print(a == b)

print(id(a))
print(id(b))

print(a is b)  # 只有id相等，才是true

# 例2
# 检查是否为None，使用is，而不是==
a = None
if a is None:
    print('a是None')
if a is not None:
    print('a不是None')

# 例3  元组嵌套列表，id(t1) != id(t2)
t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print(id(t1))
print(id(t2))
print(t1 == t2)
print(t1 is t2)  # false

t1[2].append(5)

print(t1 == t2)
print(t1 is t2)  # false

print('-----------------------------------------------总结---------------------------------------------')

# 浅拷贝中的元素，是原对象中子对象的引用，如果原对象中的元素是可变的，改变其也会影响拷贝后的对象，存在副作用
# 深度拷贝则会递归地拷贝原对象中的每一个子对象，因此拷贝后的对象和原对象互不相关。

print('-------------------------------------浅拷贝----shallow copy---------------------------------------')

# 方式1：使用数据类型本身的构造器（其实就是工厂函数），完成浅拷贝。
l1 = [1, 2, 3]
l2 = list(l1)    # l2是l1的浅拷贝
print(l1 == l2)
print(l1 is l2)  # false

s1 = set([1, 2, 3])
s2 = set(s1)     # s2是s1的浅拷贝
print(s1 == s2)
print(s1 is s2)  # false

# 方式2：对于可变的序列，使用切片
l1 = [1, 2, 3]
l2 = l1[:]
print(l1 == l2)
print(l1 is l2)  # false

# 方式3：copy.copy
import copy
l1 = [1, 2, 3]
l2 = copy.copy(l1)
print(l1 == l2)
print(l1 is l2)  # false

# 方式4：copy
l1 = [1, 2, 3]
l2 = l1.copy()
print(l1 == l2)
print(l1 is l2)  # false

# 对于元组，使用tupel()、切片，不会创建浅拷贝
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 == t2)
print(t1 is t2)  # true

t1 = (1, 2, 3)
t2 = t1[:]
print(t1 == t2)
print(t1 is t2)  # true

print('------------------------------------------------浅拷贝 案例------------------------------------------')
l1 = [[1, 2], (30, 40)]
l2 = list(l1)
print(t1 == t2)
print(t1 is t2)  # true

l1.append(100)   # 浅拷贝不受影响
l1[0].append(3)  # 浅拷贝受影响

print(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)  # false

l1[1] += (50, 60)  # 浅拷贝不受影响
print(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)  # false

print('------------------------------------------------深拷贝---------------------------------------------')
# 浅拷贝有一些副作用
# 如果想完整的拷贝一个对象，需要使用深拷贝
# 深拷贝之后，两个变量完全独立，没有任何联系
# 深拷贝 copy.deepcopy

l1 = [[1, 2], (30, 40)]
l2 = copy.deepcopy(l1)
print(t1 == t2)
print(t1 is t2)  # true

l1.append(100)   # 深拷贝不受影响
l1[0].append(3)  # 深拷贝不受影响

print(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)  # false

print('--------------------------------------------复制文件的两种方法------------------------------------------')

# 使用shutil.copy
import shutil
shutil.copy('ccc.JPG', './归类练习/eee.JPG')

# 读取，再写入
with open('ccc.JPG', 'rb') as f, open('./归类练习/fff.jpg', 'wb') as f1:
    con = f.read()
    f1.write(con)
