#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

local_school = threading.local();

def process_student():
	# 获取当前线程的student
	std = local_school.student;
	print('Hello %s-%s'%(std, threading.current_thread().name));

def process_thread(name):
	# 绑定ThreadLocal的student
	local_school.student = name;
	process_student();

def main():
	t1 = threading.Thread(target = process_thread, args=('Python', ), name = 'Thread-A');
	t2 = threading.Thread(target = process_thread, args=('Java', ), name = 'Thread-B');
	t1.start();
	t2.start();
	t1.join();
	t2.join();

if __name__ == '__main__':
	main();
	
