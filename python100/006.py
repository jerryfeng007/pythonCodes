# 递归
i = 5


def gui(i):
    if i == 1:
        return 1
    return i * gui(i-1)


print(gui(i))
