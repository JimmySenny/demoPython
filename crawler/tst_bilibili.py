#!/usr/bin/env python3
# -*- conding:utf-8 -*-

import requests;
from lxml import etree


import chardet;

#youdao
import time;
import random;
import hashlib;
import json;

requestHeaders = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36))"
};


def get_request( url, num = 0 ):
    print( url, num );

    html = requests.get( url=url, headers=requestHeaders );
    with open( 'bilibili.html', 'w' ) as f:
        f.write( html.text );

    s = etree.HTML( html.text )
    #/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/a
#    spread_module = s.xpath( '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/text()' );
#    spread_module = s.xpath( '//*[@class="spread-module"]//@href' );
#    question_content = s.xpath( '//*[@class="RichText ztext"]/text()')[0];

#    for i in spread_module:
#        print( i.text );
#    print( question_content );


def main():
    url = 'https://www.bilibili.com/v/technology/finance/#/all/coin';
    data = get_request( url );

if __name__ == '__main__':
    main();
