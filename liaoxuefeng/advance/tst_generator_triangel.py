#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

# generator 
def triangles():
	L = [1];
	while True:
		yield L;
		L = [L[x]+L[x+1] for x in range(len(L) - 1) ];
		L.insert(0,1);
		#L.insert(-1,1);
		L.append(1);

def main():
	n = 0;
	results = [];
	for t in triangles():
		print(t);
		results.append(t);
		n += 1;
		if (n == 10):
			break;
	
if __name__ == '__main__':
	main();
