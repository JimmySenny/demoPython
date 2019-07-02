#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Field(object):
	def __init__(self, name, column_type):
		self.name = name;
		self.column_type = column_type;
	
	def __str__(self):
		return '<%s:%s>' %(self.__class__.__name__, self.name);

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)');

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint');

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs): #attrs是包含所有元素和方法的字典
		if (name == 'Model'): #如果当前创建对象为Model的实例则不做操作(因为Model没有属性 做了也白做)
			return type.__new__(cls, name, bases, attrs);
		print('Found model: %s' % name); #打印当前实例的类名称
		mappings = dict(); #创建一个空的字典
		for k, v in attrs.items(): #attrs应该是存放了类的所有属性以及方法的字典,我的理解是在python中一切都是对象. 方法的类型为<class 'function'> 值为形如<function aaa at 0x10e4839d8>的内存地址.可以理解为方法是一个function的实例.这里k是属性或方法的类型,v是属性或方法的值
			if isinstance(v, Field):  #如果v是Field的实例对象
				print('Found mapping: %s ==> %s' %(k, v)); #
				mappings[k] = v; #将其添加到mappings字典中
		for k in mappings.keys(): #最后遍历mappings,从attrs中pop
			attrs.pop(k);
		#最后正在创建的对象 添加两个属性  __mappings__和 __table__
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name; #假设表名和类名一致
		return type.__new__(cls, name, bases, attrs);

class Model(dict, metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw);

	def __getattr__(self, key):
		try:
			return self[key];
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key);

	def __setattr__(self, key, value):
		self[key] = value;
	
	def save(self):
		fields = [];
		params = [];
		args = [];
		for k, v in self.__mappings__.items():
			fields.append(v.name);
			params.append('?');
			args.append(getattr(self, k, None));
		sql = 'insert into %s (%s) values (%s)' %(self.__table__, ','.join(fields), ','.join(params));
		print('SQL:[%s]' % sql);
		print('ARGS:[%s]' % str(args));

class User(Model):
	# 定义类的属性到列的映射：
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')

def main():
	u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd');
	u.save();
	'''
	Found model: User
	Found mapping: id ==> <IntegerField:id>
	Found mapping: email ==> <StringField:email>
	Found mapping: name ==> <StringField:username>
	Found mapping: password ==> <StringField:password>
	SQL:[insert into User (password,id,email,username) values (?,?,?,?)]
	ARGS:[['my-pwd', 12345, 'test@orm.org', 'Michael']]
	'''

if __name__ == '__main__':
	main();

