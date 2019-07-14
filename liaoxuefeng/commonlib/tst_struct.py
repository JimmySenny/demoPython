#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import struct

def tst_2b():
	n = 10240099;
	b1 = (n & 0xff000000 ) >> 24;
	b2 = (n & 0xff0000 ) >> 16;
	b3 = (n & 0xff00 ) >> 8;
	b4 = (n & 0xff ) >> 0;
	bs = bytes([b1, b2, b3, b4]);
	print(bs);
	
def tst_picture():
	with open('./hp.bmp', 'rb') as fbmp:
		s1 = fbmp.read(30);
	
	with open('./hp.jpg', 'rb') as fjpg:
		s2 = fjpg.read(30);

	with open('./hp.png', 'rb') as fpng:
		s3 = fpng.read(30);

	with open('./hp.gif', 'rb') as fgif:
		s4 = fgif.read(30);
	'''
	file hp*
	hp.bmp: PC bitmap, Windows 3.x format, 1641 x 1094 x 24
	hp.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 192x192, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=5], baseline, precision 8, 1641x1094, frames 3
	hp.png: PNG image data, 1641 x 1094, 8-bit/color RGBA, non-interlaced
	hp.gif: GIF image data, version 89a, 1641 x 1094
	'''
	print(s1);
	print(s2);
	print(s3);
	print(s4);
	'''
	b'BM\x9e2R\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00i\x06\x00\x00F\x04\x00\x00\x01\x00\x18\x00'
	b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00\xc0\x00\xc0\x00\x00\xff\xe1\x00ZExif\x00\x00'
	b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x06i\x00\x00\x04F\x08\x06\x00\x00\x00\xd3'
	b'GIF89ai\x06F\x04\xf7\x00\x00\x00\x00\x00\x00\x003\x00\x00f\x00\x00\x99\x00\x00\xcc\x00\x00'
	'''
	print(struct.unpack('<ccIIIIIIHH', s1)); #(b'B', b'M', 5386910, 0, 54, 40, 1641, 1094, 1, 24)
	print(struct.unpack('>IIIIIIIH', s2)); #
	print(struct.unpack('<IcccccIIIIIc', s3)); #
	print(struct.unpack('<cccccccIIIIIHc', s4)); #

def main():
	tst_2b();
	# I：4字节无符号整数和H：2字节无符号整数
	print(struct.pack('>I', 10240099));
	print(struct.unpack('>I', b'\x00\x9c@c'));
	print(struct.unpack('>HH', b'\x00\x9c@c'));
	tst_picture();

if __name__ == '__main__':
	main();
