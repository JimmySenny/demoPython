#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import wraps

class logit(object):
	def __init__(self, logfile='logit.log'):
		self.logfile = logfile;

	def __call__(self, func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + " was called";
			with open(self.logfile, 'w') as opend_file:
				opend_file.write(log_string + '\n');
			self.notify();
			return func(*args, **kwargs);
		return wrapped_function;

	def notify(self):
		pass;

@logit()
def myfunc1():
	pass

myfunc1();
#outputs: myfunc1 was called
#		: logit.log

class email_logit(logit):
	'''
	一个logit的实现版本，可以在函数调用时发送email给管理员
	'''
	def __init__(self, email='jimmysheng128@126.com', *args, **kwargs):
		self.email = email;
		super(email_logit, self).__init__(*args, **kwargs);

	def notify(self):
		#发送一封邮件到self.email
		print('send email');
		pass;

@email_logit()
def myfunc2():
	pass

myfunc2();
#outputs: send email
#		: myfunc1 was called
#		: logit.log
