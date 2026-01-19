# 이름이 없는 동물의 아이디
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59039
# 작성자: 설무아
# 작성일: 2026. 01. 19. 09:59:18

SELECT ANIMAL_ID
from ANIMAL_INS
where  NAME is null
order by ANIMAL_ID