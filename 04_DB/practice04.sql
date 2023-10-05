-- practice04.sql

USE pet_shop;


-- 모든 고양이의 id 만 조회
SELECT id FROM cats;

-- 모든 고양이의 이름과 종만 조회
SELECT name, breed FROM cats;

-- 종이 Tabby 인 고양이의 이름과 나이만 조회
SELECT name, age FROM cats WHERE breed = 'Tabby';

-- id 와 나이가 같은 고양이의 id와 나이만 조회
SELECT id, age FROM cats WHERE id = age;

SELECT * FROM cats;