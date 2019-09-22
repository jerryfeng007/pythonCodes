# skip 模块

import pytest
import time


@pytest.importorskip(time)
def test_15():
    print('哈哈哈')
    print(time.time())
    assert 1 > 0
