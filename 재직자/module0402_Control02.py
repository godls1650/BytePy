# 파이썬의 for 문
# range를 사용하는 경우 : 어느 범위의 숫자를 기준으로 반복한다. 시작값 ~ 종료값을 1씩 늘려가며 적용 
# range이외의 시퀀스를 사용하는 경우
sample = [10,20,14,21] # <0,1,2,3>

# range값을 인덱스로 사용한경우 --> for
for i in range(0,4) :
    print(sample[i] , end = ' ')
    
print()

# 리스트를 직접 for문에 사용한경우 --> foreach
for i in sample :
    print(i, end = ' ')

print()
# 중첩 제어
# 구조를 쌓는다
# 반복을 한다. --> 매번 같은내용을 반복하는 것이 아니다.
# 조건이 만족된 경우에 반복한다.







