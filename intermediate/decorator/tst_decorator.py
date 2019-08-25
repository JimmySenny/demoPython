#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def tst_decorator(func):
	def wrapTheFunction():
		print("doing some boring work before executing func()");
		func();
		print("doing some boring work after executing func()");
	return wrapTheFunction;

def function_requiring_decoration():
	print("function which needs some decoration to remve my foul smell");

function_requiring_decoration();
#outputs: "function which needs some decoration to remve my foul smell"

function_requiring_decoration = tst_decorator(function_requiring_decoration);

function_requiring_decoration();
#outputs: "doing some boring work before executing func()"
#		: "function which needs some decoration to remve my foul smell"
#		: "doing some boring work after executing func()"

@tst_decorator
def function_requiring_decoration2():
	print("Hey you! Decorate me");

function_requiring_decoration2();
#outputs: "doing some boring work before executing func()"
#		: "Hey you! Decorate me"
#		: "doing some boring work after executing func()"

#the @tst_decorator is just a short way of saying:
#function_requiring_decoration2 = tst_decorator(function_requiring_decoration2)

print( function_requiring_decoration2.__name__ );
#outputs: wrapTheFunction

from functools import wraps

def new_decorator(func):
	@wraps(func)
	def wrapTheFunction():
		print("doing some boring work before executing func()");
		func();
		print("doing some boring work after executing func()");
	return wrapTheFunction;

@new_decorator
def function_requiring_decoration3():
	print("Hey you! Decorate me");

print( function_requiring_decoration3.__name__ );
#outputs: function_requiring_decoration3
	
		
