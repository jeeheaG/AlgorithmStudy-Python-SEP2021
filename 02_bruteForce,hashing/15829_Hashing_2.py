#백준 15829 Hashing - 100점
#주의>> stdin.readline() 로 입력받으면 해당 줄의 마지막 개행문자까지 포함하므로 실제 데이터 길이에 +1됨. int등으로 형번횐하면 괜찮겠지만 항상 .strip()을 붙이는 습관 들일 것
#100점 나오려면 유니코드 활용 - 귀찮아하지 말고 시간 단축 생각하기
from sys import stdin

#데이터 입력
L = int(stdin.readline())
data = stdin.readline().rstrip()
sum = 0
r = 31
n = [0]*L
M = 1234567891 

#알파벳을 의미하는 숫자 반환 함수 - 유니코드 활용
def alToNum(data) :
    for i in range(L) :
        cal = ord(data[i]) - ord('a') + 1
        #print(data[i], "의 숫자 ", cal)
        n[i] = cal
    
alToNum(data)

#알파벳 배열을 숫자로 만들고 해시값 계산
for j in range(len(data)) :
    ri = r**j
    sum += n[j]*ri
    #print(j, " sum : ", sum)

print(sum % M)
