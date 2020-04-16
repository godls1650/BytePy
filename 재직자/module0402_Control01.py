# module0402_Control01
# 제어문 : 프로그램 동작의 순서 ( 이 프로그램의 논리적인 구조를 만든다. )
# 분기 제어 : if 명령어    /    반복 제어  while 명령어 블록 , for 명령어 블록

number = int(input('input your number > '))
isOdd = bool()
# 조건부 표현식 :  값을 저장할 변수 = 참일 때 저장할 값  조건 수식   거짓일 때 저장할 값 
isOdd = bool(number % 2)
result = '홀수' if number %2 else '짝수'

result = '홀수' if number %2  else '짝수' 

    
# 삼항 연산자  (?  : )
# result = number % 2 ? '홀수' : '짝수'



pocket = ['card', 'wallet']
if 'coin' in pocket :
    print('자판기 ㄱㄱㄱ')



money = True # 돈이 있다.
#money = False # 돈이 없다.
# 제어명령어의 구조
if money : # if 뒤의 수식의 값이 true 라면 아래 블록을 실행한다.  만약 ~~~ 라면  
    print('call taxi')
else :
    print('work')

print('go home')



# 절대값 변환


x = -102
if x < 0 :
    x = -x
print('|%d|'%(x))

# 교통사고 피해자의 나이를 입력하고 나이가 12세 이하이면 벌금 변수에 500을 저장
# 그 외의 경우엔 0원을 저장
# 함수 호출의 역순으로 처리

result = 500 if (int(input('나이 > '))) <= 12 else 0 


age = int(input('나이 > '))
result = bool()
if age <= 12 :
    result = 500
else :
    result = 0
    


















