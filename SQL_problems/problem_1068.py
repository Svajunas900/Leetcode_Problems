"""1068. Product Sales Analysis I 


Write a solution to report the product_name, year, 
and price for each sale_id in the Sales table.

Return the resulting table in any order.

The result format is in the following example.
"""

# SELECT Product.product_name, Sales.year, Sales.price as price FROM Sales 
# LEFT JOIN Product ON Product.product_id = Sales.product_id;