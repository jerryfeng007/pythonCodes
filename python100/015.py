# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

a = 95

if a >= 90:
    print('A')
else:
    if a >= 60:
        print('B')
    else:
        print('c')


if a >= 90:
    print('A')
elif a >= 60:
    print('B')
else:
    print('c')
