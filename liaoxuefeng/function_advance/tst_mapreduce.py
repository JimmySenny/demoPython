#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

def f(x):
	return x*x;

def f_add(x,y):
	return x + y;

def f_add2(x,y):
	return x*10+y;

#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
	return digits[s];


#整理成一个str2int的函数就是
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9};
def str2int(s):
	def fn(x,y):
		return 10*x+y;
	def char2num(s):
		return DIGITS[s];
	return reduce(fn,map(char2num,s));

#用lambda函数进一步简化成
def lchar2num(s):
	return DIGITS[s];
def lstr2int(s):
	return reduce(lambda x,y:10*x+y,map(lchar2num,s));
	
def main():
	m = map(f,[1,2,3,4,5,6,7,8,9]);
	print(m);

	#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
	r = reduce(f_add,[1,3,5,7,9]); 
	print(r); #25

	r = reduce(f_add2,[1,3,5,7,9]);
	print(r);  #13579

	r = reduce(f_add2, map(char2num, '13579'));
	print(r);

	i = str2int('1234567');
	print(i+1);

	i = lstr2int('987654321');
	print(i+1);


if __name__ == '__main__':
	main();
