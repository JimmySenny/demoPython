#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

'''
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
if(re.match(r'正则表达式', str):
	print('match');
else:
	print('failed');
'''

def comp_split():
	s = r'a b   c';
	print('split by \' \':', s.split(' '));
	print('split by re:', re.split(r'\s+', s));

def re_group():
	m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345');
	print('[%s][%s][%s][%s]'%(m, m.group(0), m.group(1), m.group(2)));

def re_compile():
	re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$');
	print(re_telephone.match('010-12345').groups());
	print(re_telephone.match('010-8086').groups());

def main():
	print(re.match( r'^\d{3}\-\d{3,8}$', '010-12345')); #<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
	if (re.match(r'^\d{3}\-\d{3,8}$', '010 12345')):
		print('match');
	else:
		print('nomatch');
	pass;

	comp_split();

	print(re.split(r'[\s\,]+', 'a,b, c  d'));
	print(re.split(r'[\s\,\;]+', 'a,b;; c  d'));

	re_group();

	#贪婪匹配
	print(re.match(r'^(\d+)(0*)$', '102300').groups());
	print(re.match(r'^(\d+?)(0*)$', '102300').groups());

	re_compile();

if __name__ == '__main__':
	main();
