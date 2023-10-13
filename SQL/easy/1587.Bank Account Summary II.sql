# https://leetcode.com/problems/bank-account-summary-ii/description/

SELECT name, SUM(amount) AS balance
FROM Transactions t
JOIN Users u ON t.account = u.account
GROUP BY name
HAVING balance > 10000;