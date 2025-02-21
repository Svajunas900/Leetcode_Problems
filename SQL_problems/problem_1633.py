"""1633. Percentage of Users Attended a Contest


Write a solution to find the percentage of the users 
registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. 
In case of a tie, order it by contest_id in ascending order.

The result format is in the following example.
"""

# SELECT contest_id, ROUND(COUNT(contest_id)/(SELECT COUNT(user_id) FROM Users)*100,2) as percentage 
# FROM Users u 
# INNER JOIN Register r
# ON u.user_id = r.user_id
# GROUP BY contest_id
# ORDER BY percentage DESC, contest_id;