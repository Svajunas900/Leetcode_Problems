"""197. Rising Temperature


Write a solution to find all dates' id with higher temperatures compared 
to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.
"""

# SELECT current_day.id
# FROM Weather AS current_day
# WHERE EXISTS (
#     SELECT 1
#     FROM Weather AS yesterday
#     WHERE current_day.temperature > yesterday.temperature
#     AND current_day.recordDate = yesterday.recordDate + INTERVAL 1 DAY
# );