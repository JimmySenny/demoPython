#!/usr/bin/lib python3
# -*- coding:utf-8 -*-

import requests

def tst_get():
	r = requests.get('https://www.baidu.com');
	print(r.encoding);
	print(r.status_code);
	print(r.text.encode('utf-8'));

def tst_params():
	r = requests.get('https://www.baidu.com/s', params={'wd':'python'});
	print(r.url); #https://www.baidu.com/s?wd=python
	print(r.status_code);
	print(r.text.encode('utf-8'));
	print(r.content);

def tst_json():
	r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json');
	print(r.json());

def tst_header():
	 r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}, timeout=3);
	 print(r.text.encode('utf-8'));

def tst_post():
	r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'});
	print(r.status_code);

def tst_cookie():
	cs = {'token':'123456', 'status':'working'};
	r = requests.get('https://www.baidu.com', cookies=cs);
	print(r.status_code);
	#print(r.cookies['status']);


def main():
	#tst_get();
	#tst_params();
	#tst_json();
	tst_header();
	tst_post();
	tst_cookie();

if __name__ == '__main__':
	main();

