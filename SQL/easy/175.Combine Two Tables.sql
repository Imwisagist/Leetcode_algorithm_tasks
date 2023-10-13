# https://leetcode.com/problems/combine-two-tables/description/

SELECT
    firstName,
    lastName,
    city,
    state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;