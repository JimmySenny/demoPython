#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

balance = 0;
lock = threading.Lock()

def change_it(n):
	global balance;
	balance += n
	balance -= n

def run_thread(n):
	for i in range(100000):
		'''
		change_it(n);
		'''
		lock.acquire();
		try:
			change_it(n);
		finally:
			lock.release();

def main():
	global balance;
	t1 = threading.Thread(target=run_thread, args=(5,));
	t2 = threading.Thread(target=run_thread, args=(8,));
	t1.start();
	t2.start();
	t1.join();
	t2.join();
	print(balance);

if __name__ == '__main__':
	main();
