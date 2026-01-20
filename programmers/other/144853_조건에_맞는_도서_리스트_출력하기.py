# 조건에 맞는 도서 리스트 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144853
# 작성자: 설무아
# 작성일: 2026. 01. 20. 09:44:03

SELECT BOOK_ID,DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
from BOOK
where CATEGORY = '인문' and year(PUBLISHED_DATE) =2021
ORDER BY PUBLISHED_DATE;