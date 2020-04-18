#!/usr/bin/env python3
# -*- conding:utf-8 -*-

import re;

def tst_re():
	#data = r'<section><h2>My IPv4 Address</h2><p id="ipv4"><span class="icon icon-flag-cn" title="Lanzhou, China"></span><a href="https://www.ipaddress.com/ipv4/42.94.221.146" class="ip ipv4">42.94.221.146</a></p></section>'
	#pattern = re.compile(r'<section>.*<a href="https://www.ipaddress.com\/ipv4\/([0-9]{1,3}\.){3}[0-9]{1,3}.*<\/section>');
	with open( './response.html', 'r' ) as f:
		data = f.read();
	pattern = re.compile(r'ipv4\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}');
	ip_addr = re.findall( pattern, data);
	print("ipaddress: [%s]" % ip_addr);

def main():
	tst_re();

if __name__ == '__main__':
	main();
