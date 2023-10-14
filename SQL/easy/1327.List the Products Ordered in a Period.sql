# https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/

SELECT product_name, SUM(unit) AS unit
FROM Products p
JOIN Orders o USING (product_id)
WHERE YEAR(order_date) = '2020' AND MONTH(order_date) = '02'
GROUP BY p.product_id
HAVING SUM(o.unit) > 99;