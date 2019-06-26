#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

def f(x,y):
	return x*10 + y;

def f2(x,y):
	return x/10 + y;

def char2int(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

def str2float(s):
	#lnum = s.split('.');
	#print(lnum);
	#if(len(lnum)>2):
	#	print('ERROR');
	l = len(s);
	try: 
		i = s.index('.');
	except ValueError as e:
		i = -1;

	#print('i',i);
	#print('d',s[i+1:]);

	if(i == 0): # .123 之类
		num_i = 0;
		num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0 - l + i + 1 );
	elif (i == -1):  #123
		num_i = reduce(f,map(char2int, s));
		num_d = 0;
	elif (l - i <= 1): # 123.之类
		num_i = reduce(f,map(char2int, s[:i]));
		num_d = 0;
	else:
		num_i = reduce(f,map(char2int, s[:i]));
		num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0-l + i + 1 );
	
	#print('num[%d][%d]'%(num_i, num_d));
	return num_i + num_d;

def main():
	print(str2float('123.456'));
	print(str2float('0.456'));
	print(str2float('.456'));
	print(str2float('123.'));
	print(str2float('123'));

if __name__ == '__main__':
	main();


'''
def str2float(s):
    def str2int(ns):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ns]
 
    def f(x,y):
        return x*10+y
    resultNum = 0
    numL = s.split('.')
 
    for index,numS in enumerate(numL):
        if index==0:
            resultNum = resultNum + reduce(f,map(str2int,numS))
        else:
            resultNum = resultNum + reduce(f,map(str2int,numS))*pow(10,0-len(numS))
    return resultNum

#利用map和reduce编写一个str2float函数，把字符串‘123.456’转换成浮点数123.456
def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/(10**len(s2))#乘幂
print('\'123.456\'=',str2float('123.456'))

'''
