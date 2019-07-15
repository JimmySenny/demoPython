#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import hmac

def tst_hmac():
	message = b'hello python!';
	key = b'secret';

	h = hmac.new(key, message, digestmod='MD5');
	print(h.hexdigest()); #22af6ded0a893c5da4f7235936ee047e 

	m1 = b'hello ';
	m2 = b'python!';
	h2 = hmac.new(key, m1, digestmod='MD5');
	h2.update(m2);
	print(h2.hexdigest()); #22af6ded0a893c5da4f7235936ee047e


if __name__ == '__main__':
	tst_hmac();
