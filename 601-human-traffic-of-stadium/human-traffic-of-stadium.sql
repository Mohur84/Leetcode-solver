# Write your MySQL query statement below
WITH busy AS (
    SELECT id, visit_date, people,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
counted AS (
    SELECT id, visit_date, people,
           COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM busy
)
SELECT id, visit_date, people
FROM counted
WHERE cnt >= 3
ORDER BY visit_date;