# 백준 9625 BABBA graph

from sys import stdin

K = int(stdin.readline())
a = 1
b = 0

# 버튼을 누름 - 현재 a b개수를 인수로 받고 다음 a b개수를 반환함
def pressButton(a,b) :
    return [b, a+b]

# K번 반복
for i in range(1, K+1) :
    a, b = pressButton(a,b)

print(a,b)
