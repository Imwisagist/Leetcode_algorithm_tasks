# https://leetcode.com/problems/not-boring-movies/description/

SELECT
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE MOD(id,2) = 1 AND description != 'boring'
ORDER BY rating DESC;