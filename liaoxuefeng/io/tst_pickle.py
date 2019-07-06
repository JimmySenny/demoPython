#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle
import json

d = dict(name='Python', age=20, score=90);
class Student(object):
	def __init__(self, name, age, score):
		self.name = name;
		self.age = age;
		self.score = score;

	def __str__(self):
		return 'NAME:[%s] AGE:[%s], SCORE[%s]' %(self.name, self.age, self.score);
	__repr__ = __str__;
	
s = Student('JSON', 30, 99);

def student2dict(std):
	return { 'name':std.name,
			 'age':std.age,
			 'score':std.score};
def dict2student(d):
	return Student(d['name'], d['age'], d['score']);

def tst_pickle():
	print('pickle.dumps()',pickle.dumps(d)); # 任意对象序列化为 bytes
	with open('./pickle.dump', 'wb') as f1:
		pickle.dump(d,f1); #把对象序列化后写入一个file-like Object
	
	with open('./pickle.dump', 'rb') as f2:
		#print(f2.read());
		dr = pickle.load(f2); #从一个file-like Object中直接反序列化出对象
		print(dr);

def tst_json():
	print('json.dumps()', json.dumps(d));
	with open('./json.dump', 'w') as f1:
		json.dump(d, f1);

	with open('./json.dump', 'r') as f2:
		dr = json.load(f2);
		print(dr);
	
def tst_json2():
	#print('tst2:json.dumps()', json.dumps(s)); 
	#TypeError: <__main__.Student object at 0x7f35650b6d30> is not JSON serializable

	#可选参数default就是把任意一个对象变成一个可序列为JSON的对象
	#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
	print('default:json.dumps()', json.dumps(s, default=student2dict));

	#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量 也有少数例外，比如定义了__slots__的class
	print('default2:json.dumps()', json.dumps(s, default=lambda obj: obj.__dict__));

	#object_hook函数负责把dict转换为Student实例
	json_str = '{"age": 20, "score": 88, "name": "Bob"}';
	print('json.loads()', json.loads(json_str, object_hook=dict2student));

	
def main():
	tst_pickle();
	tst_json();
	tst_json2();

if __name__ == '__main__':
	main();

