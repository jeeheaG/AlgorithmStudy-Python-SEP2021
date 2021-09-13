#2161
from sys import stdin

#전체 개수 입력
n = int(input())
#입력 받은 n값을 크기로, 데이터 입력받을 배열 생성
data = [0]*n
##result[0]*n
#결과값을 하나씩 넣을 배열 선언
result=[]
#데이터 입력
for i in range(0,n) :
    data[i] = i+1

#print(data)

#카드를 버릴 차례라면 True, 뒤로 넣을 차례라면 False
throw = True
#data배열이 끝날때까지 반복하도록 함
i=0
while i<len(data) :
    #print("이번 숫자는 " + str(data[i]))
    if throw :
        #카드를 버릴 차례
        result.append(data[i])
    elif not throw :
        #뒤로 넣을 차례
        data.append(data[i])
    throw = not throw
    i+=1

##결과값을 한 줄에 출력
ans=""
for r in result :
    ans = ans+str(r)+" "
print(ans)
##print(n+n//2)
