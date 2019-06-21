#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

def main():
	print(list(range(1,11))); # 1,2,3,...
	print([x*x for x in range(1,11)]); #1*1, 2*2, 3*3,...
	print([x*x for x in range(1,11) if x % 2 == 0]); #2*2, 4*4, 6*6,...
	print([m+n for m in 'ABC' for n in '123']); #A1,A2,A3,B1,B2,B3,...

	# 列出当前目录下的所有文件和目录名
	print([d for d in os.listdir('.')]);

	D = {'A':'1', 'B':'2', 'C':'3'};
	print([k + '=' + v for k, v in D.items()]);

    # 把一个list中所有的字符串变成小写
	L = ['Hello', 'World', 'IBM', 'Apple'];
	print([s.lower() for s in L]);

	L1 = ['Hello', 'World', 18, 'Apple', None];
	print([ x for x in L1 if (isinstance( x, str))]);



if __name__ == '__main__':
	main();
