import pymysql
#python操作mysql模块

conn=pymysql.connect(host='47.107.129.166',port=3306,user='root',passwd='LINxiang@5',db='PYLINK')

# print(conn,6666)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)#设置成字典形式光标
#execute执行命令


#查/查不用commit
sql="CREATE TABLE IF NOT EXISTS TEST(id INT,name VARCHAR(20))"
cursor.execute(sql);
# ret=cursor.execute("INSERT INTO TEST VALUES (5,'ALEX'),(6,'ALVIN')")
#ret代表影响行数

#注意此时是光标位置，移动光标会影响最终结果
#光标效果类似yield迭代器效果（读取文件可参考此效果，使用yield迭代减少内存消耗，增加速度）
res=cursor.execute("SELECT * FROM account")
print(cursor.rowcount)
def run_yidld():
    for i in range(cursor.rowcount):
        ret=yield cursor.fetchone()
        print(ret)
test=run_yidld()
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
# print(res)
# print(cursor.fetchone())
# print(cursor.fetchone())
# # cursor.scroll(-1,mode='relative')#正数1向下，负数向上,可以设置成0
# cursor.scroll(0,mode='absolute')
# print(cursor.fetchone())
# cursor.scroll(0,mode='absolute')
# print(cursor.fetchmany(10),type(cursor.fetchmany(10)))
# print(cursor)


#增/删/改
# try :
#     cursor.execute("INSERT INTO account values (6,'我是来自己pymysql',5000)");
#     cursor.execute('UPDATE account SET balance=6000 WHERE id=5 ');
#     cursor.execute('DELETE FROM account WHERE id=6');
#     conn.commit()#提交
# except Exception as e:
#     print(e)
#     conn.rollback()#出错回滚

#sql注入  字符串结尾有带;--
#sql中的-- 表示注释后面的语句
#加入 or 1=1;--直接注入
#参数拼接使用execute函数来
"""
    sql='select * from account where user=%s and password=%s'
    cursor.execute(sql,(user,password))
"""


cursor.close()
conn.close()