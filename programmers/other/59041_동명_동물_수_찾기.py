# 동명 동물 수 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59041
# 작성자: 설무아
# 작성일: 2026. 02. 05. 09:34:26

SELECT name, count(name) as count
from ANIMAL_INS
where name is not null 
group by name
having count(name) >=2
order by NAME