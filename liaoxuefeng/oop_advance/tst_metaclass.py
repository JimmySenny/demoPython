#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s.' % name);

def fn(self, name='Python'):
	print('Hello, %s.' % name);

'''
示例：metaclass可以给我们自定义的MyList增加一个add方法
'''

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value:self.append(value);
		return type.__new__(cls, name, bases, attrs);

#当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
#在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
	pass;


def main():
	h = Hello();
	h.hello(); #Hello, world.
	print(type(Hello)); #<class 'type'>
	print(type(h)); #<class '__main__.Hello'>
	'''通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义'''
	Hello2 = type('Hello', (object,), dict(hello=fn)); #创建Hello2 class 注意object, 
	h2 = Hello2();
	h2.hello(); #Hello, Python.
	print(type(Hello2)); #<class 'type'>
	print(type(h2)); # <class '__main__.Hello'>

	L = MyList();
	L.add(1);
	L.add(3);
	L.add(5);
	print(L); #[1, 3, 5] 而普通的list没有add()方法：

if __name__ == '__main__':
	main();

