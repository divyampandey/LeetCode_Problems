# Write your MySQL query statement below
select  case when max(t.rnk) > 1 then t.salary 
             else null
        end as SecondHighestSalary from (
select id, salary, dense_rank()
    over(order by salary desc) as 
rnk
from Employee ) t
where t.rnk = 2