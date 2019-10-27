# 找出第一个唯一的字符，并打印出他的索引

s = 'nssolwloenmm'

for i in range(len(s)):
    if s.count(s[i]) != 1:
        continue
    print(i)
    print(s[i])
    break
