#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#模拟内置函数 abs()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def main():
	my_abs(33);
	my_abs('aa');
	

if __name__ == '__main__':
	main();
