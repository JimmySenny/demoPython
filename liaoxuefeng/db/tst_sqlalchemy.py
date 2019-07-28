#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ORM

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base();

# 定义User对象:
class User(Base):
	# 表的名字:
	__tablename__ = 'user'

	# 表的结构:
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# 初始化数据库连接:
'''
engine = create_engine(
        "mysql+pymysql://root:123456@127.0.0.1:3306/s9day120?charset=utf8",
		max_overflow=0,  # 超过连接池大小外最多创建的连接
		pool_size=5,  # 连接池大小
		pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
		pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
		)
'''
engine = create_engine('mysql+mysqlconnector://root:password@127.0.0.1:3306/rmtdb');
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine);

# 创建session对象:
session = DBSession();
# 创建新User对象:
new_user = User(id='5', name='Bob');
# 添加到session:
session.add(new_user);
new_user = User(id='2', name='Bob');
session.add(new_user);
# 提交即保存到数据库:
session.commit();
# 关闭session:
session.close();
