-- practice01.sql

-- 디비 생성
CREATE DATABASE practice;

-- 테이블 생성
CREATE TABLE people (
	first_name VARCHAR (20),
    last_name VARCHAR (20),
    age INT
);
-- 작업할 디비 선택
USE pratice;
-- or 왼쪽에서 그냥 선택-> 선택되면 불드체됨.


SHOW TABLES;

-- 테이블 상세보기
DESC people;

-- 테이블 지우기
DROP TABLE people;