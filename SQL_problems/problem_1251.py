"""1251. Average Selling Price


Write a solution to find the average selling price for each product. 
average_price should be rounded to 2 decimal places. 
If a product does not have any sold units, 
its average selling price is assumed to be 0.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2), 0) as average_price 
# FROM Prices p 
# LEFT JOIN UnitsSold u 
# ON p.product_id = u.product_id
# AND u.purchase_date 
# BETWEEN start_date
# AND end_date
# GROUP BY p.product_id;