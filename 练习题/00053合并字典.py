# 两个字典合并

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# 方式1
dict1.update(dict2)
print(dict1)


# 方式2   使用 **，函数将参数以字典的形式导入
def hebing(d1, d2):
    return {**d1, **d2}


print(hebing(dict1, dict2))
