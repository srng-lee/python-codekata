# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 설무아
# 작성일: 2026. 01. 22. 10:50:57

def solution(angle):
    if 0 < angle < 90:
        return 1
    if angle == 90:
        return 2
    if 90< angle < 180:
        return 3
    if angle == 180:
        return 4