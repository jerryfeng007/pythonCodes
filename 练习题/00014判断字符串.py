s = '123abc'
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())


# 自定义函数，判断字符串是否为数字
def is_num(s, l):
    for i in s:
        if i not in l:
            print('不是数字')
            break
    else:
        print('是数字')


s = '777.8'
l = ['0', '1' '2', '3', '4', '5', '6', '7', '8', '9']
is_num(s, l)
