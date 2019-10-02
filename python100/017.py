# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = '123runoobc  kdf235*(dfl'
l_en = []
l_space = []
l_shu = []
l_other = []
for i in s:
    if i.isalpha():
        l_en.append(i)
    elif i.isdigit():
        l_shu.append(i)
    elif i.isspace():
        l_space.append(i)
    else:
        l_other.append(i)

print(len(l_en), len(l_space), len(l_shu), len(l_other))
