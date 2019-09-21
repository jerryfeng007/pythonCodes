# yield是最底层的
# 进一步封装，这里使用了greenlet

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()  # 使用switch就可以随意切换了
    print(34)


def test2():
    print(56)
    gr1.switch()  # 使用switch就可以随意切换了
    print(78)
    gr1.switch()


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr2.switch()  # 使用switch就可以随意切换了

# 但是不可能所有的都是指定程序去切换，也不现实，请看下一章---协程3
