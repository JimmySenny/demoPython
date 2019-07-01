#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	__slots__ = ('_name');
	
	def __init__(self, name='student'):
		self._name = name;

	def __str__(self):
		return 'Fib object (name = [%s])' % self._name;
	
	__repr__ = __str__;

class Fib(object):
	__slots__ = ('_a', '_b');

	def __init__(self):
		self._a, self._b = 0, 1; 
	
	'''
	如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
	该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
	直到遇到StopIteration错误时退出循环。
	'''
	def __next__(self):
		self._a, self._b = self._b, self._a + self._b;
		if (self._a > 10):
			raise StopIteration; # 循环结束条件
		return self._a;

	def __iter__(self):
		return self; # 实例本身就是迭代对象，故返回自己

	def __getitem__(self, n):
		if ( isinstance(n, int)): #n 是索引
			a, b = 1, 1;
			for x in range(n):
				a, b = b, a+b;
			return a;
		if ( isinstance(n, slice)):#ns 是切片
			start = n.start;
			stop = n.stop;
			if start is None:
				start = 0;
			a, b = 1, 1;
			l = [];
			for x in range(stop):
				if x >= start:
					l.append(a);
				a, b =  b, a + b;
			return l;


def main():
	print('student------------------');
	print(Student('Python'));
	s = Student();
	print(s);
	print('fib----------------------');
	for n in Fib():
		print(n);

	f = Fib();
	print('f[3]', f[3]);
	print('f[2:5]', f[2:5]);


if __name__ == '__main__':
	main();

	

