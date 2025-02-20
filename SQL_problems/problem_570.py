"""570. Managers with at Least 5 Direct Reports


Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT name FROM Employee WHERE id IN 
# (SELECT managerId FROM Employee GROUP BY managerId HAVING COUNT(*) >= 5);