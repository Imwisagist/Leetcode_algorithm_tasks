# https://leetcode.com/problems/employees-with-missing-information/description/

SELECT j.employee_id
FROM (
    SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
    UNION 
    SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)
) AS j
WHERE j.name IS NULL OR j.salary IS NULL
ORDER BY employee_id;