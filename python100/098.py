# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

s = input('输入一个字符串：')

with open('101.txt', 'w') as f:
    f.write(s.upper())
