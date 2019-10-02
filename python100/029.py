# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

a = 23459
print(len(str(a)))

a = str(a)
a = a[::-1]
for i in a:
    print(i)

