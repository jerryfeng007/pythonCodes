# 演示 scope=session, 运行 fixture5 和 fixture6多个py文件， 可以跨文件使用


def test_23_a():
    print('autouse的用法1哈哈哈')
    assert 1 == 1


def test_24_a():
    print('autouse的用法2嘿嘿嘿')
    assert 1 == 1
