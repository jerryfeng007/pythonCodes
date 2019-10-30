def clear(l):
    l.clear()
    return l


print(clear([1, 2, 3, 4]))


def dele(l):
    del l[::]
    return l


print(dele([1, 2, 3, 4]))
