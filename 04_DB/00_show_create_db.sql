-- 00_show_create_db.sql
-- 주석은 --
-- SQL 고정 명령어는 대문자로, 내가 짓는 이름은 소문자로. (소문자도 가능하나 대문자가 권장)
-- 반드시 세미콜론;으로 끝나기. 끝나지 않으면 실행되지 않음. (workbench 제외)
-- 띄어쓰기와 줄 바꿈을 적절하게. DB는 신경 쓰지 않음
-- 컬럼명은 여러 단어일 경우 따옴표로 감쌈. 한 단어일 경우 안 감싸도 됨.
-- 값은 문자열일 경우 따옴표로 감싼다.
-- 문자열 속 따옴표는 이스케이프 문자열 ('\')로 사용한다.
-- 모든 데이터 베이스 목록 보여주기
-- 커서를 둔 곳이 실행됨. 

SHOW DATABASES;

CREATE DATABASE test;

DROP DATABASE test;

CREATE DATABASE pet_shop;



