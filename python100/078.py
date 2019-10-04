# 找到年龄最大的人，并输出。请找出程序中有什么问题。

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

person2 = sorted(person.items(), key=lambda x: x[1])
print(person2)

a = person2[-1]
print(a)

print(a[0])

