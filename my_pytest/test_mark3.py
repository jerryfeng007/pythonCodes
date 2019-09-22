# 参数化

import pytest

numlist = [666, 888]


@pytest.mark.parametrize('num', numlist)
def test_15(num):
    print('哈哈哈')
    assert num > 0
