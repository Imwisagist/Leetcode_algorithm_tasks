# https://leetcode.com/problems/swap-salary/description/

UPDATE Salary
SET sex = CASE
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END;