# 1.字符串反转
s = 'HelloWorld'
print(s[::-1])

# 2.列表反转
list1 = [1, 2, 3, 2, 5, 4]
list1.reverse()
print(list1)

# 3.元组的反转
tuple1 = (1, 2, 1, 4, 3)
s = ''
for s1 in tuple1:
    s = str(s1) + s
    print(s)

# 4.删除列表中所有的1
# 方法1：这个方法的坏处，是把所有的元素都去重了，所以结果可能不正确
L = [1, 2, 3, 1, 3, 1, 5, 1]
s = set(L)    # 去重（备注：set()是集合，不允许重复的值）
L = list(s)   # 把集合转变为列表
L.remove(1)
print(L)

# 方法2：靠谱
L1 = [1, 2, 3, 1, 3, 1, 5, 1]
while True:
    try:
        L1.remove(1)
    except Exception as e:
        print(L1)
        break

# 方法3：靠谱
L2 = [1, 2, 3, 1, 3, 1, 5, 1]
L2.sort()
while True:
    if L2[0] == 1:
        L2.remove(1)
    else:
        print(L2)
        break


