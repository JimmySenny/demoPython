#!/usr/bin/env python3
# -*- conding:utf-8 -*-

import chardet;
import requests;

#youdao
import time;
import random;
import hashlib;
import json;

header = { 
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36))"
};


def get_json( url, num ):
    params = {
            'p':str( num ), 
            };

    url = url + str( num );
    print( url, num );

    try:
        html = request.get( url, params = params, headers=headers );
        return html.json();
    except BaseException:
        print( "open url error ..." );

def main():
    for i in range(112):
        url = 'https://www.bilibili.com/video/BV164411b7dx?p=';
        num = i;

        html = get_json( url, num );
        print( html );
        '''
        infos = html['data']['items'];

        for info in infos:
            title = info['item']['description'];
            video_url = info['item']['video_playurl'];

            print(title);
        '''

if __name__ == '__main__':
    main();
