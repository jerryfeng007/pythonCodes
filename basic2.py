# 秦红华课程---美女讲师教你学Python第一季：基础入门视频教程

# 程序的入口，main函数，增强程序的可读性
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

if __name__ == '__main__':
    print('如果没有main函数，程序也可以执行，但只能从上往下执行')
    v1 = sub(1, 2)
    v2 = add(3, 4)
    print(v1, v2)

# print函数
print('aaa')  # 换行
print('sss', end='')  # 不换行
print()

# 日期和时间-----------------------------------------------datetime----------------------------------------------------------
from datetime import datetime
print(datetime.now())
print(datetime.today())
print(datetime.now().day)
print(datetime.today().day)
print(datetime.now().month)
print(datetime.today().month)
print(datetime.now().year)
print(datetime.today().year)
print(datetime.now().hour)
print(datetime.today().hour)
print(datetime.now().minute)
print(datetime.today().minute)
print(datetime.now().second)
print(datetime.today().second)
print(datetime.now().microsecond)
print(datetime.today().microsecond)
print(datetime.now().date())
print(datetime.today().date())
print(datetime.now().time())
print(datetime.today().time())

# 格式化时间---------------------------------datetime.ctime()  和 datetime.strftime()-----------------------------------
print(datetime.now())  # 当前时间---返回datetime类型
print(datetime.now().ctime())  # 格式化当前时间---返回字符串类型
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 格式化当前时间---返回字符串类型，需要什么字段，就%什么字段














