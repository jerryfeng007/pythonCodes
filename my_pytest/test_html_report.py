# 安装pytest-html
# pytest -vs test_html_report.py --html=report12345.html --self-contained-html


def test_001():
    assert 1 > 0


def test_002():
    assert 1 > 2


def test_003():
    assert 1 > 3


def test_004():
    assert 1 > -1
