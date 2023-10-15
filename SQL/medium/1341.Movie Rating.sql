# https://leetcode.com/problems/movie-rating/description/

(SELECT u.name as results 
FROM MovieRating as m,Users as u 
WHERE u.user_id = m.user_id 
GROUP BY m.user_id 
ORDER BY COUNT(m.user_id) DESC, u.name 
LIMIT 1)
UNION ALL
(SELECT m.title as results
FROM MovieRating as r,Movies as m
WHERE m.movie_id = r.movie_id AND r.created_at LIKE "2020-02-%"
GROUP BY r.movie_id 
ORDER BY AVG(r.rating) DESC, m.title 
LIMIT 1);