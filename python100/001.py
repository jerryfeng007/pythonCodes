# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 方法1


def func1():
    l2 = []
    for ge in range(1, 5):
        for shi in range(1, 5):
            if shi != ge:
                for bai in range(1, 5):
                    if bai != shi and bai != ge:
                        a = str(bai)+str(shi)+str(ge)
                        l2.append(eval(a))
    l2.sort()
    print(l2)


# 方法2--------------------正常思路应该是这样
def func2():
    l3 = []
    for ge in range(1, 5):
        for shi in range(1, 5):
            for bai in range(1, 5):
                if ge != shi and ge != bai and shi != bai:
                    b = str(bai)+str(shi)+str(ge)
                    l3.append(eval(b))
    l3.sort()
    print(l3)


func1()
func2()
