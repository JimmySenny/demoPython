#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from math import sqrt

def main():
    try:
        height = float(input('Height(m):'));
        weight = float(input('Weight(kg):'));
    except TypeError:
        print('ERROR INPUT');
    finally:
        pass;

    bmi = weight / (height*height);
    print(bmi);
    if (bmi < 18.5):
        print('过轻');
    elif (bmi < 25):
        print('正常');
    elif (bmi < 28):
        print('过重');
    elif (bmi < 32):
        print('肥胖');
    else:
        print('巨肥');
	


if __name__ == '__main__':
    main();


