# 10. scope   autouse
# scope: class       每个类调用一次
#        function    每个函数/方法调用一次
#        module      每个py文件调用一次
#        session     多个文件调用一次，可以跨py文件调用，每个文件其实就是module

import pytest


@pytest.fixture(scope='module', autouse=True)
def aaa(request):
    print(request.module.__name__)


@pytest.fixture(scope='function', autouse=True)
def bbb(request):
    print(request.function.__name__)


def test_17_a():
    print('autouse的用法1')
    assert 1 == 1


def test_18_a():
    print('autouse的用法2')
    assert 1 == 1
