#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os;
import time;
import logging
logging.basicConfig(level=logging.INFO);

def tst_show_dir():
	print(os.path.abspath('.'));
	print(os.listdir('.'));
	print(os.walk('.',topdown=True, onerror=OSError(FileNotFoundError)));
	for x in os.listdir('.'):
		x_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(x)));
		print(os.path.getsize(x), x_time, x);

def tst_showall_dir(path='.'):
	#print([f for f in os.listdir(path) if os.path.isfile(f)]);
	#print('path:',path);
	for f in os.listdir(path):
		x = os.path.join(path, f);
		if os.path.isdir(x):
			tst_showall_dir(x);
		elif os.path.isfile(f):
			print(x);
		else:
			print(x);
			pass;

def tst_showall_dir2(path='.'):
	# os.walk(top, topdown=True, onerror=None, followlinks=False)
	for pathname, dirname, filename in os.walk(path ):
		print(dirname);
		for f in filename: 
			print(os.path.join(pathname, f));

def tst_search_dir(key, path='.'):
	for f in os.listdir(path):
		x = os.path.join(path, f);
		if os.path.isdir(x):
			tst_search_dir(key,x);
		elif os.path.isfile(f):
			if key in f:
				print(x);
		else:
			ff = os.path.split(x)[1];
			if key in ff:
				print(x);

def main():
	print('tst_show_dir-------------------------');
	tst_show_dir();
	print('tst_showall_dir-------------------------');
	tst_showall_dir();
	print('tst_showall_dir2-------------------------');
	tst_showall_dir2();
	print('tst_search_dir-------------------------');
	tst_search_dir('.py');
	
if __name__ == '__main__':
	main();
