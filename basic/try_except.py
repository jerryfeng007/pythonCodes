# 1.Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常
try:
    print(4/0)
except Exception as e:
    print('0不能做除数', str(e))

# 2.except后面省略异常类型，这表示与任意异常相匹配（包括系统异常等）
try:
    print(4/0)
except:
    print('0不能做除数')

# 3.finally使用场景---无论如何都要执行的语句
# 文件的读取
# 无论是读取成功还是读取失败，都会执行f.close()
# 所以，文件读取，最好使用with open，就可以省略f.close()

print('----------------------------------如何选择合适的异常处理方式----------------------------------------')

# 方式1
try:
    pass
except Exception as e:
    print('异常了', str(e))    # 捕获异常，程序可以继续运行

# 方式2：
if 2 > 1:
    raise Exception('异常了')  # 直接报错，程序终止运行
