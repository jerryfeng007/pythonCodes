# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

'''
Monday   Tuesday   Wednesday   Thursday   Friday   Saturday   Sunday
'''

s = input('输入第一个字母')

if s == 'M':
    print('Monday')
elif s == 'W':
    print('Wednesday')
elif s == 'F':
    print('Friday')
elif s == 'T':
    s2 = input('输入第二个字母')
    if s2 == 'u':
        print('Tuesday')
    elif s2 == 'h':
        print('Thursday')
    else:
        print('error')
elif s == 'S':
    s3 = input()
    if s3 == 'a':
        print('Saturday')
    elif s3 == 'u':
        print('Sunday')
    else:
        print('error')
