"""1193. Monthly Transactions I


Write an SQL query to find for each month and country, 
the number of transactions and their total amount, 
the number of approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.
"""

# SELECT SUBSTRING(trans_date, 1, 7) as month,
# country,
# count(state) as trans_count,
# sum(state="approved") as approved_count,
# sum(amount) as trans_total_amount,
# sum(IF(state="approved", amount, 0)) as approved_total_amount
# FROM Transactions
# GROUP BY month, country 