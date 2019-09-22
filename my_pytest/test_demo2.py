# 3. 类，以Test开头命名， 方法以test_开头


class TestClass:
    def test_1(self):
        x = 'this'
        assert 'h' in x

    def test_2(self):
        x = 'hello'
        assert 'a' not in x
