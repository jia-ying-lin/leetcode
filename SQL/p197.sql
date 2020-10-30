# Write your MySQL query statement below

# Runtime: 607 ms, faster than 13.86% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.

SELECT w2.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1 and w1.temperature < w2.temperature

# Runtime: 290 ms, faster than 97.36% of MySQL online submissions for Rising Temperature.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rising Temperature.

SELECT w2.id
FROM Weather w1, Weather w2
WHERE to_days(w1.recordDate) + 1 = to_days(w2.recordDate) and w1.temperature < w2.temperature