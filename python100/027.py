# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
aaa = input()
aaa = aaa[::-1]
print(aaa)
for i in aaa.split(','):
    print(i)

