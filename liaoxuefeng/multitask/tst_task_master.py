#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

#任务队列
task_queue = queue.Queue();
#结果队列
result_queue = queue.Queue();

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
	pass;

def main():
	print('master start');
	#把两个Queue都注册到网络上, callable参数关联了Queue对象:
	QueueManager.register('task_queue', callable = lambda:task_queue);
	QueueManager.register('result_queue', callable = lambda:result_queue);
	## 绑定端口15001, 设置验证码'abc':
	manager = QueueManager( address=('', 15001), authkey=b'abc');
	manager.start();
	# 获得通过网络访问的Queue对象: 在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.task_queue()获得的Queue接口添加。
	qt = manager.task_queue();
	qs = manager.result_queue();

	# 放几个任务进去:
	for i in range(10):
		n = random.randint(0, 10000);
		print('Put task %d' % n );
		qt.put(n);
		#time.sleep(random.randint(10, 1000));
	
	for i in range(10):
		r = qs.get(timeout= 10);
		print('Result:[%s]'% r );

	manager.shutdown();
	print('master done');

if __name__ == '__main__':
	main();
