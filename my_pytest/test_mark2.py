# pytest -vs test_mark2.py::TestClassEEE::test_13
# pytest -vs -k test_13 test_mark2.py
# pytest -vs -k "not test_13" test_mark2.py
# pytest -vs -k "test_13 or test_14" test_mark2.py


class TestClassEEE:
    def test_13(self):
        print('哈哈哈')
        assert 1 == 2

    def test_133(self):
        print('嘿嘿嘿')
        assert 1 == 1

    def test_14(self):
        print('嘿嘿嘿')
        assert 1 == 1
