create database multi;
use multi;

create table students(
 id int,
 name varchar(100),
 phone char(13),
 address varchar(1000),
 job varchar(100)
);

--

insert into students
 values(1, 'hong-gd', '010-1111-1111', 'seoul', 'ai'
);

insert into students(id, name, phone)
values (2, 'kim-sd', '02-222-2222');

select *
from students;

commit;

update students 
set phone = '010-2222-2222',
    address = 'suwon',
    job = 'engineer'
where id = 2;

delete from students
where id = 1;

rollback;

use mysql;

grant all privileges on *.* to 'root'@'localhost' with grant option;
create user 'root'@'%' identified by '암호@';

grant all privileges on *.* to 'root'@'%' with grant option;

flush privileges;
commit;