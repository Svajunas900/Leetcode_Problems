"""577. Employee Bonus


Write a solution to report the name and 
bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT Employee.name, Bonus.bonus FROM Employee LEFT JOIN Bonus ON Bonus.empId = Employee.empId 
# WHERE Bonus.bonus < 1000 OR Bonus.bonus is null;

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
  joined_df = pd.merge(employee, bonus, on="empId", how="left")
  return joined_df[(joined_df["bonus"] < 1000) | (joined_df["bonus"].isna())][["name", "bonus"]]