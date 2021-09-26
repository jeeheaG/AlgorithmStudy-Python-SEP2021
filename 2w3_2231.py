#백준 2231 분해합
#[LOST] 문제의 출력 조건을 정확히 읽을 것! 해당하는 값이 없을 시 0 출력
from sys import stdin

N = int(stdin.readline())

result = 0

#완전 탐색 - 어떤 수의 생성자는 원래 수보다 무조건 작으므로 0부터 N-1까지 다 계산해 봄
for i in range(N) :
    isum = sum(list(map(int, str(i)))) #숫자의 각 자리수를 int 배열로 저장하고 그들의 합을 구함
    if(i+isum == N) : 
        result = i
        break

print(result)

