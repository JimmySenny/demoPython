#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests;
#import lxml #import etree;


headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" 
};

def tst_geturl(sub_url):
	url = 'https://i3wm.org/docs/offset={sub_url}';
	print(url);
	r = requests.get(url, headers=headers);
	print(r)
	return r.text;

def tst_parse(text):
	html = lxml.etree.HTML(text);
	html.xpath();

def main():
	tst_geturl("userguide.html");

if __name__ == '__main__':
	main();
