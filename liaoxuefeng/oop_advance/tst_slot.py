#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from types import MethodType

class Student(object):
	pass;

def set_name(self, name): # 定义一个函数作为实例方法
	self.name = name;

def set_score(self, score): # 定义一个函数作为实例方法
	self.score = score;

class Student2(object):
	__slots__ = ( 'name','score' );
	pass;


def main():
	s = Student();
	s2 = Student();
	s.name = 'Python'; # 动态给实例绑定一个属性
	print(s.name); # Python
	s.set_name = MethodType(set_name, s); # 动态给实例绑定一个方法
	s.set_name('Hello World');
	print(s.name); # Hello World
	'''给一个实例绑定的属性和方法，对另一个实例是不起作用的 '''
	#s2.set_name('ABC'); #AttributeError: 'Student' object has no attribute 'set_name'
	#print(s2.name); # AttributeError: 'Student' object has no attribute 'name'
	Student.set_score = set_score;# 为了给所有实例都绑定属性及方法，可以给class绑定
	'''通常情况下，set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。'''
	s.set_score(100);
	s2.set_score(90);
	print(s.score);
	print(s2.score);
	''' __slots__变量，来限制该class实例能添加的属性 '''
	s3 = Student2();
	s3.name = 'ABC';
	s3.score = 99;
	#s3.age = 30; # AttributeError: 'Student2' object has no attribute 'age'

if __name__ == '__main__':
	main();

