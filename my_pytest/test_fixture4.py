# 演示 scope=class

import pytest


@pytest.fixture(scope='class', autouse=True)
def ccc():
    print('scope=class,一个类只调用一次')


class TestClassAAA:
    def test_19_a(self):
        print('autouse的用法1哈哈哈')
        assert 1 == 1

    def test_20_a(self):
        print('autouse的用法2嘿嘿嘿')
        assert 1 == 1
