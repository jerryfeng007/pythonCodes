import random

s = '01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

s1 = random.sample(s, 4)
print(s1)

s2 = ''.join(s1)
print(s2)
