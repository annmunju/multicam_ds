use employees;

select * from employees limit 5;
select * from dept_emp limit 5;

select *
from employees emp inner join dept_emp de on emp.emp_no = de.emp_no
limit 5;

select *
from employees emp inner join dept_emp de on emp.emp_no = de.emp_no
where de.to_date = "9999-01-01"
limit 10;

select first_name, dept_no
from employees emp inner join dept_emp de on emp.emp_no = de.emp_no
where de.to_date = "9999-01-01"
limit 10;

select first_name, title
from employees emp inner join titles tit on emp.emp_no = tit.emp_no
limit 10;

select *
from employees join dept_emp using(emp_no)
limit 5;

select *
from employees emp natural join titles tt 
limit 50;

-- 다 연결됨..
select count(*)
from employees join dept_emp;
select count(*)
from employees cross join dept_emp;

-- 같은 행만 연결됨..
select count(*)
from employees join dept_emp using(emp_no);

select count(*)
from employees emp natural join titles tt;


-- 현재 근무하고 있는 (9999-01-01) 직원들의 이름과 월급 출력
select first_name, salary
from employees emp inner join salaries sl on emp.emp_no = sl.emp_no
where sl.to_date = '9999-01-01';

-- 부서 이름과 관리자 이름을 출력
select dept_name, first_name
from (select * from departments natural join dept_manager) dept inner join employees emp on dept.emp_no = emp.emp_no
where to_date = '9999-01-01';

select dept_name, first_name
from departments d join dept_manager dm on d.dept_no = dm.dept_no
join employees e on dm.emp_no = e.emp_no
where dm.to_date = '9999-01-01';

select dept_name, first_name
from departments join dept_manager using(dept_no)
join employees using(emp_no)
where to_date = '9999-01-01';

use multi;

create table join_a(
    aa int,
    ab char(3)
);

create table join_b(
    bb int,
    ab char(3)
);

insert into join_a
values(1 , 'aaa');
insert into join_a
values(2 , 'bbb');
insert into join_a
values(3 , 'ccc');


insert into join_b
values(4 , 'aaa');
insert into join_b
values(5 , 'bbb');
insert into join_b
values(6 , 'ccc');

insert into join_a
values(7 , 'ddd');
insert into join_b
values(8 , 'eee');

select *
from join_a left join join_b using(ab);

select *
from join_a right join join_b using(ab);

select salary
from salaries
where emp_no in
    (select emp_no
    from employees
    where last_name = 'Haraldson')
limit 50;