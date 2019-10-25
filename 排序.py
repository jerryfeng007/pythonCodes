import re
s = '192.168.0.25, 192.168.0.18, 192.168.0.9, 130.168.210.33? 192.168.0.23! 980.132.123.111: 127.0.0.1;'
s = re.sub(r'[^\w.]', ' ', s)
# print(s)

l = s.split()
# print(l)

l2 = []
for i in l:
    if i.startswith('192') or i.startswith('127'):
        l2.append(i)
print(l2)
