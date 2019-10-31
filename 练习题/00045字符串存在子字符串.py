# 给定一个字符串，然后判断指定的子字符串是否存在于该字符串中。
s = 'iloveuhahaha'


def in_not(s, ss):
    if ss in s:
        return True
    return False


print(in_not(s, 'hahaha'))
print(in_not(s, 'hhh'))


# 方法2
def in_not2(s, ss):
    if s.find(ss) > 0:
        return True
    return False


print(in_not2(s, 'hahaha'))
print(in_not2(s, 'hhh'))
