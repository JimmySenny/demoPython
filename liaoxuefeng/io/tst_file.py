#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

def main():
	try: 
		with open('./a.txt', 'r') as f:
			print(f.read());
	except Exception as e:
		logging.exception(e);
	finally:
		pass;

	print('-------------------------------');
	with open('./tst_file.py', 'r') as f:
		print(f.read());

	print('-------------------------------');
	with open('./abc.txt', 'r', encoding='utf-8') as f:
		for line in f.readlines(): 
			print('[%s]'%line);

	print('-------------------------------');
	with open('./abc.txt', 'r', encoding='utf-8' ) as f:
		while True:
			r = f.read(2);
			if( len(r) > 0):
				print(r);
			else:
				print('end');
				break;
	
if __name__ == '__main__':
	main();
