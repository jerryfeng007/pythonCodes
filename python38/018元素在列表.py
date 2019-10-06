# 判断元素是否在列表

# 方法1
l = [1, 2, 3, 4]
print(5 in l)


# 方法2
for i in l:
    if i == 5:
        print('5在列表中')
        break
else:
    print('5不在列表中')
