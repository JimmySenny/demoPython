#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import defaultdict;
import collections;
import json;

def error():
	some_dict = {};
	some_dict['colours']['favourite'] = 'yellow';

def right():
	tree = lambda:collections.defaultdict(tree);
	some_dict = tree();
	some_dict['colours']['favourite'] = 'yellow';
	print(some_dict);
	print('-----------------------------------');
	print(json.dumps(some_dict));

def main():
	colours = (
		( 'Yasoob', 'Yellow' ),
		( 'Ali', 'Blue' ),
		( 'Arham', 'Green' ),
		( 'Ali', 'Black' ),
		( 'Ahmed', 'Silver' ),)

	favourite_colours = defaultdict(list);

	for name, colour in colours:
		favourite_colours[name].append(colour);

	print(favourite_colours);
	print('-----------------------------------');
	#error(); KeyError: 'colours'
	right();


if __name__ == '__main__':
	main();

#defaultdict(<class 'list'>, {'Yasoob': ['Yellow'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})
