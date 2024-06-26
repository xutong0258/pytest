# test_example.py
import pytest
from util import *

file = './test.log'
LOG = init_logger('hello', file)

# 定义一个fixture，用于setup和teardown
@pytest.fixture(scope="module")
def setup_data():
    # setup代码
    LOG.info('setup_data')
    data = {"key1": "value1", "key2": "value2"}
    yield data  # 返回数据，测试用例可以使用这个数据
    # teardown代码
    LOG.info('Tearing down data...')

# 使用fixture的测试用例
def test_example1(setup_data):
    assert setup_data["key1"] == "value1"

def test_example2(setup_data):
    assert setup_data["key2"] == "value2"

# 如果需要在每个测试用例之前和之后运行setup和teardown代码，可以使用yield
@pytest.fixture(autouse=True)
def setup_teardown():
    # setup代码
    LOG.info('setup_teardown')
    yield  # 测试用例执行到这里，然后执行测试用例
    # teardown代码
    LOG.info('setup_teardown')

if __name__ == "__main__":
    pytest.main(['-vs', '--html=report/report.html'])