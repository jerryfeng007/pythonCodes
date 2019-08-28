from unittest.mock import MagicMock

print('----------------------------------------side_effect--------------------------------------------------------')

# mock 的函数，属性是可以根据不同的输入，返回不同的数值,而不只是一个 return_value


def aaa(arg):
    if arg < 0:
        return 1
    else:
        return 2


mock123 = MagicMock()
mock123.side_effect = aaa

print(mock123(1))
print(mock123(-1))
