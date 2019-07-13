#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict

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

def main():
	tst_namedtuple();
	tst_deque();
	tst_defaultdict();
	tst_OrderedDict();
	
if __name__ == '__main__':
	main();
