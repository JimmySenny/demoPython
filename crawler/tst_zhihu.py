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
    with open( 'zhihu.html', 'w' ) as f:
        f.write( html.text );

    s = etree.HTML( html.text )
#    question_title = s.xpath( '/html/body/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div[1]/h1' );
#    question_content = s.xpath( '//*[@id="root"]/div/main/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/span');
    question_title = s.xpath( '//*[@class="QuestionHeader-title"]/text()')[0];
    question_content = s.xpath( '//*[@class="RichText ztext"]/text()')[0];

    print( question_title );
    print( question_content );


def main():
    url = 'https://www.zhihu.com/question/21358581';
    data = get_request( url );

if __name__ == '__main__':
    main();
