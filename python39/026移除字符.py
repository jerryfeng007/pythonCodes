#  移除字符串中的指定位置字符

# 移除第三个字符

test_str = "Runoob"

l = list(test_str)
print(l)

l.pop(2)
print(l)

test_str = ''.join(l)
print(test_str)
