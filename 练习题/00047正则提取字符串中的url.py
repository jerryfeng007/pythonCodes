# 给定一个字符串，里面包含 URL 地址，需要我们使用正则表达式来获取字符串的 URL。

s = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'

# 这里没有使用正则

l = s.split('，')
print(l)

ll = []
for i in range(len(l)):
    lll = l[i].split('：')
    ll.append(lll[1])

print(ll)
