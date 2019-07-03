#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

s = '0';
n = int(s);
logging.info('n = [%d]' %n );
print(10/n);

'''
INFO:root:n = [0]
Traceback (most recent call last):
  File "tst_logging.py", line 10, in <module>
    print(10/n);
ZeroDivisionError: division by zero
'''
