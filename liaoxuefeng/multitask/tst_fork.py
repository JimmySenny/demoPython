#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

def main():
	print('Process [%s] start...'% (os.getpid()));
	pid = os.fork();
	if( pid == 0):
		print('child process [%s], parent is [%s]'%(os.getpid(), os.getppid()));
	else:
		print('parent process [%s], child is [%s]'%(os.getpid(), pid));
	
if __name__ == '__main__':
	main();
