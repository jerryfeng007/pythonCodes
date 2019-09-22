import pytest


@pytest.mark.skip(reason='不想执行这一个')
def test_15():
    print('哈哈哈')
    assert 1 > 0


def test_16():
    print('哈哈哈')
    assert 2 > 0
