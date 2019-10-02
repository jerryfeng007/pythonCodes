# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加由键盘控制
num = 4
a = 4


def aaa(num):
    if num == 0:
        return 0
    return int(str(a) * num) + aaa(num-1)


print(aaa(num))
