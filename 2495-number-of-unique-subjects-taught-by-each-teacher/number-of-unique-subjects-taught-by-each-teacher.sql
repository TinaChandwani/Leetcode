SELECT teacher_id, COUNT(DISTINCT subject_id) as cnt
FROM Teacher
GROUP by teacher_id