# 3월에 태어난 여성 회원 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
# 작성자: 설무아
# 작성일: 2026. 01. 22. 09:21:29

SELECT MEMBER_ID, 
MEMBER_NAME, 
GENDER, 
DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' AND TLNO IS NOT NULL AND MONTH(DATE_OF_BIRTH) = 3
ORDER BY  MEMBER_ID;