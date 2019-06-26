#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 过滤偶数
def is_odd(n):  
	return n % 2 == 1;

# 删除序列中的空字符串
def not_empty(s):
	return s and s.strip();

'''
用filter求素数
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
首先，列出从2开始的所有自然数，构造一个序列：
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
'''
def odd_iter():
	n = 1;
	while True:
		n +=  1;
		yield n;

def not_divisible(n):
	return lambda x : x % n > 0;

def primes():
	yield 2;
	it = odd_iter();
	while True:
		n = next(it);
		it = filter(not_divisible(n), it);
		yield n;

def is_primes():
	for n in primes():
		if (n < 100):
			print(n);
		else:
			break;

def main():
	print(filter(is_odd, [1,2,3,4,5,6,7,8,9])); #[1, 3, 5, 7, 9]
	print(filter(not_empty,['A', '', 'B', None, 'C', '  '])); #['A', 'B', 'C']
	is_primes();


if __name__ == '__main__':
	main();
