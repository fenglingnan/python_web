create  table TEST1(
    id int,
    name char(18),
    gender enum('male','famale')
);
# enum 在mysql8里必须选一个否则无法插入
create table TEST2(
    id int,
    name char(18),
    hobby set('抽烟','喝酒','烫头','洗脚','按摩')
);
#mysql设置严格模式，就不可对not null插入空值

#set 值必须有一个，可多选（多选会被去重），但是不可插入不存在的数据
#约束某一个字段
#无符号的 int unsigned(unsigned必须在not null之前)
#不能为空 not null
#默认值是什么 default 'val'
#唯一约束 unique(mysql里null可以多个空值)
  # 第一个被定义为非空+唯一的字段会成为这张表的primary-key（一张表只能有一个主键）
  # 唯一约束/联合唯一 unique(几个字段联合起来不能重复)
  # 可以手动指定主键字段
#自增 auto_increament,自带非空约束，至少unique约束之后才能写
#主键
  # 一张表只有一个主键
  # 联合主键primary-key
#外键
create table run(
    id int unsigned not null,
    name char(18)
)
create table uni(
    id int unique auto_increment,
    name char(18)
);
create table t1(
    id int primary key auto_increment,
    user_name char(12) not null,
    sex enum('male','famale') default 'male',
    hobby set('上课','写作业','考试')
);
#增
 #insert into table values ()...
 #insert into table() values ()...
 #insert into table() select () from o_table;
#删
 #delete from table/清空表
  #不会清空自增字段的offset/auto_increament的值未改
 #truncate table table_name
  #会清空offset/修改auto_increament
 #delete from table where
    #先查询再删除数据
#改
 #update table set
#查
 #select、where
#单表数据查询
    #select * from table
    #select (字段名) from table
    #select (field...) as (field...) from table;
    #select distinct (field...) from table
    #select (field(+-*/)四则运算) from employee;
    #select concat(emp_name,':',salary) from employee
    #可使用函数concat/concat_ws
#where 过滤
    #比较运算符
    #范围
        #between and(两个界限都是闭区间)[a,b]格式
        #in
    #模糊匹配
        #like
            #%通配符 任意长度任意内容%的长度可以为0 %string%,可能前后两个匹配长度都为0
            #_通配符 一个字符长度的任意内容employee
         #like降低正则匹配使用频率/盲猜正则匹配引擎速度不如like模糊匹配
        #regexp
    #逻辑运算
        #优先级 not>and>or
#group 分组
    #分组只组的第一个
    #分组一般和聚合函数一起用
#聚合函数 count/计数 max/最大值 min/最小值 sum/求和 avg/平均
#having 过滤
    #在having条件中可使用函数，where中不行
    #适合过滤符合条件的一组数据，而不是一行数据
    #先分组再过滤
#order by 排序(asc/升序,desc/降序)默认升序
#limit m，n不写m，m默认为0
    #limit 2,1 === limit 1 offset 2

#多表查询
    #连表查询
        #表与表之间的连接方式
            #inner join会去掉不匹配的项
            #左/右外连接不会去掉匹配的项
            #union全外连接(大概率不用)
    #子查询
        #in not in
    #exist
        #布尔值
        #如果为false就不执行sql语句


####多表是为了数据去重，减小体积和查询速度