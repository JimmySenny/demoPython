#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector

def main():
	conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='rmtdb');
	#conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='rmtdb', auth_plugin='mysql_native_password');
	cursor = conn.cursor();
	#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))');
	'''
	cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael']);
	print(cursor.rowcount);
	conn.commit();
	cursor.close();
	'''

	#查询
	#cursor = conn.cursor();
	cursor.execute('select * from tb_rmt_user where user_id=%s', ('000', ));
	values = cursor.fetchall();
	print(values);
	cursor.close();
	conn.close();

if __name__ == '__main__':
	main();
