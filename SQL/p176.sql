# Write your MySQL query statement below
with cte as(
SELECT salary,
rank() over (order by salary desc) as rnk
FROM employee)
SELECT 
max(case when cte.rnk = 2 then salary else null end)  SecondHighestSalary
from cte