# test_example.py
import pytest
from util import *

file = './hello.log'
LOG = init_logger('hello', file)

if __name__ == "__main__":
    str_cmd = 'pytest test_fixture.py --html=report/report.html'
    result, errors, return_code = cmd_ecute(str_cmd, LOG)
    LOG.info(f'result:{result}')
    LOG.info(f'errors:{errors}')
    LOG.info(f'return_code:{return_code}')
    # print('test')
    # pytest.main(['-vs', '--html=report/report.html'])