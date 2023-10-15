# https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/

SELECT person_name 
FROM (
    SELECT
        person_name,
        weight,
        turn,
        SUM(weight) OVER(ORDER BY turn) AS cum_sum
    FROM Queue) x
WHERE cum_sum <= 1000
ORDER BY turn DESC
LIMIT 1;