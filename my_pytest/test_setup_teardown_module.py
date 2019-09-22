# 4. setup_module  teardown_module   的全局性，整个py模块执行一次


def setup_module():
    print('整个py模块只执行一次')


def teardown_module():
    print('整个py模块只执行一次')


def test_3():
    a = 'hello'
    assert 'h' in a


def test_4():
    a = 'hello'
    assert 'm' not in a
