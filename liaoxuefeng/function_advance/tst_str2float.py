#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

def f(x,y):
	return x*10 + y;

def f2(x,y):
	return x/10 + y;

def char2int(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

def str2float(s):
	#lnum = s.split('.');
	#print(lnum);
	#if(len(lnum)>2):
	#	print('ERROR');
	l = len(s);
	try: 
		i = s.index('.');
	except ValueError as e:
		i = -1;

	#print('i',i);
	#print('d',s[i+1:]);

	if(i == 0): # .123 之类
		num_i = 0;
		num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0 - l + i + 1 );
	elif (i == -1):  #123
		num_i = reduce(f,map(char2int, s));
		num_d = 0;
	elif (l - i <= 1): # 123.之类
		num_i = reduce(f,map(char2int, s[:i]));
		num_d = 0;
	else:
		num_i = reduce(f,map(char2int, s[:i]));
		num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0-l + i + 1 );
	
	#print('num[%d][%d]'%(num_i, num_d));
	return num_i + num_d;

def main():
	print(str2float('123.456'));
	print(str2float('0.456'));
	print(str2float('.456'));
	print(str2float('123.'));
	print(str2float('123'));

	'''
	3
	[123][0]
	123
	1
	[0][0]
	0
	0
	[0][0]
	0
	3
	[123][0]
	123
	[123][0]
	123
	'''

if __name__ == '__main__':
	main();

