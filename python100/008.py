# 输出 9*9 乘法口诀表
'''
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={j*i}', end=' ')
    print()



