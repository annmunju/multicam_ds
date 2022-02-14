show databases;
show tables;

create databases multi;

use multi;

create table students(
 id int,
 name varchar(100),
 phone char(13),
 address varchar(1000)
);

desc students;

insert into students
 values(1, 'hong-gd', '010-1111-1111', 'seoul'
);

select *
from students;

alter table students
add job varchar(100);

desc students;

-- 원하는 열에만 데이터 추가하기
insert into students(id, name, address, job)
values (2, 'kim-sd', 'suwon', 'engineer');

-- 데이터의 속성 수정하기
alter table students
modify job varchar(1000);

-- 테이블 삭제하기
drop table students;

-- 데이터 베이스 삭제하기
drop databases multi;