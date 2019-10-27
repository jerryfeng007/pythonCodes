# 冒泡排序是指从头至尾比较相邻的元素，如果第一个元素比第二个元素大，就交换。
# 以下是冒泡升序


def mao_pao(l):
    for i in range(len(l)-1):  # 比较几轮
        flag = True
        for j in range(len(l)-1-i):  # 每一轮比较几次
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                flag = False
        if flag:
            return l  # 提前return
    return l


l1 = [1, 2, 3, -3, -2, -1, 0, 2, 1, 4, 2, 6]
print(mao_pao(l1))
