#!/usr/bin/env python3
# -*- conding:utf-8 -*-

from urllib import request;
import chardet;
from urllib import parse;
import urllib.error

#youdao
import time;
import random;
import hashlib;
import json;

header = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" 
};

def urlopen_url():
	response = request.urlopen('https://zhuanlan.zhihu.com/');
	html = response.read();
	charset = chardet.detect(html);
	print(charset);
	#print(html);

def urlopen_request():
	request_url = request.Request('https://zhuanlan.zhihu.com/');
	response = request.urlopen(request_url);
	html = response.read();
	html = html.decode("utf-8");
	print(html);

def urlopen_request_get():
	url = 'https://cn.bing.com/search';
	params = {'q': 'python', };

	#使用parse方法对参数进行URL编码
	encoded_params = parse.urlencode(params);
	request_url = request.Request(url + '?' + encoded_params, headers=header );

	response = request.urlopen(request_url);

	#print( response.read().decode('utf-8'));
	with open('./response.html', 'w' ) as f:
		f.write(response.read().decode('utf-8'));

def urlopen_request_post():
	
	url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule';
	post_data = {
		'i': '你好', 
		'client': 'fanyideskweb',
		'salt': '15853849529172',
		'sign': 'a2b23c118765db72dbb8b1abbcb5e82d'
	};

	# 使用parse方法对参数进行URL编码
	encoded_data = parse.urlencode(post_data).encode('utf-8');
	# 使用urllib发送POST数据无需拼接URL
	request_url = request.Request(url, headers=header, data=encoded_data);
	response = request.urlopen(request_url);

	with open('./response.html', 'w' ) as f:
		f.write(response.read().decode('utf-8'));

def urlopen_request_post_youdao():
	url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule';
	#Form Data
	u = 'fanyideskweb'; # client;
	i = input("Translation Input:" );
	d = i;
	f = str(int(time.time() * 1000 ) + random.randint(1, 10 ) );
	c = 'ebSeFb%=XZ%T[KZ)c(sy!';
	print("slat: %s" % f);

	md5 = hashlib.md5();
	md5.update(u.encode('utf-8'));
	md5.update(d.encode('utf-8'));
	md5.update(f.encode('utf-8'));
	md5.update(c.encode('utf-8'));

	sign = md5.hexdigest();
	print("sign: %s" % sign);
	data = {
		"i": i,
		"from": "AUTO",
		"to": "AUTO",
		"smartresult": "dict",
		"client": "fanyideskweb",
		"salt": f,
		"sign": sign,
		"ts":f,
		"bv": "70244e0061db49a9ee62d341c5fed82a",
		"doctype": "json",
		"version": "2.1",
		"keyfrom": "fanyi.web",
		"action": "FY_BY_REALTIME",
		"typoResult": "false"
	}

	#使用urlencode方法转换标准格式
	encoded_data = parse.urlencode(data).encode('utf-8');
	print("encoded_data %s" % encoded_data );
	request_url = request.Request(url, headers=header, data=encoded_data);

	response = request.urlopen( request_url );

	#if 200 
	responseCode = response.getcode();
	print( responseCode );
	if ( responseCode == 200 ):
		json_result = json.loads( response.read().decode('utf-8') ); #response转换为json
		
		for i, j in json_result.items():
			print(i, j);

		# I:是 
		# {"errorCode", "50"}
		# {"translateResult":[[{"tgt":"is","src":"是"}]],"errorCode":0,"type":"zh-CHS2en","smartResult":{"entries":["","are\r\n","am\r\n","yes\r\n"],"type":1}}"
		transCode = json_result["errorCode"];
		print(transCode);
		if ( transCode == 0 ):
			translation_result = json_result['translateResult'][0][0]['tgt'];
			print("Translation result: [%s]" % translation_result );
		else:
			print("Translation Error" );

	else:
		print("request error");

def urlopen_request_error():
	try:
		request.urlopen('https://www.baidu.com/admin/');
	except urllib.error.HTTPError as e0:
		print(e0.reason);

	try:
		request.urlopen('htt://www.baidu.com');
	except urllib.error.URLError  as e:
		print(e.reason);

def main():
	#urlopen_url();
	#urlopen_request();
	#urlopen_request_get();
	#urlopen_request_post();
	#urlopen_request_post_youdao();
	urlopen_request_error();

if __name__ == '__main__':
	main();
