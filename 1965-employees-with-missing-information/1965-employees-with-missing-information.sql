# Write your MySQL query statement below

with all_employees as (
select a.employee_id from employees a
    union select b.employee_id from salaries b
    
)
select all_employees.employee_id from 
all_employees left join
Employees
on Employees.employee_id = all_employees.employee_id
left join Salaries 
on all_employees.employee_id = Salaries.employee_id
where Employees.name is null or Salaries.salary is null
group by employee_id
order by employee_id

