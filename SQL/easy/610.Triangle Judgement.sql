# https://leetcode.com/problems/triangle-judgement/description/

SELECT
    x,y,z,
    IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle
FROM Triangle;