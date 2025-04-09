SELECT r.contest_id, 
ROUND(((COUNT(u.user_id) / (SELECT COUNT(user_id) FROM Users)) * 100),2) as percentage
FROM Users u
JOIN Register r ON u.user_id = r.user_id
group by r.contest_id
order by percentage DESC ,r.contest_id ASC