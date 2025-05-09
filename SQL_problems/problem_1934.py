"""1934. Confirmation Rate


The confirmation rate of a user is the number of 'confirmed' 
messages divided by the total number of requested confirmation messages. 
The confirmation rate of a user that did not request any confirmation messages is 0. 
Round the confirmation rate to two decimal places.

Write a solution to find the confirmation rate of each user.

Return the result table in any order.

The result format is in the following example.
"""

# SELECT s.user_id, ROUND(IFNULL(AVG(action = 'confirmed'), 0), 2) as confirmation_rate 
# FROM Signups s 
# LEFT JOIN Confirmations c 
# ON s.user_id = c.user_id 
# GROUP BY s.user_id

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
  confirmations['confirmation_rate'] = confirmations['action'].apply(lambda x:1 if x == 'confirmed' else 0)
  avg_conf = confirmations[['user_id','confirmation_rate']].groupby('user_id')['confirmation_rate'].mean().round(2).reset_index()
  output = pd.merge(signups['user_id'],avg_conf,how='left').fillna(0)  
  return output