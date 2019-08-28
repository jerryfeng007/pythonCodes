from unittest.mock import patch

# 单元测试的核心还是 mock，mock 掉依赖项，测试相应的逻辑或算法的准确性

# 暂时不会用patch

# 编写高质量的单元测试
# 1.需要我们 cover 模块的每条语句，提高 Test Coverage
#   python的coverage tool：
#   https://coverage.readthedocs.io/en/v4.5.x


# 2.模块化

def work(arr):
    # pre process
    ...
    ...
    # sort
    l = len(arr)
    for i in range(0, l):
        for j in range(i + 1, j):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    # post process
    ...
    ...
    return arr

# ------------------------------------------->

# 正确的测试方法，应该是先模块化代码


def preprocess(arr):
    ...
    ...
    return arr


def sort(arr):
    ...
    ...
    return arr


def postprocess(arr):
    ...
    return arr


def work(self):
    arr = preprocess(arr)
    arr = sort(arr)
    arr = postprocess(arr)
    return arr

# 测试三个子函数的功能正确性；
# 然后mock子函数
# 调用 work() 函数
# 验证三个子函数被 call 过

# ----------------------------------------------------------------->


def test_preprocess(self):
    ...


def test_sort(self):
    ...


def test_postprocess(self):
    ...


@patch('%s.preprocess')
@patch('%s.sort')
@patch('%s.postprocess')
def test_work(self, mock_post_process, mock_sort, mock_preprocess):
    work()
    self.assertTrue(mock_post_process.called)
    self.assertTrue(mock_sort.called)
    self.assertTrue(mock_preprocess.called)
