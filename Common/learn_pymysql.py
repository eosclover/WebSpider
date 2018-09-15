# import pymysql

#练习pymysql
#通过pymysql的connect()方法声明一个mysql连接对象db
# db=pymysql.connect(host='localhost', #IP
#                    user='root',
#                    password='123456',
#                    port=3306) #端口号为int数字
# #创建游标
# cursor=db.cursor()
# #查看数据库版本
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchone()
# print('Database version:',data)
# cursor.execute("create database spider default character set utf8")
# db.close()



#创建表
# import pymysql
# db=pymysql.connect(host='localhost', #IP
#                    user='root',
#                    password='123456',
#                    port=3306,
#                    db='spider')
# cursor=db.cursor()
# sql='create table if not exists student' \
#     '(id varchar(255) not null,name varchar(255) not null,age int not null,' \
#     'primary key (id))'
# cursor.execute(sql)
#
# db.close()


# #插入数据
# import pymysql
# id='20120001'
# user='Bob'
# age=20
# db=pymysql.connect(host='localhost', #IP
#                    user='root',
#                    password='123456',
#                    port=3306,
#                    db='spider')
# cursor=db.cursor()
# #遇到的问题，第一次执行的时候，table表名与数据库中的不一致，导致执行不成功
# #要学会调试代码，全拼个人摸索
# sql='insert into student(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()


#上面的nsert 操作是通过构造sql语句实现的，很明显，不是很方便，要是早多增一个或多个字段，sql语句句需要更改
# insert into student(id,name,age,gender) values (%s,%s,%s,%s)

# #解决办法：构造动态字典，元祖也动态构造(字段名)
# import pymysql
# db=pymysql.connect(host='localhost', #IP
#                    user='root',
#                    password='123456',
#                    port=3306,
#                    db='spider')
# cursor=db.cursor()
# data={'id':'20120003',
#       'name':'Alice',
#       'age':'20',}
# table='student'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# print(values)
# sql='insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful')
#         db.commit()
# except:
#     print('Faild')
#     db.rollback()
# db.close()













import pymysql
db=pymysql.connect(host='localhost', #IP
                   user='root',
                   password='123456',
                   port=3306,
                   db='spider')
cursor=db.cursor()
data={'id':'20120003',
      'name':'Alice',
      'age':'20',}
table='student'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
print(values)

sql='select * from student where age>=20'
try :
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one=cursor.fetchone()
    print('One:',one)
    result=cursor.fetchall()
    print('Result:',result)
    print('Result type:',type(result))
    for row in result:
        print(row)
except:
    print('Error')