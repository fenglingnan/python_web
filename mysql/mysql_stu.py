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