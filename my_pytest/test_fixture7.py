# 演示 params

import pytest


@pytest.fixture(params=[1, 2, 3])  # 相当于for循环
def eee(request):
    print('演示 params')
    return request.param


def test_25_a(eee):
    print('autouse的用法1哈哈哈')
    print(eee)
    assert eee != 0
