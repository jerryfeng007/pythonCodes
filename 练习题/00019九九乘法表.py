"""
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
"""

for j in range(1, 10):
    for i in range(1, j+1):
        print(f'{i}x{j}={i*j}', end=' ')
    print()
