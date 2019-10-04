# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

a = 1234
print('原始的为：', a)

# 加5
l = [(int(i) + 5) for i in str(a)]
print(l)

# 除以10的余数
for i in range(len(l)):
    l[i] = l[i] % 10
print(l)

# 交换
l[0], l[1], l[2], l[3] = l[3], l[2], l[1], l[0]
print(l)

l = [str(i) for i in l]
l = ''.join(l)
print('加密后为：', l)
