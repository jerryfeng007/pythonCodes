"""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
"""


def shuixianhua(n):
    l = len(str(n))
    sum = 0
    for i in str(n):
        sum += int(i) ** l
    if n == sum:
        return True
    else:
        return False


print(shuixianhua(153))
print('----------------------------')


# 获取指定区间内的水仙花数
def get_shuixianhua(min, max):
    for i in range(min, max):
        l = len(str(i))
        sum = 0
        for j in str(i):
            sum += int(j) ** l
        if sum == i:
            print(i)


get_shuixianhua(1, 10000)
