#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

from collections import Iterable
from collections import Iterator

def main():
	#可以使用isinstance()判断一个对象是否是Iterable对象
	print(isinstance([], Iterable));   #True
	print(isinstance({}, Iterable));   #True
	print(isinstance('abc', Iterable));#True
	print(isinstance((x for x in range(10)), Iterable)); #True

	#可以使用isinstance()判断一个对象是否是Iterator对象
	print(isinstance((x for x in range(10)), Iterator)); #True
	print(isinstance([], Iterator)); #False
	print(isinstance({}, Iterator)); #False
	print(isinstance('abc', Iterator)); #False

	#把list、dict、str等Iterable变成Iterator可以使用iter()函数
	print(isinstance(iter([]), Iterator)); #True
	print(isinstance(iter({}), Iterator)); #True
	print(isinstance(iter('abc'), Iterator)); #True

if __name__ == '__main__':
	main();
	
