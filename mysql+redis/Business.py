#mysql事务
#适合更改后的数据和更改前的数据有关系时，开启事务
#事务会产生行级锁
"""
    BEGIN;
    for update;
    COMMIT;
"""
import pymysql
conn=pymysql.connect(host='47.107.129.166',port=3306,user='root',passwd='LINxiang@5',db='PYLINK')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute('BEGIN');
id=1
balance=5000
sql="SELECT * FROM account WHERE id=%s FOR UPDATE"
res_sql="UPDATE account SET balance=%s WHERE id=%s"
cursor.execute(sql,(id));
cursor.execute(res_sql,(balance,id))
cursor.execute('COMMIT');