#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import wraps

def logit(logfile='out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + " was called";
			print(log_string);
			#打开logfile
			with open(logfile, 'a') as opend_file:
				opend_file.write(log_string+'\n');
			return func(*args, **kwargs)
		return wrapped_function
	return logging_decorator

@logit()
def myfunc1():
	pass;

myfunc1();
#outputs: myfunc1 was called
#		: out.log

@logit(logfile='out2.log')
def myfunc2():
	pass;

myfunc2();
#outputs: myfunc2 was called
#		: out2.log
