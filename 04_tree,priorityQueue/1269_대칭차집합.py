# 백준 1269 대칭 차집합 트리
# 집합 자료형 사용하지 않고도 풀어보기
from sys import stdin

NA, NB = map(int, stdin.readline().split())
#집합 자료형 set()
A = set(list(map(int, stdin.readline().split())))
B = set(list(map(int, stdin.readline().split())))

print(len(A - B) + len(B - A))