#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import chardet

def tst_detect():
	print(chardet.detect(b'hello, python!'));
	data = '离离原上草，一岁一枯荣'.encode('gbk');
	print(chardet.detect(data));
	data_u = '离离原上草，一岁一枯荣'.encode('utf-8');
	print(chardet.detect(data_u));
	data_j = '最新の主要ニュース'.encode('euc-jp');
	print(chardet.detect(data_j));

def main():
	tst_detect();

if __name__ == '__main__':
	main();
