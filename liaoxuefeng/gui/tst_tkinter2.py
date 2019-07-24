#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter

def main():
	a = tkinter.Tk();
	a.title('Hello Python Tkinter');
	label = tkinter.Label(a, text='H P T');
	label.pack();
	tkinter.mainloop();

if __name__ == '__main__':
	main();
