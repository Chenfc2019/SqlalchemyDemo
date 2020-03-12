#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sqldemo.py
# @Author: Small-orange
# @Date  : 2020-3-12
# @Desc  : sqlalchemy的使用案例-创建表，添加数据
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

#创建数据库连接
#root:数据库用户名
#123456：密码
#localhost:数据库主机地址
#3306：端口号
#demo01：数据库名称
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/demo01')
#连接到数据库
conn = engine.connect()
#1.通过sql语句创建表
# sql = '''create table user (
#          id int not null primary key,
#          name varchar(50),
#          age int)'''
# #执行sql语句
# conn.execute(sql)

#2.通过ORM的方式创建表
#MetaData类主要用于保存表结构，连接字符串等数据，是一个多表共享的对象
metadata = MetaData(engine) #绑定一个数据源的metadata
#定义表结构,包括表名，上面绑定的数据源metadata和列定义
student = Table('student',metadata,
                Column('id',Integer,primary_key=True),
                Column('name',String(20)),
                Column('score',Integer)
                )
metadata.create_all(engine) #创建表，安全操作，会先判断表是否存在

#向表中添加数据
#对数据库的操作需要通过session来完成
DBsession = sessionmaker(bind=engine)
#sessionmake方法创建一个Session工厂，然后在调用工厂的方法来实例化一个Session对象。
session = DBsession()

Base = declarative_base()

#创建数据表对应的类
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    score = Column(Integer)

#待添加的数据
stu1 = Student(id=1001,name='xiaoming',score=66)
stu2 = Student(id=1002,name='xiaohong',score=86)
stu3 = Student(id=1003,name='xiaofang',score=77)
stu4 = Student(id=1004,name='xiaohua',score=90)
stu5 = Student(id=1005,name='xiaoliang',score=55)

session.add_all([stu1,stu2,stu3,stu4,stu5])#谭家所有数据
session.commit() #提交事务

#查询操作
result = session.query(Student).all()
print('-----查询结果-----')
for stu in result:
    print(stu3)

session.close() #关闭session




