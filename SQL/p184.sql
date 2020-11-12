-- Runtime: 652 ms, faster than 31.92% of MySQL online submissions for Department Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Department Highest Salary.

SELECT Department.Name as Department, T.Name as Employee, T.Salary
FROM
(
SELECT Name, Salary, DepartmentId, Max(Salary) over (Partition By DepartmentId) as ms
FROM Employee
) T
INNER JOIN Department ON Department.Id = T.DepartmentId
WHERE T.Salary = T.ms