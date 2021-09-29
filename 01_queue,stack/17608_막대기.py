#17608 막대기 stack
from sys import stdin

#전체 개수와 데이터 입력받
n = int(input())
data = [0]*n
for i in range(0,n) :
    data[i] = int(stdin.readline())

#print(data)
    
curBig = 0
count = 0
#데이터 뒤에서부터 돌면서 현재까지 가장 큰 값은 curBig에 저장.
#curBig보다 크면 count에 +1하고 curBig값으로 업데이트
for i in range(1,n+1) :
    if data[-i] > curBig :
        curBig = data[-i]
        count+=1
        #print(str(-i)+" 보인다 count")

#출력
print(count)
    
