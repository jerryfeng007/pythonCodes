# 在数组 arr 中查找字符 D
# 注意，可能会有多个值哦

arr = ['A', 'B', 'C', 'D', 'B', 'E']
y = 'B'


def chazhao(arr, y):
    for i, v in enumerate(arr):
        if v == y:
            print(i)


chazhao(arr, y)
