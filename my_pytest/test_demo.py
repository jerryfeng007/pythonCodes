# 1. py文件以 test_开头
# 2. 函数以 test_命名
# 3. pytest -s 可以看到打印的信息
# 4. pytest -vs 可以看到更详细的信息


def func(x):
    print('只有pytest -s 才能看到打印的信息')
    return x+1


def test_func():
    print('这是test_demo')
    a = func(3)
    assert a == 4
