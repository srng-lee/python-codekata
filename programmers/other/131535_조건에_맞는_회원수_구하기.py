# 조건에 맞는 회원수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131535
# 작성자: 설무아
# 작성일: 2026. 01. 19. 10:00:20

SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021
  AND AGE BETWEEN 20 AND 29;