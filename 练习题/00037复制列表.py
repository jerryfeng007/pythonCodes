from copy import deepcopy


def copy1(l):
    l1 = l
    return l1


print(copy1([1, 2, 3]))


def copy2(l):
    return l.copy()


print(copy2([1, 2, 3]))


def copy3(l):
    return list(l)


print(copy3([1, 2, 3]))


def copy4(l):
    return deepcopy(l)


print(copy4([1, 2, 3]))


def copy5(l):
    return [x for x in l]


print(copy5([1, 2, 3]))
