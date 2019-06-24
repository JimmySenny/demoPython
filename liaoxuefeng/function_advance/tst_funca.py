#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def func_add(x,y,f):
	return f(x) + f(y);


def main():
	print(abs(-10));
	print(abs); #abs是函数本身

	f = abs;
	print(f); #函数本身也可以赋值给变量
	print(f(-10)); #通过函数赋值给的变量调用这个函数

	#abs = 10; #函数名其实就是指向函数的变量
	#print(abs(-10));

	print(func_add(-1,-2,abs)); #一个函数就可以接收另一个函数作为参数


if __name__ ==  '__main__':
	main();
