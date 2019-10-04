# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。

with open('101.txt', 'w') as f:
    while True:
        a = input('输入字符：')
        if a.endswith('#'):
            f.write(a[:-1])
            exit()
        f.write(a)
