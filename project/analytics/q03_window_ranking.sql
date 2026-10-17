-- title: Ранжування оплат клієнтів за допомогою віконної функції
SELECT id, member_id, paid,
       RANK() OVER (PARTITION BY member_id ORDER BY paid DESC) as rank_in_member
FROM visit
ORDER BY member_id, rank_in_member, id
LIMIT 100;