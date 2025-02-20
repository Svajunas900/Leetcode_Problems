"""584. Find Customer Referee


Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT name FROM Customer WHERE referee_id != 2 or referee_id is null;\

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
  return customer[(customer["referee_id"] != 2) | (customer["referee_id"].isna())][["name"]]