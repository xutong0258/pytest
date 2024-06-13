import os
import sys
import logging
import subprocess
from subprocess import *

print(f'Hello')

PROGRAM = 'Hello'

formatter2 = logging.Formatter(
'[%(asctime)s]'
'%(filename)s'
'[Line:%(lineno)d]: '
'%(message)s')

CH = logging.StreamHandler()
CH.setLevel(logging.DEBUG)
CH.setFormatter(formatter2)


LOG = logging.getLogger(PROGRAM)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(CH)

_format = ('[%(asctime)s][%(filename)s][%(funcName)s][%(lineno)s]'
' %(levelname)s: %(message)s')

def init_logger(loggername, file=None):
    logger = logging.getLogger(loggername)
    logger.setLevel(level=logging.DEBUG)
     # print("logger.handlers:", logger.handlers)
    if not logger.handlers:
       if file:
          file_handler = logging.FileHandler(file)
          file_format = logging.Formatter(_format)
          file_handler.setFormatter(file_format)
          file_handler.setLevel(logging.DEBUG)
          logger.addHandler(file_handler)
    return logger

def cmd_ecute(cmd, logger=None, outfile=None, errfile=None):
    if outfile is None and errfile is None:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # result = stdout.decode('utf-8').strip('\r\n')
        result = stdout
        errors = stderr
        return_code = process.returncode
        msg = result if not stderr else errors
        if logger:
            logger.info(cmd)
            logger.debug(return_code)
            if return_code != 0:
                logger.error(errors)

        return result, errors, return_code
    else:
        f_out = open(outfile, 'w')
        f_err = open(errfile, 'w')
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=f_out,
            stderr=f_err)
        output, errors = process.communicate()
        return_code = process.returncode
        if logger:
            logger.info(cmd)
            logger.debug(return_code)
        if return_code != 0:
            logger.error(errors)

        return return_code

def test():
    str_cmd = 'dir'
    result, errors, return_code = cmd_ecute(str_cmd, LOG)
    LOG.info(f'result:{result}')
    print('test')

if __name__ == '__main__':
   test()