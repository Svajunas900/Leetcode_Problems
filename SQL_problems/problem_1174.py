"""1174. Immediate Food Delivery II


If the customer's preferred delivery date is the same as the order date, 
then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. 
It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, 
rounded to 2 decimal places.

The result format is in the following example.
"""

# SELECT ROUND(AVG(order_date = customer_pref_delivery_date)*100,2) as immediate_percentage
# FROM Delivery
# WHERE (customer_id, order_date) in (
#     SELECT customer_id, MIN(order_date)
#     FROM delivery
#     GROUP BY customer_id
# );