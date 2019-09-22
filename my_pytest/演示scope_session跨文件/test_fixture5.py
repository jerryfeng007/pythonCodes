# 演示 scope=session  只运行 fixture5 单个文件

import pytest


@pytest.fixture(scope='session', autouse=True)
def ddd():
    print('scope=session,多个文件只调用一次，可以跨py文件')


class TestClassBBB:
    def test_21_a(self):
        print('autouse的用法1哈哈哈')
        assert 1 == 1

    def test_22_a(self):
        print('autouse的用法2嘿嘿嘿')
        assert 1 == 1
