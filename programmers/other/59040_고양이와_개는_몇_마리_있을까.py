# 고양이와 개는 몇 마리 있을까
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59040
# 작성자: 설무아
# 작성일: 2026. 02. 06. 12:41:58

SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
where ANIMAL_TYPE in('Cat','Dog')
group by ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;