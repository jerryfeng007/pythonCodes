# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
with open('101.txt', 'r') as f:
    c1 = f.read()

with open('102.txt', 'r') as f:
    c2 = f.read()

with open('103.txt', 'w') as f:
    # if c1 > c2:
    #     f.write(c2 + c1)
    # else:
    #     f.write(c1 + c2)

    # 方式2
    l = [c1, c2]
    print(l)
    l.sort()
    print(l)
    s = ''.join(l)
    print(s)
