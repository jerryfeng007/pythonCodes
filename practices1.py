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
# num1, num2 = eval(input('请输入两个数，以英文逗号分割：'))
# print(num1 + num2)
'''
以上使用了eval()函数，括号里必须为字符串，它把字符串转化为别的（去掉字符串两边的引号）
'''

# 12.输入一个三位数，然后输出每个位置的数字（比如输入719，显示：百位数字：7，十位数字：1，个位数字：9）
# num = input('请输入一个三位数：')
# if num.isdigit():
#     if len(num) == 3:
#         num = int(num)
#         print(f'百位数字是：{num//100}，十位数字是：{num%100//10}，个位数字是：{num%10}')
#     else:
#         print('输入的不是三位数！')
# else:
#     print('输入必须为数字！')

# 方法2
# num = input('请输入一个三位数：')
# if num.isdigit():
#     if len(num) == 3:
#         print(f'百位数字是：{num[0]}，十位数字是：{num[1]}，个位数字是：{num[2]}')
#     else:
#         print('输入的不是三位数！')
# else:
#     print('输入必须为数字！')

# 13.编程实现145893秒是几天几小时几分几秒
total_seconds = 145893
day = int(total_seconds/60/60//24)
hour = total_seconds//3600-day * 24
min = total_seconds//60 - hour * 60 - day * 24 * 60
sec = total_seconds - day * 24 * 3600 - hour * 3600 - min * 60
print(f'{total_seconds}秒是{day}天{hour}小时{min}分{sec}秒')

# 14.用户依次输入语文、数学、英语，输出总分和平均分
# score = eval(input('请分别输入语文、数学、英语分数，以英文逗号分割：'))
# # print(f'总分为：{sum(score)},平均分为：{sum(score)/3}')
# print('总分为：%.1f,平均分为：%.1f' % (sum(score), sum(score)/3))

# 15.输入三个互不相等的整数，按照从小到大输出
# a = eval(input('输入三个互不相等的整数，以英文逗号分割：'))
# if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
#     print('请输入三个互不相等的数！')
# else:
#     if a[0] > a[1] > a[2]:
#         print(a[2], a[1], a[0])
#     elif a[0] > a[2] > a[1]:
#         print(a[1], a[2], a[0])
#     elif a[1] > a[2] > a[0]:
#         print(a[0], a[2], a[1])
#     elif a[1] > a[0] > a[2]:
#         print(a[2], a[0], a[1])
#     elif a[2] > a[1] > a[0]:
#         print(a[0], a[1], a[2])
#     elif a[2] > a[0] > a[1]:
#         print(a[1], a[0], a[2])

# 方法2
# a = eval(input('输入三个互不相等的整数，以英文逗号分割：'))
# if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
#     print('请输入三个互不相等的数！')
# else:
#     if max(a) == a[0]:
#         if a[1] > a[2]:
#             print(a[2], a[1], a[0])
#         else:
#             print(a[1], a[2], a[0])
#     elif max(a) == a[1]:
#         if a[2] > a[0]:
#             print(a[0], a[2], a[1])
#         else:
#             print(a[2], a[0], a[1])
#     elif max(a) == a[2]:
#         if a[1] > a[0]:
#             print(a[0], a[1], a[2])
#         else:
#             print(a[1], a[0], a[2])

# 方法3
# a = eval(input('输入三个互不相等的整数，以英文逗号分割：'))
# if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
#     print('请输入三个互不相等的数！')
# else:
#     b = sorted(a)
#     print(b[0], b[1], b[2])

# 方法4
# list1 = []
# a1, a2, a3 = eval(input('输入三个互不相等的整数，以空格分割：'))
# if a1 == a2 or a1 == a3 or a2 == a3:
#     print('请输入三个互不相等的数！')
# else:
#     list1.append(int(a1))
#     list1.append(int(a2))
#     list1.append(int(a3))
#     list1.sort()
#     print(list1)

# 16.登录的判断
# 提示输入用户名和密码，如果用户名等于Admin，密码为123，提示登录成功，
# 如果用户名不是Admin，提示用户名不存在
# 如果密码不等于123，提示密码错误
# username = input('请输入用户名：')
# pwd = input('请输入密码：')
# if username != 'Admin':
#     print('用户名不存在')
# elif pwd != '123':
#     print('密码错误')
# elif username == 'Admin' and pwd == '123':
#     print('登录成功')

# 17.输入张三的语文、数学成绩，输出以下判断是否正确，正确（True）,错误（False）
# 张三的语文和数学都大于90分
# yuwen = float(input('请输入语文成绩：'))
# shuxue = float(input('请输入数学成绩：'))
# print(yuwen > 90 and shuxue > 90)
# # 张三的语文和数学有一门大于90分
# print(yuwen > 90 or shuxue > 90)

# 18.输入一个时间(比如，13:12:11)，实现以下需求：
# 对输入的时间进行有效性判断
# 计算时分秒数字之和
# 把输入的时间时常转化为秒，并输出
# 输入的时间再过18888秒后的时间是多少
time = input('请输入一个时间，比如13:12:11')
hour = time[0:2]
min = time[3:5]
sec = time[6:8]
hour = int(hour)
min = int(min)
sec = int(sec)
if not (0 <= hour <= 23 and 0 <= min <= 59 and 0 <= sec <= 59):
    print('输入的时间无效，请重新输入')
else:
    print('时分秒数字之和为：', hour + min + sec)
    secs = hour * 3600 + min * 60 + sec
    print('输入的时间转化为秒是：', secs)
    secs += 18888
    print('输入的时间再过18888秒之后是%d秒' % secs)
    hour = secs//3600
    min = secs // 60 - hour * 60
    sec = secs - min * 60 - hour * 3600
    print('输入的时间再过18888秒之后是%d小时%d分钟%d秒' % (hour, min, sec))

# 方法2









