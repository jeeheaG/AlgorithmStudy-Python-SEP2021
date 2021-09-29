#백준 2798 블랙잭 완전탐색
#입력받는 방법 한 번 정리하기
#문제똑바로 읽기..^^ : <인지 <=인지
from sys import stdin

N, M = map(int, stdin.readline().split()) #잊지 말기!
card = list(map(int, stdin.readline().split()))

closeSum = 0

# N개의 수 중 3개를 비복원추출하는 모든 경우의 수 탐색
for i in range(0, N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            sum = card[i] + card[j] + card[k]
            #print(sum)
            # sum 값이 M보다 작거나 같은 값들 중 가장 큰 값 구하기
            if(sum<=M) :
                #아래 if문은 closeSum = max(closeSum, sum)과 같은 표현!
                if(closeSum < sum) :
                    closeSum = sum
print(closeSum)
            

