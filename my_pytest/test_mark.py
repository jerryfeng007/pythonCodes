# 8. mark  pytest -m "标签" py文件     注意：必须用双引号，单引号检测不到
#          pytest -m "not 标签" py文件

import pytest


@pytest.mark.love
def test_13():
    print('哈哈哈')
    assert 1 == 2


def test_14():
    print('嘿嘿嘿')
    assert 1 == 1
