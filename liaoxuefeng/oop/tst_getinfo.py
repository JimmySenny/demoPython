#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import types

def fn():
	pass;

def tst_type():
	print('tst_type');
	print(type(123));
	print(type('123'));
	print(type(None));
	print(type(abs));

	'''
	<type 'int'>
	<type 'str'>
	<type 'NoneType'>
	<type 'builtin_function_or_method'>
	'''
	print( type(123) == type(456) ); #True
	print( type(123) == int ); #True
	print( type(123) == str ); #False
	print( type(fn) == types.FunctionType ); #True
	print( type(abs) == types.BuiltinFunctionType ); #True
	print( type(lambda x: x) == types.LambdaType ); #True
	print( type(x for x in range(10)) == types.GeneratorType ); #True

def tst_isinstance():
	print('tst_isinstance');
	#能用type()判断的基本类型也可以用isinstance()判断
	print( isinstance(123, int) ); #True
	print( isinstance('123', str) ); #True 
	print( isinstance(b'a', bytes) ); #True

	#并且还可以判断一个变量是否是某些类型中的一种
	print( isinstance([1, 2, 3], (list, tuple)) ); #True
	print( isinstance((1, 2, 3), (list, tuple)) ); #True

	pass; # class 判断 类及其子类

def tst_dir():
	print('tst_dir');
	print(dir('ABC'));

	# getattr() setattr() hasattr()

def main():
	tst_type();
	tst_isinstance();
	tst_dir();

if __name__ == '__main__':
	main();
	
