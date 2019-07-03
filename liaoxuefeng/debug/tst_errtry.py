#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def foo(s):
	return 10/int(s);

def bar(s):
	return foo(s)*2;

def main(): 
	print('start');
	try:
		print('try:');
		r = 10/0;
		print('result:', r);
	except ZeroDivisionError as e:
		print('except:', e);
	finally:
		print('finally...');
	print('end');

	'''
	可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
	这时，只要main()捕获到了，就可以处理：
	'''
	try:
		bar('0');
	except Exception as e2:
		print('Error:', e2);
	finally:
		print('finally...');

	bar(0);
	'''
	Traceback (most recent call last):
	  File "tst_try.py", line 49, in <module>
	    main();
	  File "tst_try.py", line 33, in main
	    bar(0);
	  File "tst_try.py", line 8, in bar
	    return foo(s)*2;
	  File "tst_try.py", line 5, in foo
	    return 10/int(s);
	ZeroDivisionError: integer division or modulo by zero
	'''

if __name__ == '__main__':
	main();

	

