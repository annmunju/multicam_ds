mysql -u root -p;

source employees.sql;

show databases;

use employees;

show tables;

desc employees;

select *
from employees;

select count(*) as 사원수
from employees;

select emp_no, first_name, last_name
from employees
limit 5;

select *
from current_dept_emp
limit 1000;

select *
from employees
where hire_date >= "2000-01-01";

select count(*)
from salaries;

select *
from salaries
limit 100;

select *
from salaries
where salary >= 150000;

select *
from salaries
where salary > 100000 and salary <= 150000;

select *
from employees
where birth_date between('1960-01-01' and '1970-01-01');

select *
from salaries
order by salary asc
limit 100;

select *
from salaries
order by salary desc
limit 100;

-- 늦게 취업한 사람 순서, 나이순으로
select hire_date, birth_date
from employees
order by hire_date desc, birth_date
limit 100;

-- 나이 순서로, 늦게 취업한 순서대로
select *
from employees
order by birth_date, hire_date desc
limit 50;

select title
from titles
limit 10;

select title, count(*)
from titles
group by title;

select dept_no, count(dept_no)
from dept_emp
group by dept_no
having count(dept_no) >= 50000;