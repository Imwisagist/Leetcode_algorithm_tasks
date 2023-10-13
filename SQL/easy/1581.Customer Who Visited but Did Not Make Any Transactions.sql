# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

SELECT
    customer_id,
    COUNT(v.visit_id) AS count_no_trans
from Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;