# 给定一个字符串，然后将其翻转，逆序输出。

s = 'abcde'


# 方法1
def fan(s):
    return reversed(s)


print(''.join(fan(s)))


# 方法2
def fan2(s):
    s1 = ''
    for i in s:
        s1 = i + s1
    return s1


print(fan2(s))


# 方法3 切片
def fan3(s):
    return s[::-1]


print(fan3(s))
