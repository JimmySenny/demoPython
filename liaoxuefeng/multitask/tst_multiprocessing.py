#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

def run_proc(name):
	print('Run child process %s:[%s]'%(name, os.getpid()));

if __name__ == '__main__':
	print('Process [%s] start' % os.getpid());
	p = Process( target = run_proc, args=('test', ));
	print('Child process will start');
	p.start(); #启动
	p.join();#等待子进程结束后再继续往下运行
	print('Child process end');


