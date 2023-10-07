-- 07_update.sql

-- UPDATE <table> SET <col>=<val> WHERE <conditions>;

SELECT * FROM cats;
-- id로 바꾸지않아서 위험하다는 오류가 뜸 command에서 하면 됨
UPDATE cats SET age=100 WHERE name= 'Misty';
