# 自定义函数 is_number() 方法来判断字符串是否为数字

l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(l)


def num(s):
    for i in s:
        if i not in l:
            print('输入的字符串不是数字！')
            break
    else:
        print('是数字！')


num('13')


# 使用isdigit
bb = '1.3'
print(bb.isdigit())
