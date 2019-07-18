#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from urllib import request, parse
import sys

#Get抓取url内容
def tst_get1():
	with request.urlopen(r'https://www.baidu.com') as f:
		data = f.read();
		print('Status:', f.status, f.reason);
		for k, v in f.getheaders():
			print('%s:%s'%(k, v));
		print('Data:', data.decode('utf-8'));

#Get模拟浏览器发送Get请求
def tst_get2():
	req = request.Request(r'https://www.baidu.com/');
	req.add_header('User-Agent', r'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25');
	with request.urlopen(req) as f:
		print('Status:', f.status, f.reason);
		for k, v in f.getheaders():
			print('%s:%s'%(k, v));
		#print('Data:', f.read().decode('utf-8'));

#以POST发送一个请求
def tst_post():
	print('login to weibo');
	email = input('Email:');
	passwd = input('Password:');
	Login_data = parse.urlencode([
		('username', email),
		('password', passwd),
		('entry', 'mweibo'),
		('client_id', ''),
		('savestate', '1'),
		('ec', ''),
		('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
		]);
	req = request.Request('https://passport.weibo.cn/sso/login');
	req.add_header('Origin', 'https://passport.weibo.cn');
	req.add_header('User-Agent', r'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25');
	req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F');
	with request.urlopen(req, data=Login_data.encode('utf-8')) as f:
		print('Status:', f.status, f.reason);
		for k, v in f.getheaders():
			print('%s:%s'%(k, v));
		print('Data:', f.read().decode('utf-8'));
	
#通过一个Proxy去访问网站
def tst_handler():
	proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
	proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
	proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
	opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
	with opener.open('http://www.example.com/login.html') as f:
	    pass

def main():
	#tst_get1();
	print(sys.getdefaultencoding());
	#tst_get2();
	tst_post();

if __name__ == '__main__':
	main();
