# 列表、字符串转换
# 输出结果为：i have fentiao,fendai,fensi and fish
names = ['fentiao', 'fendai', 'fensi', 'fish']

s = ','.join(names[0:3])
s = 'i have' + ' ' + s + ' ' + 'and fish'
print(s)
