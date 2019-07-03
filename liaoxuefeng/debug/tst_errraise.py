#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class FooError(ValueError):
	pass;

def foo(s):
	n = int(s);
	if (n == 0):
		raise FooError('invalid value: %s' % s);
	return 10/n;

foo('0');

'''
Traceback (most recent call last):
  File "tst_errraise.py", line 13, in <module>
	foo('0');
  File "tst_errraise.py", line 10, in foo
    raise FooError('invalid value: %s' % s);
__main__.FooError: invalid value: 0
'''
