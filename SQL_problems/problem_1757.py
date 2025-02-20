"""1757. Recyclable and Low Fat Products


Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT product_id FROM Products WHERE low_fats="Y" AND recyclable="Y";


import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][["product_id"]]
