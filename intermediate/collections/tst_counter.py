#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import Counter;

def main():
	colours = (
		( 'Yasoob', 'Yellow' ),
		( 'Ali', 'Blue' ),
		( 'Arham', 'Green' ),
		( 'Ali', 'Black' ),
		( 'Ahmed', 'Silver' ),)

	favs = Counter(name for name, colour in colours);
	print( favs );
	#Counter({'Ali': 2, 'Yasoob': 1, 'Arham': 1, 'Ahmed': 1})
	
	with open( 'filename', 'rb' ) as f:
		line_count = Counter(f);
	print( line_count );



if __name__ == '__main__':
	main();

#defaultdict(<class 'list'>, {'Yasoob': ['Yellow'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})
