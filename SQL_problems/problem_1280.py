"""1280. Students and Examinations

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by student_id and subject_name.

The result format is in the following example.
"""

# SELECT s.student_id, s.student_name, sb.subject_name, COUNT(e.subject_name) as attended_exams
# FROM Students as s 
# CROSS JOIN Subjects sb
# LEFT JOIN Examinations as e 
# ON e.student_id = s.student_id 
# AND sb.subject_name = e.subject_name
# GROUP BY s.student_id, e.subject_name, sb.subject_name
# ORDER BY s.student_id, sb.subject_name