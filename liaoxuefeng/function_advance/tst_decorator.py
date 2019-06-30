#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

def now():
	print('decorator');

def log(func):
	def wrapper(*args, **kwargs):
		print('call %s' % func.__name__);
		return func(*args, **kwargs);
	return wrapper;

@log # now1 = log(now1)
def now1():
	print('decorator1');

def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2('execute') # now3 = log2('execute')(now3)
def now2():
	print('decorator2');

def log3(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print('call %s()' % func.__name__);
		return func(*args, **kwargs);
	return wrapper;

def log4(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			print('call %s()' % func.__name__);
			return func(*args, **kwargs);
		return wrapper;
	return decorator;

@log3
def now3():
	print('decorator3');

@log4('44444')
def now4():
	print('decorator4');

def log4(params=None):
	def decorator(fn):
		@functools.wraps(fn)
		def wrapper(*args, **kwargs):
			print('%s begin call' % fn.__name__);
			if(isinstance(params, str)):
				print('args:%s'%params);
			func = fn(*args, **kwargs);
			print('%s end call' % fn.__name__);
			return func;
		return wrapper;
	if(not callable(params)):
		return decorator;
	return decorator(params);

@log4
def f1():
	print('f1 execute');

@log4()
def f2():
	print('f2 execute');

@log4('params...')
def f3():
	print('f3 execute');


def main():
	print('now--------------------');
	f = now;
	f(); # decorator
	print(now.__name__); # now
	print(f.__name__);   # now
	print('now1-------------------');
	now1();	#call now1 decorator1
	print(now1.__name__); #wrapper
	print('now2-------------------');
	now2();	#execute now2(): decorator2
	print(now2.__name__); #wrapper
	print('now3-------------------');
	now3(); #call now3()  decorator3
	print(now3.__name__); #now3
	print('now4-------------------');
	now4();	#call now4() decorator4
	print(now4.__name__); #now4
	print('f-------------------');
	f1();
	f2();
	f3();
if __name__ == '__main__':
	main();
