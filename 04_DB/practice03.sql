-- practice03.sql

USE practice;
CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
	last_name VARCHAR(20) NOT NULL,
	first_name VARCHAR(20) NOT NULL,
	middle_name VARCHAR(20) DEFAULT 'NO middlename',
    age INT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'working'
);
DROP TABLE employees;
-- id - 숫자, PK, 자동 오름
-- last_name 문자(적정), 필수
-- first_name 문자(적정), 필수
-- middle_name 문자(적정), 필수 아님
-- age 숫자, 필수
-- status 문자(적정), 필수, 기본 값('working')

INSERT INTO employees(first_name, last_name, age)
VALUES ('Dora', 'Smith', 58);

SELECT * FROM employees;