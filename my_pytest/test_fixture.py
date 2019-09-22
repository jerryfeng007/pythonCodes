# 9. fixture   比如有的用例执行之前需要先登录，
#              @pytest.fixture()加到登陆函数前面，然后把函数名作为参数传给需要用登陆的用例

import pytest


@pytest.fixture()
def login():
    print('先login')


def test_11(login):
    print('哈哈哈')
    assert 1 == 1


def test_12():
    print('嘿嘿嘿')
    assert 1 == 1
