# 7. setup_method  teardown_method，每个类中的方法执行一次


class TestMyClass:
    def setup_method(self):
        print('每个方法之前执行一次')
        self.a = 'hello'

    def teardown_method(self):
        print('每个方法之后执行一次')

    def test_9(self):
        assert 'h' in self.a

    def test_10(self):
        assert 'm' not in self.a
