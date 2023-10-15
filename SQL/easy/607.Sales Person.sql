# https://leetcode.com/problems/sales-person/description/

SELECT s.name
FROM SalesPerson s
WHERE s.name NOT IN
    (SELECT s.name
     FROM SalesPerson s
        LEFT JOIN Orders o USING (sales_id)
        LEFT JOIN Company c USING (com_id)
     WHERE c.name = 'Red');