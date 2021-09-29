#12605 단어순서 뒤집기 stack
from sys import stdin

#전체 개수 입력
n = int(stdin.readline())
#데이터 입력받을 배열과 결과물 넣을 배열 선언
data = [""]*n
result = [""]*n
#데이터 입력
for i in range(0,n) :
    data[i] = stdin.readline()

#print(data)

#데이터 하나씩 돌면서 스페이스바 기준으로 단어를 잘라 새 배열 slist를 만듦.
#slist의 값을 역순으로, 준비된 temp에 넣고 temp 하나가 다 만들어지면, 결과물 result에 저장
for i in range(0,n) :
    temp = "Case #"+str(i+1)+": "
    slist = data[i].split()
    for j in range (1,len(slist)+1) :
        temp += slist[-j]
        temp += " "
    result[i] = temp

#결과물 result를 한 줄에 하나씩 출력
for r in result :
    print(r)
#print(result)
