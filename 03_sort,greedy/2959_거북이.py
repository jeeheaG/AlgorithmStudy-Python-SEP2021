#백준 2959 거북이 sort 
from sys import stdin

#입력
n = list(map(int, stdin.readline().split()))

#오름차순으로 정렬
n = sorted(n)

#넓이 구함. 마주보는 두 변 중 더 짧은 변이 직사각형의 한 변의 길이가 되므로 두 변의 길이는 n[0]과 n[2]
print(n[0] * n[2])