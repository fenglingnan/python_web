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