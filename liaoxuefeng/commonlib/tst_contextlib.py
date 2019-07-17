#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from contextlib import contextmanager

class Query(object):
	def __init__(self, name):
		self._name = name;

	def __enter__(self):
		print('Begin');
		return self;

	def __exit__(self, exc_type, exc_value, traceback):
		if(exc_type):
			print('Error');
		else:
			print('End');

	def query(self):
		print('Query info about %s' %self._name);

class Query2(object):
	def __init__(self, name):
		self._name = name;

	def query(self):
		print('Query info about %s' %self._name);

@contextmanager
def create_query(name):
	print('Begin');
	q = Query(name);
	yield q;
	print('End');

@contextmanager
def tag(name):
	print('<%s>' % name);
	yield;
	print('</%s>' % name);

def main():
	with Query('Python') as q:
		q.query();

	with create_query('Python3') as q2:
		q2.query();

	with tag('root'):
		print('hello');
		print('python');

if __name__ == '__main__':
	main();

