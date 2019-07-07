#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Pool;
import os;
import time;
import random;

def long_time_task(name):
	print('Run task %s:[%s]' %(name, os.getpid()));
	start = time.time();
	time.sleep(random.random()*3);
	end = time.time();
	print('Task %s runs %0.2f seconds'%(name, (end-start)));

if __name__ == '__main__':
	print('Process [%s]'%os.getpid());
	p = Pool(4);
	for i in range(5):
		p.apply_async(long_time_task, args=(i, ));
	print('Waiting for all subprocess done');
	p.close(); #调用close()之后就不能继续添加新的Process了
	p.join(); #对Pool对象调用join()方法会等待所有子进程执行完毕 之前必须先调用close()
	print('All subprocess done');
	'''	
	task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制
	由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
	'''	