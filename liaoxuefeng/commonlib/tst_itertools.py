#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import itertools, time


def tst_icount():
	natuals = itertools.count(2);
	for n in natuals:
		print(n);
		time.sleep(1);
	
def tst_icount2():
	odd = itertools.count(1, 2);
	for x in odd:
		print(x);
		time.sleep(1);

def tst_icycle():
	cs = itertools.cycle('ABCD');
	for c in cs:
		print(c);
		time.sleep(1);

def tst_irepeat():
	ns = itertools.repeat('OX', 3);
	for n in ns:
		print(n);
		time.sleep(1);

#把一组迭代对象串联起来，形成一个更大的迭代器
def tst_ichain():
	for c in itertools.chain('ABC', 'XYZ'):
		print(c);

def tst_igroupby():
	for key, group in itertools.groupby('AAABBBCCAAADD'):
		print(key, list(group));

	for key, group in itertools.groupby('aAAbbBCcAaa', lambda c:c.upper()):
		print(key, list(group));

def main():
	#tst_icount(); #2开始无限迭代
	#tst_icount2(); #1开始奇数无限迭代
	#tst_icycle(); #ABCDABCD无限迭代
	tst_irepeat();
	tst_ichain();
	tst_igroupby();

if __name__ == '__main__':
	main();
