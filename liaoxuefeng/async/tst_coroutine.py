#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Python对协程的支持是通过generator实现的。

def consumer():
	r = '';
	while True:
		n = yield r;
		if not n:
			return;
		print('[CONSUMER] consuming %s ...' % n );
		r = '200 OK';

def produce(c):
	c.send(None);
	n = 0;
	while n < 5:
		n = n + 1;
		print('[PRODUCER] Producing %s ...' % n );
		r = c.send(n);
		print('[PRODUCER] Consumer return:%s ...' % r );
	c.close();

c = consumer();
produce(c);
