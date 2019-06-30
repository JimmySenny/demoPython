#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

def int2(x, base=2):
	return int(x, base);

fpint2 = functools.partial(int, base=2);

max2 = functools.partial(max, 10);

def tst_add(a,b,c=3):
	print('a is: %s b is:%s c is:%s' %(a, b, c));
	return a + b + c;
fpadd = functools.partial(tst_add,1,2);

def main():
	print('[%d]'% int('15')); #15
	print('[%o]'% 15); #17
	print('[%x]'% 15); #f
	print('[%d]'% int('15',base=8)); #13
	print('[%o]'% int('15',8)); #15
	print(int('15',base=8)); #13
	print(int('15',8)); #13
	print('[%d]'% int('15',base=16)); #21
	print('[%x]'% int('15',16)); #15
	print(int('15',base=16)); #21
	print(int('15',16)); #21
	print(int('101',base=2)); #5
	print(int('101',2)); #5
	print(int2('101')); #5
	print(int2('101',10)); #101
	print(fpint2('101')); #5
	# print(fpint2('101',10)); # int() takes at most 2 arguments (3 given)
	'''
	实际上会把10作为*args的一部分自动加到左边
	相当于：args = (10, 5, 6, 7) max(*args)
	'''
	print(max2(5, 6, 7)); # 10

	print('fpadd()', fpadd());
	print('fpadd(5)', fpadd(5));
	#print('fpadd(5,10)', fpadd(5, 10)); #TypeError: tst_add() takes at most 3 arguments (4 given)
	print('fpadd(c=10)', fpadd(c=10));

if __name__ == '__main__':
	main();
