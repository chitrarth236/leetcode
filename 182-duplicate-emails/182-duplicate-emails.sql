# Write your MySQL query statement below

SELECT DISTINCT A.email FROM Person AS A JOIN Person AS B ON A.email = B.email WHERE A.id <> B.id;
