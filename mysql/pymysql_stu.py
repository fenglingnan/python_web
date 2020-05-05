import pymysql
#python操作mysql模块

conn=pymysql.connect(host='47.107.129.166',port=3306,user='root',passwd='LINxiang@5',db='PYLINK')

print(conn,6666)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)#设置成字典形式光标
#excute执行命令
sql="CREATE TABLE IF NOT EXISTS TEST(id INT,name VARCHAR(20))"
cursor.execute(sql);

# ret=cursor.execute("INSERT INTO TEST VALUES (5,'ALEX'),(6,'ALVIN')")
#ret代表影响行数

res=cursor.execute("SELECT * FROM account")
print(res)
print(cursor.fetchone())
print(cursor.fetchone())
# cursor.scroll(-1,mode='relative')#正数1向下，负数向上,可以设置成0
cursor.scroll(0,mode='absolute')
print(cursor.fetchone())




conn.commit()
cursor.close()
conn.close()