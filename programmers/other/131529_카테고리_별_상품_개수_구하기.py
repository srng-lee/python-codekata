# 카테고리 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
# 작성자: 설무아
# 작성일: 2026. 02. 05. 09:45:13

SELECT substring(PRODUCT_CODE,1,2) as CATEGORY, count(*) as PRODUCTS
from PRODUCT
group by substring(PRODUCT_CODE,1,2)
order by  CATEGORY