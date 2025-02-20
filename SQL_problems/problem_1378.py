"""1378. Replace Employee ID With The Unique Identifier


Write a solution to show the unique ID of each user, 
If a user does not have a unique ID replace just show null.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT unique_id, name 
# FROM Employees 
# LEFT JOIN EmployeeUNI 
# ON Employees.id = EmployeeUNI.id; 

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    joined_df = pd.merge(employees, employee_uni, on="id", how="left")
    return joined_df[["unique_id", "name"]]