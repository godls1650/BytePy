#제어문 : 프로그램의 구조를 제어하는 문장
# 분기 제어  조건수식에 의해서 실행 할 문장인지 아닌지를 결정
# 같다 다르다 초과 미만 이하 이상... 포함되어있다 있지 않다. ==> True / False

#height = int(input('키를 입력 하세요 > '))
# 만약 ~~라면 : if  다중 조건을 이용한 다중 분기  ==  !=    !(반전, 부정) 연산 ! : not
# 나이 와 키를 입력하고
# 나이가 10세 이상이고 키가 150cm 보다 큰사람 만 통과하는 프로그램을 작성하세요
# 조건을 만족하지 못한 경우 키 때문인지 나이 때문인지에 따라서
# 떡국을 먹으세요 , 우유를 먹으세요 를 출력하세요

# 나열 자료형과 if 문

number = int(input('숫자 입력 > '))
#if number % 2 : 
#    result = '홀수'
#else :
#    result = '짝수'

result = '홀수' if number % 2  else '짝수' # 조건부 표현식  result = A if 조건식 else B

print('{0}는 {1}입니다.'.format(number, result))


age = int(input('나이를 입력 하세요 > '))
if age >= 20 :
    print('성인 입니다.')
    pay = 1250
elif age >= 17 :
    print('고등학생 입니다.')
    pay = 860
elif age >= 14 :
    print('중학생 입니다.')
    pay = 570
elif age >= 8 :
    pay = 560
    print('초딩입니다. ')
else :
    pay = 0
    print('미취학 입니다.')
    
print('요금은 {}원 입니다.'.format(pay))


pocket = ['Wallet', 'Lighter','Key']
item = input('소지한 물건을 쓰세요 > ')


if item not in pocket :
    print('있는 물건입니다 . 니꺼 아니에요')
else :
    print('새것 인거같습니다. 주워갑니다.')


if age >= 10 and height > 150 :
    print('통과')
elif height <= 150:
    print('우유 먹으세요')
elif age < 10 :
    print('떡국 먹으세요')
else :
    pass

    


