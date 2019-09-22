# 10. 必须建一个名字叫做：conftest.py的文件，里边可以写个函数login，然后@pytest.fixture()
#     然后在其他py文件里就可以使用了，把函数名作为参数传给需要用登陆的用例
#     注意，无需导入conftest，即可直接使用


def test_15(login_func):
    print('login之后，执行test_15')
    assert 1 == 1


def test_16(login_func):
    print('经济计划')
    assert 1 == 1
