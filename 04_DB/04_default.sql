-- 04_default.sql 

CREATE TABLE dogs3 (
	name VARCHAR(20) DEFAULT 'no name',
    age INT DEFAULT 0
    );
    
INSERT INTO dogs3() 
VALUES ();

SELECT * FROM dogs3;

-- 디폴트는 디폴트일 뿐 널을 넣는다면 들어간다.
INSERT INTO dogs3 (name) VALUES (NULL);

-- 그래서 보통 이 두개를 같이씀. 데이터 안넣으면 기본값이고 널은 들어올 수 없다.
CREATE TABLE dogs4(
	name VARCHAR(20) NOT NULL DEFAULT 'No name',
    age INT NOT NULL DEFAULT 0
);

-- 널을 넣었기에 이러면 에러남.
INSERT INTO dogs4 (name) VALUES(NULL);
