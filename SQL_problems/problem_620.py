"""620. Not Boring Movies

Write a solution to report the movies with an odd-numbered ID 
and a description that is not "boring".

Return the result table ordered by rating in descending order.

The result format is in the following example.
"""

# SELECT * 
# FROM Cinema 
# WHERE description != "boring" 
# AND id % 2 = 1 
# ORDER BY rating DESC;

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][["product_id"]]