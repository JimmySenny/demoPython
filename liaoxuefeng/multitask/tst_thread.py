#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading, time;

def loop():
	print('thread [%s] is running' % threading.current_thread().name);
	n = 0;
	while( n < 5):
		n += 1;
		print('thread [%s] >>> [%s]' % (threading.current_thread().name, n));
		time.sleep(1);
	print('thread [%s] ended' % threading.current_thread().name);

def main():
	print('thread [%s] is running' % threading.current_thread().name);
	t = threading.Thread(target=loop, name='LoopThread');
	t.start();
	t.join();
	print('thread [%s] ended' % threading.current_thread().name);

if __name__ == '__main__':
	main();

	'''
	thread [MainThread] is running
	thread [LoopThread] is running
	thread [LoopThread] >>> [1]
	thread [LoopThread] >>> [2]
	thread [LoopThread] >>> [3]
	thread [LoopThread] >>> [4]
	thread [LoopThread] >>> [5]
	thread [LoopThread] ended
	thread [MainThread] ended
	'''
