#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def myodd():
	print('step1');
	yield 1;
	print('step2');
	yield 2;
	print('step3');
	yield 3;


def fib1(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	print(b);
	return 'done1'

def fib2(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b 
		a, b = b, a + b
		n = n + 1

def main():
	L = [ x*x for x in range(10)]; # list
	print(L); 
	G = ( x*x for x in range(10));
	#print(G); #<generator object <genexpr> at 0x7f51d445d870>
	print(next(G));
	print(next(G));
	for g in G:
		print(g);

	o = myodd()
	print(next(o));
	print(next(o));

	print('fib1');
	print(fib1(3));
	print('fib2');
	for x in fib2(3):
		print(x);
	
	g = fib2(3);
	while True:
		try:
			x = next(g);
			print('g:',x);
		except StopIteration as e:
			print('Generator return value:', e.value);
			break;
	

if __name__ == '__main__':
	main();

