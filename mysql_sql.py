import mysql.connector
print('------------------------------------连接数据库---------------------------------------------')

try:
    con = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='vertrigo',
        port=3306,
        database='mysql',
        charset='utf8',
        buffered=True)
    print('数据库连接成功')
    cursor = con.cursor()     # 获取游标，很关键
except mysql.connector.Error as e:
    print('数据库连接失败', str(e))
    
print('------------------------------------建表-------------------------------------------')

'''
# 建表，了解即可
sql_create_table='CREATE TABLE `student` \
(`id` int(10) NOT NULL AUTO_INCREMENT,\
`name` varchar(10) DEFAULT NULL,\
`age` int(3) DEFAULT NULL,\
PRIMARY KEY (`id`)) \
ENGINE=MyISAM DEFAULT CHARSET=utf8'
# ENGINE=INNODB DEFAULT CHARSET=utf8'

try:
    cursor.execute(sql_create_table)
    print('创建表成功！')
except mysql.connector.Error as e:
    print('创建表失败！', str(e))
'''

print('-----------------------------------插入数据--------------------------------------------')

# 备注：如果表引擎为Innodb，执行完成后需执行commit进行事务提交
    # con.commit()
    # cursor.execute('commit')

# try:
    # 第一种，直接字符串插入方式
    # sql_insert1 = "insert into student(name,age) values('xiaoqiang',20)"
    # cursor.execute(sql_insert1)
    # print('插入第一条数据成功')
    
    # 第二种，元组插入方式
    # 此处的%s为占位符，而不是格式化字符串，所以age用%s
    # sql_insert2 = "insert into student(name,age) values(%s,%s)"
    # data = ('testing', 18)
    # cursor.execute(sql_insert2, data)
    # print('插入第二条数据成功')
    
    # 一次插入多条语句，效率比一条条插高
    # stmt = 'insert into student(name,age) values(%s,%s)'
    # data = [('xiaoqiang1', 21), ('xiaoqiang2', 22), ('xiaoqiang3', 21)]
    # cursor.executemany(stmt, data)  # 这里是 executemany
    # print('插入多条成功')
    
# except mysql.connector.Error as e:
#     print('插入数据报错', str(e))
    
# finally:
#     cursor.close()  # 游标的关闭
#     con.close()  # 链接的关闭

print('----------------------------------查询-------------------------------------------')

try:
    sql_query1 = 'select id,name from student where age > %s'
    data = (20,)  # 固定格式，记住就可以了，因为只有一个占位
    cursor.execute(sql_query1, data)
    values = cursor.fetchall()
    print('所有数据：', values)   # 返回的是一个list的形式，里面是元组

    sql_query2 = 'select * from student'
    cursor.execute(sql_query2)
    result1 = cursor.fetchone()
    print('返回1条数据', result1)   # 一条数据，元组的形式返回

    result2 = cursor.fetchone()[0]  # 加[0]代表返回第一个字段
    print('返回第1个字段', result2)   # 因为上面已经执行了一条，所以游标变化到第二条数据

    result3 = cursor.fetchmany(3)  # 只返回了3条数据，列表的形式返回
    print('返回3条数据', result3)

except mysql.connector.Error as e:
    print('查询错误', str(e))

finally:
    cursor.close()
    con.close()

print('-----------------------------------删除--------------------------------------------')

'''
# 删除 (了解)
cursor=con.cursor()
try:
    sql_delete='delete from student where name=%s and age < %s'
    data = ('testing',25)
    cursor.execute(sql_delete,data)
except mysql.connector.Error as e:
    print('删除错误',str(e))
    
finally:
    cursor.close()
    con.close() 
'''
