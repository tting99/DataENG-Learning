-- 05_primary.sql

INSERT INTO dogs4()
VALUES (),(),(),();

SELECT * FROM dogs4;

-- 주키 주는법.
CREATE TABLE dogs5 (
	id INT NOT NULL PRIMARY KEY,
	name VARCHAR(20) NOT NULL DEFAULT '댕댕이',
    age INT NOT NULL DEFAULT '0'
);

-- 이러면 당연히 에러겠지, 주키가 유니크하지않아서
INSERT INTO dogs5 (id, name, age)
VALUES
	(1, '골드', 3),
    (1, '실버', 5);
    
SELECT * FROM dogs5;

-- 보통 주 키는 이 옵션하고 같이 쓴다.() 주키를 매번 카운트할 수 없으니.  자동으로 인크리지먼트
CREATE TABLE uniq_dogs (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL DEFAULT '댕댕이',
    age INT NOT NULL DEFAULT '0'
);
-- 아이디 따로 안줘도 됨 위에서 자동 했으니.
INSERT INTO uniq_dogs (name, age)
VALUES
	('골드', 3),
    ('실버', 5),
    ('에메랄드', 2);
    

SELECT * FROM uniq_dogs;

-- 이렇게 아무것도 없는거 넣어도 주키 알아서 올라감.
INSERT INTO uniq_dogs()
VALUES (),(),(),();