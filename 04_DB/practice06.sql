-- practice06.sql

-- 나이가 4살인 모든 고양이를 삭제
DELETE FROM cats WHERE age = 4;

-- 나이가 id와 같은 모든 고양이를 삭제
DELETE FROM cats WHERE age = id;

SELECT * FROM cats; 

-- 모든 고양이 삭제
DELETE FROM cats;
