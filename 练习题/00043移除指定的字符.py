# 给定一个字符串，然后移除指定位置的字符

test_str = "Runoob"  # 移除第三个字符


def move(s, n):
    return s[:n-1] + s[3:]


print(move(test_str, 3))


# 方法2
def move2(s, n):
    return s.replace(s[n-1], '', 1)


print(move2(test_str, 3))
