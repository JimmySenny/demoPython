#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def add_end(L=[]):
	L.append('end');
	return L;

def add_end2(L=None):
	if L is None:
		L = [];
	L.append('END');
	return L;

def main():
	a = [1,2,3];
	add_end(a);
	print(a);
	b = ['x','y','z'];
	add_end(b);
	print(b);

	print(add_end()); #end
	print(add_end()); #end, end
	print(add_end()); #end, end, end

	print(add_end2()); #END
	print(add_end2()); #END
	print(add_end2()); #END

if __name__ == '__main__':
	main();
