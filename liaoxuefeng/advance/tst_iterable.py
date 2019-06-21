#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Iterable

def main():
	L = ['A','B','C','D','E'];
	T = ('a','b','c','d','e');
	D = {'k1':1,'k2':2,'k3':3,'k5':5,'k4':4};
	S = '12345678';

	print( isinstance(L,Iterable));
	print( isinstance(T,Iterable));
	print( isinstance(D,Iterable));
	print( isinstance(D.values(),Iterable));
	print( isinstance(D.items(),Iterable));
	print( isinstance(S,Iterable));

if __name__ == '__main__':
	main();


