-- 06_read.sql

USE pet_shop;

CREATE TABLE cats(
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100),
    breed VARCHAR(100),
    age INT
);

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);

SELECT * FROM cats;
	
SELECT name,age FROM cats;

SELECT * FROM cats WHERE age = 4;
-- 저장된 것은 name이 Egg지만 egg로 잡아도 나온다. 대소문자를 확실히 가리지 않는다
-- insensitive(대소문자 안따짐.) <-> sensitive(대소문자 따짐)
SELECT * FROM cats WHERE name = 'egg';

-- 컬럼명을 바꿀 수 있다. 조회해서 가져온 결과의 컬럼을 지정한다.
SELECT name AS '이름' FROM cats;

-- 여러개를 한번에도 가능하다.
SELECT name AS '이름', breed AS '종' FROM cats;


