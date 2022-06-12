# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete from Person 
where id not in (select t.min_id from 
(select email, min(id)as min_id from Person group by email)t
                 )
