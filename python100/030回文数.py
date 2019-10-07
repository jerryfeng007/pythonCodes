# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


def aaa(a):
    a = str(a)
    if a[0] == a[4] and a[1] == a[3]:
        print(True)
    else:
        print(False)


aaa(12321)
aaa(13456)
aaa(35753)
