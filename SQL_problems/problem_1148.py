"""1148. Article Views I

Write a solution to find all the authors that viewed 
at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.
"""

# SELECT DISTINCT author_id as id FROM Views WHERE author_id = viewer_id ORDER BY author_id

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views["author_id"] == views["viewer_id"]][["author_id"]].drop_duplicates().sort_values("author_id").rename(columns={"author_id": "id"})