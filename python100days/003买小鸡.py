# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for i in range(20):
    for j in range(33):
        for k in range(300):
            if i + j + k == 100 and i * 5 + j * 3 + k / 3 == 100:
                print(i, j, k)
