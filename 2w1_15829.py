#백준 15829 Hashing - 50점
#주의>> stdin.readline() 로 입력받으면 해당 줄의 마지막 개행문자까지 포함하므로 실제 데이터 길이에 +1됨. int등으로 형번횐하면 괜찮겠지만 항상 .strip()을 붙이는 습관 들일 것
#100점 나오려면 유니코드 활용
from sys import stdin

#데이터 입력
L = int(stdin.readline())
data = stdin.readline().rstrip()
sum = 0
r = 31
n = [0]*L
M = 1234567891 

#알파벳을 의미하는 숫자 반환 함수
def alToNum(data) :
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in range(L) :
        for i in range(len(alph)) :
            #print(a + ", " + alph[i])
            if(data[j] == alph[i]) :
                #print(i, " 찾았다 : ", i+1)
                n[j] = i+1
                break
    
alToNum(data)

#알파벳 배열을 숫자로 만들고 해시값 계산
for j in range(len(data)) :
    ri = r**j
    sum += n[j]*ri
    #print(j, " sum : ", sum)

print(sum % M)
