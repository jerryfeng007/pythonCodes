# 1.字符串反转
s = 'HelloWorld'
print(s[::-1])

# 2.列表反转
list1 = [1, 2, 3, 2, 5, 4]
# 方法1：
print(list1[::-1])
# 方法2：
list1.reverse()
print(list1)

# 3.元组的反转
tuple1 = (1, 2, 1, 4, 3)
# 方法1
print(tuple1[::-1])
# 方法2
s = ''
for s1 in tuple1:
    s = str(s1) + s
    print(s)

# 4.删除列表中所有的1
# 方法1：这个方法的坏处，是把所有的元素都去重了，所以结果可能不正确
L = [1, 2, 3, 1, 3, 1, 5, 1]
s = set(L)    # 去重（备注：set()是集合，不允许重复的值）
L = list(s)   # 把集合转变为列表
L.remove(1)
print(L)

# 方法2：靠谱
L1 = [1, 2, 3, 1, 3, 1, 5, 1]
while True:
    try:
        L1.remove(1)
    except Exception as e:
        print(L1)
        break

# 方法3：靠谱
L2 = [1, 2, 3, 1, 3, 1, 5, 1]
L2.sort()
while True:
    if L2[0] == 1:
        L2.remove(1)
    else:
        print(L2)
        break
# 5.对调两个变量的值
a = 10
b = 20
a, b = b, a   # 序列解包赋值
print(a, b)

# 6.闰年
'''
普通闰年：能被4整除，但不能被100整除的年份（如2004是闰年，1999不是闰年）
世纪闰年：能被400整除的为世纪闰年（如2000年是闰年，1900年不是）
'''
# year = input('请输入一个年份：').strip()
# year = int(year)
# if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#     print(f'{year}年是闰年')
# else:
#     print(f'{year}年不是闰年')

# 7.九九乘法表
'''
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9  
'''

'''
# 1x3=3 2x3=6 3x3=9  以这一行为例
j = 3  # 先写死
for i in range(1, 4):
    print(f'{i}x{j}={i*j}', end=' ')
'''

# 再上面的基础上，把j变活，j的取值范围是1-9
for j in range(1, 10):
    for i in range(1, j+1):
        print(f'{i}x{j}={i*j}', end=' ')
    print()  # 换行

# 8.打印以下：
# *
# **
# ***
# ****
# *****
# n = int(input('请输入你想要的数字：').strip())
# i = 1
# while i <= n:
#     print('*' * i)
#     i += 1

# 9.练习
# 取到1/4/7
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = [i[0] for i in l]
print(l1)

# 取到1/5/9
l2 = [l[i][i] for i in range(len(l))]
print(l2)

# 10.计算圆的周长和面积
# 初级版
# r = float(input('请输入圆的半径：'))  # 这里可以用int、float、eval
# if r > 0:
#     zhouchang = 2 * 3.1415926 * r
#     area = 3.1415926 * r ** 2
#     print('圆的周长为：%.2f' % zhouchang)
#     print('圆的面积为：%.2f' % area)
# else:
#     print('半径不能为负数或者0')

# 升级版---解决输入非数字报错的问题
# while True:
#     try:
#         r = float(input('请输入圆的半径：'))  # 这里可以用int、float、eval
#         if r > 0:
#             zhouchang = 2 * 3.1415926 * r
#             area = 3.1415926 * r ** 2
#             print('圆的周长为：%.2f' % zhouchang)
#             print('圆的面积为：%.2f' % area)
#             break
#         else:
#             print('半径不能为负数或者0')
#     except Exception as e:
#         print('输入必须为整数或者小数')

# 11.输入两个数，求和
# num1 = int(input('输入第一个数：'))
# num2 = int(input('输入第二个数：'))
# print('他们的和为：', num1 + num2)

# 升级版，在一行输入这两个数
num1, num2 = eval(input('请输入两个数，以英文逗号分割：'))
print(num1 + num2)
'''
以上使用了eval()函数，括号里必须为字符串，它把字符串转化为别的（去掉字符串两边的引号）
'''




