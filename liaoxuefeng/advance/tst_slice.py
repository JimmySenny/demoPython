#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
	L = ['A', 'B', 'C', 'D', 'E'];
	print(L[0:3]);# A,B,C
	print(L[:3]); # A,B,C
	print(L[-2:-1]); # D
	print(L[-2:]);   # D,E
	print(L[:]);   # A,B,C,D,E

	T = ('1','2','3','4','5');	
	print(T[:3]);

	S = 'ABCEDFG';
	print(S[:3]); #ABC

	R = list(range(100))
	print('R[:10] =', R[:10])
	print('R[-10:] =', R[-10:])
	print('R[10:20] =', R[10:20])
	print('R[:10:2] =', R[:10:2])
	print('R[::5] =', R[::5])

if __name__ == '__main__':
	main();
