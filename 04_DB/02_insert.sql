-- 02_insert.sql

USE pet_shop;

-- INSERT INTO <table>(<col1>, <col2>)
-- VALUES (<col1>, <col2>)
INSERT INTO dogs1 (name, breed, age)
VALUES ('맥스', '말티즈', '2');

-- 디비 확인해보기.
SELECT * FROM dogs1;


-- 여러개 넣어보기
INSERT INTO dogs1 (name, breed, age)
VALUES
	('짱구', '시고르자브', 5),
	('찡찡', '요쿠', 2)