CREATE TABLE employee(

    `id` TINYINT AUTO_INCREMENT,
    `name` VARCHAR(25),
    `gender` boolean,
    `age` INT,
    `department` VARCHAR(20),
    `salary` DOUBLE(7,2),
    PRIMARY KEY(`id`)

)
INSERT INTO user (name,salary,depart) values ('阿祥',20000,'技术')
mysql 执行顺序 from where select group by having order by
分组过滤不能使用where 用having
count(*)统计所有行,count(字段)不统计null
CREATE TABLE ClassCharger_new(

       id TINYINT PRIMARY KEY auto_increment,
       name VARCHAR (20),
       age INT ,
       is_marriged boolean

);
INSERT INTO ClassCharger_new (name,age,is_marriged) VALUES ("冰冰",12,0),
                                                       ("丹丹",14,0),
                                                       ("歪歪",22,0),
                                                       ("姗姗",20,0),
                                                       ("小雨",21,0);
如果设置自增id，会从1开始，不会从0开始（插入记录未设置id）
CREATE TABLE Student(

       id INT  auto_increment,
       name VARCHAR (20),
       charger_id TINYINT,
       PRIMARY KEY (id)



) ENGINE=INNODB;
INSERT INTO S3 (name,charger_id) VALUES
                                            ("alvin2",4),
                                            ("alvin3",1),
                                            ("alvin4",3),
                                            ("alvin5",1),
                                            ("alvin6",3);
CREATE TABLE Student2(

       id INT  auto_increment,
       name VARCHAR (20),
       charger_id TINYINT,
       PRIMARY KEY (id),
       FOREIGN KEY (charger_id) REFERENCES ClassCharger(id)


) ENGINE=INNODB;
CREATE TABLE S3(

       id INT  auto_increment,
       name VARCHAR (20),
       charger_id TINYINT,
       PRIMARY KEY (id),
       FOREIGN KEY (charger_id) REFERENCES CCV(id) on DELETE CASCADE(这里可以设置成SET NULL)


) ENGINE=INNODB;
被关联的表叫主表
ALTER TABLE Student  ADD CONSTRAINT abc
                     FOREIGN KEY(charger_id)
                     REFERENCES  ClassCharger(id);
--外键约束对子表的含义:   如果在父表中找不到候选键,则不允许在子表上进行insert/update

--外键约束对父表的含义:    在父表上进行update/delete以更新或删除在子表中有一条或多条对
                    -- 应匹配行的候选键时,父表的行为取决于：在定义子表的外键时指定的
                    -- on update/on delete子句