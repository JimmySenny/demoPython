#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from operator import itemgetter

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)];

def by_name(t):
	return t[0];
	pass;

def by_score(t):
	return t[1];
	pass;

def main():
	print(L);
	print('------------------------------------------------------');
	print(sorted(L, key=itemgetter(0)));
	print(sorted(L, key=itemgetter(0), reverse=True));
	print('------------------------------------------------------');
	print(sorted(L, key=itemgetter(1)));
	print(sorted(L, key=lambda t:t[1]));
	print(sorted(L, key=itemgetter(1), reverse=True));
	print('------------------------------------------------------');
	L1 = sorted(L, key=by_name);
	print(L1);
	L2 = sorted(L, key=by_score);
	print(L2);

if __name__ == '__main__':
	main();

