#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request

with request.urlopen(r'https://www.baidu.com') as f:
	data = f.read();
	print('Status:', f.status, f.reason);
	for k, v in f.getheaders():
		print('%s:%s'%(k, v));
	print('Data:', data.decode('utf-8'));

req = request.Request(r'https://www.baidu.com/');
req.add_header('User-Agent', r'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25');
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason);
	for k, v in f.getheaders():
		print('%s:%s'%(k, v));
	print('Data:', data.decode('utf-8'));
