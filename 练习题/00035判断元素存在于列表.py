def isin(l, n):
    if n in l:
        return True
    else:
        return False


print(isin([1, 2, 3, 4], 5))
print(isin([1, 2, 3, 4], 3))
