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
# if username.strip().lower() != 'admin':
#     print('用户名不存在')
# elif pwd != '123':
#     print('密码错误')
# elif username.strip().upper() == 'ADMIN' and pwd == '123':
#     print('登录成功')

# 17.输入张三的语文、数学成绩，输出以下判断是否正确，正确（True）,错误（False）
# 张三的语文和数学都大于90分
# yuwen = float(input('请输入语文成绩：'))
# shuxue = float(input('请输入数学成绩：'))
# print(yuwen > 90 and shuxue > 90)
# # 张三的语文和数学有一门大于90分
# print(yuwen > 90 or shuxue > 90)

# 18.输入一个时间(比如，13:12:11)，实现以下需求：
'''
对输入的时间进行有效性判断
计算时分秒数字之和
把输入的时间时常转化为秒，并输出
输入的时间再过18888秒后的时间是多少
'''
# 方法1
# 验证时间有效性
# def verify(time):
#     if time.strip().replace(':', '').isdigit():
#         time = time.split(':')
#         if 0 <= int(time[0]) <= 23 and 0 <= int(time[1]) <= 59 and 0 <= int(time[2]) <= 59:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# # 求时分秒之和
# def total(time):
#     time_list = []
#     time = time.split(':')
#     time_list.append(int(time[0]))
#     time_list.append(int(time[1]))
#     time_list.append(int(time[2]))
#     return time_list
#
#
# # 把输入的时间时常转化为秒，并输出
# def transfer(time_list):
#     return time_list[0] * 3600 + time_list[1] * 60 + time_list[2]
#
#
# # 输入的时间再过18888秒后的时间是多少
# def after(secs):
#     secs += 18888
#     if secs > 86400:
#         secs = secs - 86400
#         h = secs // 3600
#         m = secs // 60 - h * 60
#         s = secs - h * 3600 - m * 60
#     else:
#         h = secs // 3600
#         m = secs // 60 - h * 60
#         s = secs - h * 3600 - m * 60
#
#     return h, m, s
#
#
# if __name__ == '__main__':
#     time = input('请输入一个时间，比如13:12:11')
#     if verify(time):
#         print('有效')
#         time_list = total(time)
#         print('时分秒之和为：', sum(time_list))
#         secs = transfer(time_list)
#         print('输入的时间转化为秒是：', secs)
#         h, m, s = after(secs)
#         print('输入的时间再过18888秒之后是：{}时{}分{}秒'.format(h, m, s))
#     else:
#         print('无效')


# 方法2
# from datetime import datetime, timedelta
#
#
# # 验证时间有效性
# def verify(time):
#     time_list = []
#     if time.strip().replace(':', '').isdigit():
#         time = time.split(':')
#         if 0 <= int(time[0]) <= 23 and 0 <= int(time[1]) <= 59 and 0 <= int(time[2]) <= 59:
#             time_list.append(int(time[0]))
#             time_list.append(int(time[1]))
#             time_list.append(int(time[2]))
#             return time_list
#         else:
#             return False
#     else:
#         return False
#
#
# # 求时分秒之和
# def total(time_list):
#     return sum(time_list)
#
#
# # 把输入的时间时常转化为秒，并输出
# def transfer(time_list):
#     return time_list[0] * 3600 + time_list[1] * 60 + time_list[2]
#
#
# # 输入的时间再过18888秒后的时间是多少
# def after(time_list):
#     datetime01 = datetime(2019, 6, 3, time_list[0], time_list[1], time_list[2], 0)
#     return datetime01 + timedelta(seconds=18888)
#
#
# if __name__ == '__main__':
#     time = input('请输入一个时间，比如13:12:11')
#     time_list = verify(time)
#     if time_list:
#         print('有效')
#         total = total(time_list)
#         print('时分秒之和为：', total)
#         secs = transfer(time_list)
#         print('输入的时间转化为秒是：', secs)
#         datetime02 = after(time_list)
#         print(f'18888秒之后的时间为：{datetime02.hour}时{datetime02.minute}分{datetime02.second}秒')
#         print(type(datetime02.hour))
#     else:
#         print('无效')

# 19.输入小王的成绩（语文、英语、数学）
'''
如果平均分数大于或等于90，提醒“你是个聪明的孩子”
如果平均分数低于60分，提醒“你的成绩不理想，以后好好努力”
'''
# score = eval(input('请输入语文、英语、数学分数，以英文逗号分割：'))
# score_avg = sum(score) / 3
# print('平均分为%.1f' % score_avg)
# if score_avg >= 90:
#     print('你是个聪明的孩子')
# elif score_avg < 60:
#     print('成绩不理想，好好努力')

# 20.输入小王的成绩（语文、英语、数学）
'''
如果有一门是100分
如果有2门大于90分
如果3门都大于80分
满足以上任意一种情况，奖励一朵小红花
'''
# list1 = []
# score = eval(input('请输入语文、英语、数学分数，以英文逗号分割：'))
# if score[0] == 100 or score[1] == 100 or score[2] == 100:
#     if score[0] == 100:
#         print('语文100分，奖励小红花')
#     elif score[1] == 100:
#         print('英语100分，奖励小红花')
#     else:
#         print('数学100分，奖励小红花')
# elif (score[0] >= 90 and score[1] >= 90) or (score[0] >= 90 and score[2] >= 90) or (score[1] >= 90 and score[2] >= 90):
#     if score[0] >= 90 and score[1] >= 90:
#         list1.append('语文')
#         list1.append('英语')
#         print(f'{list1}大于90分，奖励小红花')
#     elif score[0] >= 90 and score[2] >= 90:
#         list1.append('语文')
#         list1.append('数学')
#         print(f'{list1}大于90分，奖励小红花')
#     else:
#         list1.append('英语')
#         list1.append('数学')
#         print(f'{list1}大于90分，奖励小红花')
# elif score[0] >= 80 and score[1] >= 80 and score[2] >= 80:
#     print('三门都大于80分，奖励小红花')
# else:
#     print('没有小红花')

# 21.输入小王的成绩（语文、英语、数学）
'''
所有科目都及格：“恭喜！”
否则：“很遗憾，需要补考xx”
'''
# list1 = []
# score = eval(input('请分别输入语文、英语、数学分数，以英文逗号分割：'))
# if score[0] >= 60 and score[1] >= 60 and score[2] >= 60:
#     print('恭喜！')
# else:
#     if score[0] < 60:
#         list1.append('语文')
#     if score[1] < 60:
#         list1.append('英语')
#     if score[2] < 60:
#         list1.append('数学')
#     print(f'很遗憾，需要补考{list1}')

# 22.输入小王的成绩（语文、英语、数学）
'''
成绩 >= 90， A 
90 > 成绩 >= 80 B
80 > 成绩 >= 70 C 
70 > 成绩 >= 60 D 
成绩 < 60 E 
'''
# score = eval(input('请分别输入语文、英语、数学分数，以英文逗号分割：'))
# avg = sum(score)/3
# print('平均分为%.1f' % avg)
# if avg >= 90:
#     print('A')
# elif avg >= 80:
#     print('B')
# elif avg >= 70:
#     print('C')
# elif avg >= 60:
#     print('D')
# elif avg < 60:
#     print('E')

# 23.输入一个月份，判断属于哪个季节
'''
冬季 12 1 2
春季 3 4 5
夏季 6 7 8 
秋季 9 10 11
'''
# score = eval(input('请输入一个月份，比如：5'))
# if score in [3, 4, 5]:
#     print(f'{score}月是春季')
# elif score in [6, 7, 8]:
#     print(f'{score}月是夏季')
# elif score in [9, 10, 11]:
#     print(f'{score}月是秋季')
# elif score in [12, 1, 2]:
#     print(f'{score}月是冬季')
# else:
#     print('输入错误')

# 24.先输入一个年份，再输入一个月份，输出该月的天数
# def verify(year, month):
#     if year.strip().isdigit() and month.strip().isdigit():
#         year = int(year)
#         month = int(month)
#         if month in [1, 3, 5, 7, 8, 10, 12]:
#             print(f'{year}年{month}月是31天')
#         elif month in [4, 6, 9, 11]:
#             print(f'{year}年{month}月是30天')
#         elif month == 2:
#             if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#                 print(f'{year}年{month}月有29天')
#             else:
#                 print(f'{month}月有28天')
#         else:
#             print('月必须为1-12之间的整数')
#     else:
#         print('年必须为四位数的整数，月必须为1-12之间的整数')
#
#
# if __name__ == '__main__':
#     year = input('输入一个年份')
#     month = input('输入一个月份')
#     verify(year, month)

# 25.涨工资
'''
工资<=4000，涨20%
4000--6000，涨15%
6000--8000，涨10%
8000-12000，涨5%
12000以上，涨500
输入一个工资金额，输出涨工资后的金额
'''
# def verify(name, salary):
#         if salary <= 4000:
#             print('%s原工资为%.2f,加薪后为%.2f' % (name, salary, salary * 1.2))
#         elif salary <= 6000:
#             print('%s原工资为%.2f,加薪后为%.2f' % (name, salary, salary * 1.15))
#         elif salary <= 8000:
#             print('%s原工资为%.2f,加薪后为%.2f' % (name, salary, salary * 1.1))
#         elif salary <= 12000:
#             print('%s原工资为%.2f,加薪后为%.2f' % (name, salary, salary * 1.05))
#         else:
#             print('%s原工资为%.2f,加薪后为%.2f' % (name, salary, salary + 500))
#
#
# if __name__ == '__main__':
#     name = ['张三', '李四', '王五']
#     salary_list = [4000, 6000.80, 8000.00]
#     for s in range(len(salary_list)):
#         verify(name[s], salary_list[s])

# 26.输入一个大于1的值，然后算出从1加到这个数之和，比如输入6，求1+2+3+4+5+6
# num = eval(input('输入一个大于1的整数：'))
# sum = 0
# i = 1
# if num <= 1:
#     print('必须大于1')
# else:
#     while i <= num:
#         sum += i
#         i += 1
#     print(i, sum)

# 27.输入一个正数，求出从1开始到这个数中所有包含3数字的数和3的倍数的和
# num = eval(input('输入一个大于0的正数：'))
# i = 1
# sum = 0
# while i <= num:
#     if '3' in str(i) or i % 3 == 0:
#         sum += i
#     i += 1
# print(sum)

# 28.输入班级人数，然后依次输入所有学员的成绩，计算该班级学员的平均成绩和总成绩
# num = eval(input('输入人数，比如3：'))
# i = 0
# total_s = 0
# while i < num:
#     score = eval(input('依次输入所有学员的成绩：'))
#     total_s += score
#     i += 1
# print(total_s, total_s / num)

# 29.键盘输入正整数n，求出n与其反序数之和并输出
# 例如，输入2038，输出应为2038+8302=10340
# 方法1
# n = input('请输入一个正整数：')
# n1 = n[::-1]
# total = int(n) + int(n1)
# print(n1, total)

# 方法2
# n = input('请输入一个正整数：')
# i = 0
# total = ''
# while i < len(n):
#     total = n[i] + total
#     i += 1
# print(total)
# print(int(total) + int(n))

# 30.2006年有8万人，每年增长25%，到哪年达到20万？
# 方法1
# total = 80000
# i = 2006
# while True:
#     i += 1
#     total *= 1.25
#     if total > 200000:
#         break
# print(i, total)

# 方法2
# total = 80000
# i = 2006
# while total <= 200000:
#     i += 1
#     total *= 1.25
# print(i, total)

# 31.输入一句话，判断大小多少个，小写多少，数字多少，其他多少
# s = input('输入一句话：')
# upper = []
# lower = []
# digit = []
# other = []
# for i in s:
#     if i.isupper():
#         upper.append(i)
#     elif i.islower():
#         lower.append(i)
#     elif i.isdigit():
#         digit.append(i)
#     else:
#         other.append(i)
# print(f'大写{len(upper)},小写{len(lower)},数字{len(digit)},其他{len(other)}')

# 32.从1加到100
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# 33.求1到100之间5和7的倍数之和
# list_sum = []
# for i in range(1, 101):
#     if i % 5 == 0 or i % 7 == 0:
#         list_sum.append(i)
# s = sum(list_sum)
# print(s)

# 34.水仙花数（三位数），比如 153 = 1的三次方 + 5的三次方 + 3的三次方
# for i in range(100, 1000):
#     if i == int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3:
#         print('i=', i)

# 35.9x9乘法表
'''
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9  
'''
# 考虑方式1:
# 1x3=3 2x3=6 3x3=9  # 先实现这一行
# 第一步
# i = 3
# for j in range(1, 4):
#     print(f'{j}x{i}={j * i}', end=' ')
# print()  # 需要加一个空行

# 第二步
# 在上面的基础上，把i变活，i取值1-9，需要注意与j的关系
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={j * i}', end=' ')
#     print()  # 需要加一个空行

# 考虑方式2:
'''
共有9行,用i表示,range(1, 10)
共有9列,用j表示,第1行有1列,第2行有2列,第3行有3列
i为1的时候, j需要为2, 即: for j in range(1, i+1)
'''
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={i * j}', end=' ')  # 这里不换行
#     print()  # 这里换行

# 36.100元买2元的铅笔，5元的铅笔盒，10元的文件夹，15元的彩笔，刚好花完，每样物品至少有一种，一共有多少种可能？打印出每一种组合
times = 0
for i in range(1, 51):
    for j in range(1, 21):
        for k in range(1, 11):
            for l in range(1, 7):
                if i * 2 + j * 5 + k * 10 + l * 15 == 100:
                    times += 1
                    print(times, i, j, k, l)

# 37.输入行数，打印三角形
'''
   *   
  ***
 *****
*******
空格：
1   3  第一行，3个空格
2   2  第二行，2个空格
3   1  第三行，1个空格
4   0  第四行，0个空格
空格数 = 总行数-i，i为第几行

星：
1   1  第一行，1颗星
2   3
3   5
4   7
星星 = 第几行 * 2 -1
'''
# n = eval(input('输入行数，比如5：'))
# for i in range(1, n+1):
#     print(' ' * (n-i) + '*' * (2*i-1))

# 方法2
# n = 10  # 行数 = 10
# for i in range(1, n+1):
#     # 先打印空格
#     for j in range(1, n-i+1):
#         print(' ', end='')
#     # 再打印*
#     for k in range(1, 2*i):
#         print('*', end='')
#     print()



