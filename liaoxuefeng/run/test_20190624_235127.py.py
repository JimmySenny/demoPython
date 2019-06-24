# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    def f(x,y):
        return x*10 + y;

    def char2int(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];


    l = len(s);
    try:
        i = s.index('.');
    except ValueError as e:
        i = -1;
    if(i == 0): # .123 之类
        num_i = 0;
        num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0 - l + i + 1 );
    elif (i == -1):  #123
        num_i = reduce(f,map(char2int, s));
        num_d = 0;
    elif (l - i == 1): # 123.之类
        num_i = reduce(f,map(char2int, s[:i]));
        num_d = 0;
    else:
        num_i = reduce(f,map(char2int, s[:i]));
        num_d = reduce(f,map(char2int,s[i+1:]))*pow(10, 0-l + i + 1 );

    return num_i + num_d;


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
