# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

SELECT unique_id,name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;