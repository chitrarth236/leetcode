# Write your MySQL query statement below

WITH cte1 AS(SELECT id as x,
            CASE 
            WHEN id = (SELECT count(1) from seat) and id%2 != 0 THEN student
            WHEN id % 2 != 0 THEN (select student from seat as t1 where t1.id=x+1)
            WHEN id % 2 = 0 THEN (select student from seat as t1 where t1.id=x-1)
            #else (select student from seat as t1 where t1.id=x)
            end AS student
            from seat)

SELECT x as id, student FROM cte1;