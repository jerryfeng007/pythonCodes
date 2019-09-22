# 5. setup_function  teardown_function，每个用例执行一次


def setup_function():
    print('每个用例前执行一次')


def teardown_function():
    print('每个用例后执行一次')


def test_5():
    a = 'hello'
    assert 'h' in a


def test_6():
    a = 'hello'
    assert 'm' not in a
