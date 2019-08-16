print('----------------方式1：一次性读取所有内容(内容多时不要这么用)---read()-------------------------')

with open('file1.txt', 'r') as f:
    con = f.read()
    print(con)

print('----------------方式2：一次性读取了所有行(内容多时不要这么用）--readlines()---------------------')

# with open('file1.txt', 'r') as f:
#     cons = f.readlines()       # ------------------------for循环遍历行列表
#     con = ''
#     for con_temp in cons:
#         con += con_temp
#     print(con, end='')

print('----------------方式3：每次读取一定长度的内容------------------read(size)----------------------')

# with open('file1.txt', 'r') as f:
#     con = ''
#     while True:
#         con_temp = f.read(100)
#         con += con_temp
#         if not con_temp:
#             break
#     print(con)

print('----------------方式4：每次读取一行-----------------------------readline()----------------------')

# with open('file1.txt', 'r') as f:
#     con = ''
#     while True:
#         con_temp = f.readline()
#         con += con_temp
#         if not con_temp:
#             break
#     print(con)

print('----------------方式5：for循环遍历f------------------------------------------------------------')

# with open('file1.txt', 'r') as f:
#     con = ''
#     for con_temp in f:                   # ------------------------for循环遍历f
#         con += con_temp
#     print(con, end='')

print('----------------写入文件------------------------------------------------------------')

with open('file2.txt', 'w') as f:
    print(con, end='', file=f)  # 这里使用了 print函数中的 file 写入文件了 哈哈哈哈哈
    # f.write(con)
