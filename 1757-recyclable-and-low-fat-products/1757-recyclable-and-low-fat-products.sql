# Write your MySQL query statement below
select product_id from products
where low_fats = 'Y'
and recyclable = 'Y'
group by product_id