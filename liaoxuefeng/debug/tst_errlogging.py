#!/usr/bin/env python3
# -*- coding:utf-8  -*-

import logging

def foo(s):
	return 10 / int(s);

def bar(s):
	return foo(s) * 2;

def main():
	try:
		bar('0');
	except Exception as e:
		logging.exception(e);
	
main();
print('END');
'''
ERROR:root:division by zero
Traceback (most recent call last):
  File "tst_logging.py", line 14, in main
    bar('0');
  File "tst_logging.py", line 10, in bar
    return foo(s) * 2;
  File "tst_logging.py", line 7, in foo
    return 10 / int(s);
ZeroDivisionError: division by zero
END
'''
