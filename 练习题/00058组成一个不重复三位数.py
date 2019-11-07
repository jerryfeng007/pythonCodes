# 四个数字，1， 2， 3， 4， 能组成多少个互不相同且无重复数字的三位数？各是多少？

# 分析：从个位、十位、百位的角度考虑

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i + j * 10 + k * 100)
