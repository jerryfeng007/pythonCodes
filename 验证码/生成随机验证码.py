import random
# xxxx-xxxx-xxxx-xxxx   数字 大写英文 生成500个随机验证码

l1 = []
for i in range(65, 91):
    c = chr(i)
    l1.append(c)

l2 = []
for i in range(0, 10):
    l2.append(str(i))

l3 = l1 + l2


# 实现
def code(l3):
    l4 = []
    for i in range(4):
        r = random.sample(l3, 4)
        r = ''.join(r)
        l4.append(r)
    r = '-'.join(l4)
    print(r)


for i in range(500):
    print(i)
    code(l3)
