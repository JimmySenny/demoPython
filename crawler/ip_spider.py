#!/usr/bin/env python3
# -*- conding:utf-8 -*-

from urllib import request;
import re

header = {
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" 
};

def ip_spider():
	url = 'https://www.ipaddress.com/';
	#request_url = request.Request(url.headers=header);

	response = request.urlopen(request.Request(url, headers=header));

	responseCode = response.getcode();
	print( responseCode );
	if ( responseCode == 200 ):
		html = response.read().decode("utf-8");
#		with open('./response.html', 'w' ) as f:
#			f.write(html);
		#<section><h2>My IPv4 Address</h2><p id="ipv4"><span class="icon icon-flag-cn" title="Lanzhou, China"></span><a href="https://www.ipaddress.com/ipv4/42.94.221.146" class="ip ipv4">42.94.221.146</a></p></section>
		#pattern = re.compile(r'<section>.*<a href="https://www.ipaddress.com\/ipv4\/([0-9]{1,3}\.){3}[0-9]{1,3}.*<\/section>');
		pattern = re.compile(r'ipv4\/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}');
		#pattern = re.compile(r'ipv4\##/(\d{1,3}\.){3}\d{1,3}');
		ip_addr = re.findall( pattern, html );

		print("ipaddress: [%s]" % ip_addr);
	else:
		print("ipaddress.com request error");


def main():
	ip_spider();

if __name__ == '__main__':
	main();
