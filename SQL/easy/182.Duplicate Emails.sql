# https://leetcode.com/problems/duplicate-emails/description/

SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;