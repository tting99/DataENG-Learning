-- 01_table.sql

-- 50크기의 문자열 컬럼, 인트형 나이 만들기
CREATE TABLE cats (
	name VARCHAR(50),
    age INT
);
SHOW TABLES; -- 먼테이블 있는지 보여줘
DESC cats; -- 그 테이블 자세히 보여줘
DROP TABLE cats;
CREATE TABLE dogs1 (
	name VARCHAR(50),
    breed VARCHAR(50),
    age INT
);

DESC dogs1;