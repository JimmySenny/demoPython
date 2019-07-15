#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib

def tst_md5():
	md5a = hashlib.md5();
	md5a.update('how to use md5 in python hashlib?'. encode('utf-8'));
	print(md5a.hexdigest()); #d26a53750bc40b38b65a520292f69306

	md5b = hashlib.md5();
	md5b.update('how to use md5 ' . encode('utf-8'));
	md5b.update('in python hashlib?'. encode('utf-8'));
	print(md5b.hexdigest()); #d26a53750bc40b38b65a520292f69306
	
def tst_sha1():
	sha1a = hashlib.sha1();
	sha1a.update('how to use sha1 in python hashlib?'. encode('utf-8'));
	print(sha1a.hexdigest()); #2c76b57293ce30acef38d98f6046927161b46a44

	sha1b = hashlib.sha1();
	sha1b.update('how to use sha1 ' . encode('utf-8'));
	sha1b.update('in python hashlib?'. encode('utf-8'));
	print(sha1b.hexdigest()); #2c76b57293ce30acef38d98f6046927161b46a44

def main():
	tst_md5();
	tst_sha1();

if __name__ == '__main__':
	main();
