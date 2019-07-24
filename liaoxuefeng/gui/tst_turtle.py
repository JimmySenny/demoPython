#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from turtle import *

def main():
	#设置笔刷宽度
	width(4);

	#前进
	forward(200);
	#右转90度
	right(90);

	#笔刷颜色
	pencolor('red');
	forward(200);
	right(90);

	pencolor('green');
	forward(200);
	right(90);

	pencolor('blue');
	forward(200);
	right(90);

	done();

if __name__ == '__main__':
	main();
