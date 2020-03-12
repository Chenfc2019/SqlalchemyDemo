#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sqldemo02.py
# @Author: Small-orange
# @Date  : 2020-3-12
# @Desc  : sqlalchemy的使用案例-查询

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, or_, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/demo01')

#创建基类，返回一个d定制的metaclass类
Base = declarative_base()

#自定义与表对应的类
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    score = Column(Integer)

    def to_dict(self):
        '''
        将查询结果转化为字典
        :return:
        '''
        return {k: v for k, v in self.__dict__.items() if k != "_sa_instance_state"}

#创建session，用于数据库操作
DBsession = sessionmaker(bind=engine)
session = DBsession()

#查询全部
result = session.query(Student).all()
print('---1.查询全部---')
for i in result:
    #i为Student对象
    if isinstance(i,Student):
        print(i.to_dict())

#查询部分字段
result1 = session.query(Student.id,Student.name).all()
print('---2.查询部分字段---')
for i in result1:
    #i是一个元组
    print(i)

#多条件查询or_和and_
result2 = session.query(Student).filter(or_(Student.name=='xiaoming',Student.score<60))
print('---3.1 多条件查询or_---')
for i in result2:
    if isinstance(i,Student):
        print(i.to_dict)

result3 = session.query(Student).filter(and_(Student.id>=1002,Student.score>60))
print('---3.2 多条件查询and_---')
for i in result3:
    if isinstance(i,Student):
        print(i.to_dict)

#模糊查询
result4 = session.query(Student).filter(Student.name.like('%ming%')).first()
print('---4.模糊查询---')
print(result4.to_dict)

#范围查询
result5 = session.query(Student).filter(Student.id.in_([1001,1003])).all()
print('---5.范围查询---')
for i in result5:
    if isinstance(i,Student):
        print(i.to_dict())

#排序:asc() 升序, desc()降序
result6 = session.query(Student).order_by(Student.score.desc()).all()
print('---5.降序---')
for i in result6:
    if isinstance(i,Student):
        print(i.to_dict())

#限制，limit ， slice
result7 = session.query(Student).order_by(Student.score.desc()).limit(3)
print('---6.1 limit---')
for i in result7:
    if isinstance(i,Student):
        print(i.to_dict())

#slice的范围是前闭后开
result8 = session.query(Student).order_by(Student.score.desc()).slice(3,5)
print('---6.2 slice---')
for i in result8:
    if isinstance(i,Student):
        print(i.to_dict())

#统计
result9 = session.query(Student).filter(Student.score>60).count()
print('---10.统计---')
print(result9)





