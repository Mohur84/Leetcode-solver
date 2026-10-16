# Write your MySQL query statement below
select id, count(*) AS num
from(
    select requester_id AS id
    from RequestAccepted
    Union all
    select accepter_id AS id
    from RequestAccepted
)AS friends
group by id
order by num desc
limit 1;