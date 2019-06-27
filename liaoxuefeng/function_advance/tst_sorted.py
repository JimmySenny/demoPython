#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main():
	print(sorted([36, 5, -12, 9, -21])); # [-21, -12, 5, 9, 36]
	print(sorted([36, 5, -12, 9, -21], key=abs)); # [5, 9, -12, -21, 36]
	print(sorted(['bob', 'about', 'Zoo', 'Credit'])); # ['Credit', 'Zoo', 'about', 'bob']
	print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)); # ['about', 'bob', 'Credit', 'Zoo']
	print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)); #reverse

if __name__ == '__main__':
	main();
