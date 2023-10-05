-- practice02.sql

USE practice;

CREATE TABLE people (
	first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
    );

INSERT INTO people (first_name, last_name, age)
VALUES 
('재석', '유', 40),
('재필', '이', 30);

SELECT * FROM people;