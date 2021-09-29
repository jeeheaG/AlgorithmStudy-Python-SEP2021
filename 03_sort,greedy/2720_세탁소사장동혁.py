#백준 2720 세탁소 사장 동혁 greedy
from sys import stdin

#입력, 사용할 데이터 배열
T = int(stdin.readline())
m = [int(stdin.readline()) for _ in range(T)]
coin = [25, 10, 5, 1]

#케이스 수 만큼 반복. m을 coin의 큰 값부터 나누어 몫은 출력할 문자열에 추가, 나머지는 원래 m에 다시 저장 반복
for i in range(T) :
    countString = ""
    for j in range(4) :
        countString += str(m[i]//coin[j]) + " "
        m[i] %= coin[j]

    #출력
    print(countString)

        
