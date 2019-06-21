#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
	L = ['A','B','C','D','E'];
	T = ('a','b','c','d','e');
	D = {'k1':1,'k2':2,'k3':3,'k5':5,'k4':4};
	S = '12345678';

	for i in L:
		print(i);
	for i in T:
		print(i);
	for k in D:
		print(k);
	for v in D.values():
		print(v);
	for k,v in D.items():
		print(k,v);
	for ch in S:
		print(ch);

if __name__ == '__main__':
	main();


