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

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[::2][cinema.description != 'boring'].sort_values('rating', ascending = False)