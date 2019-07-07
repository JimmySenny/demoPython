#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process, Queue;
import os, time, random;

def write_queue(queue):
	print('Process to Write:%s' % os.getpid());
	for value in ['A', 'B', 'C']:
		print('Put [%s] to Queue' % value);
		queue.put(value);
		time.sleep(random.random());

def read_queue(queue):
	print('Process to Read:%s' % os.getpid());
	while True:
		value = queue.get(True);
		print('Get [%s] from Queue' % value);

def main():
	#父进程创建Queue，并传给各个子进程
	queue = Queue();
	pw = Process(target = write_queue, args = (queue, ));
	pr = Process(target = read_queue, args = (queue, ));
	#启动子进程pw，写入
	pw.start();
	#启动子进程pr，读取
	pr.start();
	#等待pw结束:
	pw.join();
	# pr进程里是死循环，无法等待其结束，只能强行终止:
	pr.terminate();

if __name__ == '__main__':
	main();




