import pytest


@pytest.fixture()
def login_func():
    print('这是conftest.py文件里的登陆，如果别的py文件里需要登陆可以直接使用')
