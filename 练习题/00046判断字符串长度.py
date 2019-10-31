# 给定一个字符串，然后判断改字符串的长度。


str = "runoob"


def ll(str):
    return len(str)


print(ll(str))


# 方法2
def lll(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


print(lll(str))
