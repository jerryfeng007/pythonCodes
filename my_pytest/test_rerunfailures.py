# 失败重跑，尤其是ui自动化
# 安装pytest-rerunfailures
# pytest -sv test_rerunfailures.py --reruns 1


def func(x):
    print('只有pytest -s 才能看到打印的信息')
    return x+1


def test_func():
    print('这是test_demo')
    a = func(3)
    assert a == 5
