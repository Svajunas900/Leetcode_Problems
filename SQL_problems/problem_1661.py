"""1661. Average Time of Process per Machine

There is a factory website that has several machines each running the same number of processes. 
Write a solution to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. 
The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, 
which should be rounded to 3 decimal places.

Return the result table in any order.

The result format is in the following example.
"""
# SELECT a.machine_id, round(
#     (select avg(a1.timestamp) 
#      from Activity a1 where a1.activity_type = 'end' and a1.machine_id = a.machine_id) 
#     - (select avg(a1.timestamp) 
#        from Activity a1 where a1.activity_type = 'start' and a1.machine_id = a.machine_id), 3) 
# as processing_time from Activity a GROUP BY a.machine_id