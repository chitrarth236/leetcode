# Write your MySQL query statement below

WITH CTE AS (SELECT * FROM 

                (SELECT Trips.*,Users.Banned as cbanned FROM Trips 
                LEFT JOIN Users 
                ON Client_Id = Users_Id) AS midtbl

                LEFT JOIN Users
                ON Driver_Id = Users_id)


SELECT tbl1.Request_at AS Day,round(IFNULL(total_nu/total,0),2) 'Cancellation Rate'

FROM (SELECT Request_at,count(id) as total FROM 
            (SELECT Id,Status,Request_at FROM CTE               
             WHERE cbanned = "NO" AND Banned = "NO") 
             as tbl group by Request_at) AS tbl1
             
             LEFT JOIN  (SELECT Request_at,count(id) as total_nu FROM
        (SELECT Id,Status,Request_at FROM CTE WHERE cbanned = "NO" AND Banned = "NO") as tbl
            where Status != "completed"
              group by Request_at) as tbl2

ON tbl1.Request_at = tbl2.Request_at 
HAVING Day between '2013-10-01' and '2013-10-03'

