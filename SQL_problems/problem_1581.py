"""1581. Customer Who Visited but Did Not Make Any Transactions


Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in any order.

The result format is in the following example.
"""

# SELECT Visits.customer_id, COUNT(*) as count_no_trans FROM Visits 
# LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id WHERE Transactions.visit_id IS NULL GROUP BY Visits.customer_id;   