# Write your MySQL query statement below
SELECT
ROUND(
    COUNT(DISTINCT a.player_id)/
    (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
)AS fraction
FROM Activity a
JOIN(
    SELECT
    player_id,
    MIN(event_date)AS first_login
    FROM Activity
    GROUP BY player_id
)first_login
ON a.player_id=first_login.player_id
AND a.event_date=DATE_ADD(first_login, INTERVAL 1 DAY);