print('----------------------------用pdb进行代码调试-------------------------------------------------------------')

# 调试的手段
# 1.在代码中使用print语句
# 2.在IDE中设置断点
# 3.python pdb ---自带的库，命令行版本的IDE断点调试器

# 使用pdb


def bbb():
    print('进入了函数内部')
    print('还是在内部')


a = 1
b = 2
# import pdb         # 加入这2句
# pdb.set_trace()    # 加入这2句
bbb()
c = 3
print(a + b + c)


# 用法总结：
# 1.在程序加入import pdb    pdb.set_trace() 这2句
# 2.如果需要打印，格式为：p 变量名
# 3.如果继续执行下一行：  n
# 4.列举出当前代码行上下的11行：l
# 5.进入函数内部：s 命令行中会显示”--Call--“的字样，当执行完内部的代码块后，命令行中则会出现”--Return--“
# 6.继续执行，直到当前的函数完成返回：r
# 7.在20行再加一个断点：b 21
# 8.一直执行程序，直到遇到下一个断点
# 其他，参考文档：https://docs.python.org/3/library/pdb.html#module-pdb

print('----------------------------用cProfile进行代码调试-------------------------------------------------------------')

# 只需在开头导入 cProfile 这个模块，并且在最后运行cProfile.run() 就可以了


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res


import cProfile
cProfile.run('fib_seq(30)')
