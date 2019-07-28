#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

def main():
	#连接到SQLite数据库 文件式tst.db 如果文件不存在会自动创建
	conn = sqlite3.connect('tst.db');
	#创建一个Cusor
	cursor = conn.cursor();
	# 执行一条SQL语句，创建user表:
	#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))');
	#继续执行一条SQL语句，插入一条记录:
	'''
	cursor.execute('insert into user (id, name) values (\'1\', \'Python\')');
	cursor.execute('insert into user (id, name) values (\'2\', \'C\')');
	cursor.execute('insert into user (id, name) values (\'3\', \'Java\')');
	'''
	print(cursor.rowcount);
	# 查询记录
	cursor.execute('select * from user where id=?', ('2', ));
	values = cursor.fetchall();
	print(values);
	# 关闭Cursor:
	cursor.close();
	# 提交事务
	conn.commit();
	# 关闭Connection
	conn.close();

if __name__ == '__main__':
	main();
