# 평균 일일 대여 요금 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151136
# 작성자: 설무아
# 작성일: 2026. 01. 20. 09:54:19

SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE 
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'