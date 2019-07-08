#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass;

def main():
	print('worker start');
	# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
	QueueManager.register('task_queue');
	QueueManager.register('result_queue');
	server_addr = '127.0.0.1';
	print('Connect to Server: %s' % server_addr);
	# 端口和验证码注意保持与task_master.py设置的完全一致:
	m = QueueManager(address = (server_addr, 15001), authkey=b'abc');
	m.connect();
	task = m.task_queue();
	result = m.result_queue();

	for i in range(10):
		try:
			n = task.get(timeout=1);
			print('run task [%d * %d]' % (n, n ));
			r = '%d * %d = %d' %( n, n, n*n );
			time.sleep(1);
			result.put(r);
		except Queue.Empty:
			print('task queue is empty');
	print('worker done');

if __name__ == '__main__':
	main();





