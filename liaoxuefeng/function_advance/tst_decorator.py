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

def log3(text):
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

@log3('33333')
def now3():
	print('decorator3');

@log4('44444')
def now4():
	print('decorator4');

def main():
	print('now');
	f = now;
	f(); # decorator
	print(now.__name__); # now
	print(f.__name__);   # now
	print('now1');
	now1();
	print(now1.__name__);
	print('now2');
	now2();
	print(now2.__name__);
	print('now3');
	now3();
	print(now3.__name__);
	print('now4');
	now4();
	print(now4.__name__);



if __name__ == '__main__':
	main();
