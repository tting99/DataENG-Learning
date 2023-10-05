-- 03_NULL.sql

USE pet_shop;

INSERT INTO dogs1 (name, breed)
VALUES ('멍뭉이', '시고르');
-- 이렇게 하면 널값 들어감.
SELECT * FROM dogs1;

-- 널값 방지할려면
CREATE TABLE dogs2(
	name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

DESC dogs2;

-- 이러면 에러
INSERT INTO dogs2(name) VALUES ('god');
-- 널값 없이 줘야댐. 다 아는내용.
INSERT INTO dogs2(name, age) VALUES ('god', 3);

SELECT * FROM dogs2;

