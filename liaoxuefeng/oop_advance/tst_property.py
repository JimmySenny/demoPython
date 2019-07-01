#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	@property #定义读Attribute属性 get_xxx
	def score(self):
		return self._score;

	@score.setter #定义写Attribute属性 set_xxx
	def score(self,value):
		if (not isinstance(value, int)):
			raise ValueError('score must be integer!');
		if (value < 0 or value > 100):
			raise ValueError('score must between 0 ~ 100');
		self._score = value;
	
def main():
	s = Student();
	s.score = 60;
	print(s.score);
	#s.score = -1; #ValueError: score must between 0 ~ 100

if __name__ == '__main__':
	main();

	
