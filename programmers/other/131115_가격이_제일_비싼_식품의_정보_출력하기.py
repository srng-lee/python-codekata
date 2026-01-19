# 가격이 제일 비싼 식품의 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131115
# 작성자: 설무아
# 작성일: 2026. 01. 19. 09:41:02

SELECT PRODUCT_ID, PRODUCT_NAME,PRODUCT_CD, CATEGORY, PRICE
from FOOD_PRODUCT
order by price desc
limit 1;