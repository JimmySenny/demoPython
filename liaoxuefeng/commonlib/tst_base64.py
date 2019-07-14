#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

sb1 = b'binary\x00string     i\xb7\x1d\xfb\xef\xff'
sb2 = b'YmluYXJ5AHN0cmluZyAgICAgabcd++//'

def tst_standard():
	print(base64.b64encode(sb1));
	print(base64.b64decode(sb2));

def tst_urlsafe():
	print(base64.urlsafe_b64encode(sb1));
	print(base64.urlsafe_b64decode('abce--__'));

def main():
	tst_standard();
	tst_urlsafe();

if __name__ == '__main__':
	main();
