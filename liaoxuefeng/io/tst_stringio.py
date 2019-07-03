#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO

def main():
	f = StringIO();
	print('%d'%f.write('Hello'));
	print('%d'%f.write(' '));
	print('%d'%f.write('Python!'));

	print(f.getvalue());

	f2 = StringIO('hello\nhi\nhow are you');
	while True:
		s = f2.readline();
		if (s == ''):
			break;
		print(s.strip());
	'''
	5
	1
	7
	Hello Python!
	hello
	hi
	how are you
	'''

if __name__ == '__main__':
	main();

