# Write your MySQL query statement below

with temp_tbl as (
select 'store1' as store union
    select 'store2' union
    select 'store3'
    
)
 select b.product_id, a.store,case when a.store = 'store1' and c.store1 is not null 
 then c.store1
 when a.store = 'store2' and c.store2 is not null
 then c.store2
 when a.store = 'store3' and c.store3 is not null
 then c.store3 
 end as price 
 from temp_tbl a
 cross join 
 (select distinct product_id from products)b
 left join products c
 on b.product_id = c.product_id
group by b.product_id, a.store, price
having price is not null