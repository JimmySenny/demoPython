#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse

# namedtuple('名称', [属性list]):
def tst_namedtuple():
	Point = namedtuple('Point', ['x', 'y']);
	p = Point(1,2);
	print('p.x[%d] p.y[%d]' %(p.x, p.y));
	print(isinstance(p, Point)); # True
	print(isinstance(p, tuple)); # Ture  

# append() pop() appendleft() popleft()
def tst_deque():
	q = deque(['a', 'b', 'c']);
	q.append('1');
	q.appendleft('2');
	print(q);

def tst_defaultdict():
	dd = defaultdict(lambda: 'N/A');
	dd['key1'] = 'abc';
	print(dd['key1']); #abc
	print(dd['key2']); #N/A
	
def tst_OrderedDict():
	d = dict([('a', 1), ('c', 2), ('b', 3)]);
	od = OrderedDict([('a', 1), ('c', 2), ('b', 3)]);
	print(d);
	print(od); #OrderedDict([('a', 1), ('c', 2), ('b', 3)])

# 构造缺省参数
defaults = {
	'color':'red',
	'user':'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
# 先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数
combined = ChainMap(command_line_args, os.environ, defaults)

def tst_ChainMap():
	print('color=%s' % combined['color']); 
	print('user=%s' % combined['user']); 

def tst_Counter():
	c = Counter();
	for ch in 'Hello Python!':
		c[ch] += 1;
	print(c);#Counter({'l': 2, 'o': 2, ' ': 1, 'P': 1, 'e': 1, 'h': 1, 'H': 1, 't': 1, 'n': 1, 'y': 1, '!': 1})

def main():
	tst_namedtuple();
	tst_deque();
	tst_defaultdict();
	tst_OrderedDict();
	tst_ChainMap();
	tst_Counter();
	
if __name__ == '__main__':
	main();
