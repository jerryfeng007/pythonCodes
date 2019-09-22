# 6. setup_class  teardown_class，每个类执行一次


class TestMyClass:
    def setup_class(self):
        print('每个类中之前执行一次')
        self.a = 'hello'

    def teardown_class(self):
        print('每个类中之后执行一次')

    def test_7(self):
        assert 'h' in self.a

    def test_8(self):
        assert 'm' not in self.a
