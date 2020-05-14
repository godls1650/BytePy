# if 제어문 논리값을 기준으로 실행 여부를 결정하는 코드를 작성
#   논리값을 기준으로 두개 이상의 경우 중 하나를 실행 한다면 : if / else

# 음수값을 입력하면 재입력하는 코드
# 입력한 정수의 절대값을 출력하는 프로그램

# while반복
nVar = int(input('정수 입력 > '))
if nVar < 0 :
    nVar *= -1 # nVar = nVar * -1
else :
    pass
print('입력 값의 절대값은 |{}| 입니다.'.format(nVar))


if nVar < 0 :
    nVar = int(input('음수는 허용 안됩니다. 재입력 하세요 > '))

if nVar % 2 == 1 :
    print('홀수 입니다.')
elif nVar == 0 :
    print('0입니다.')
else :
    print('짝수 입니다.')

# 이진수로 바꿔서 출력
bit = list() # 나열할 데이터

while nVar != 0 :
    bit.append(nVar % 2)
    nVar //= 2 # nVar = nVar // 2

bit.reverse()
print(bit)
# for 제어문 -> 횟수를 확인할 수 있는 제어문
# 어떤 값이 특정 횟수만큼 반복하는 경우 ,
# 리스트, 튜플, 문자열,...등 나열된 데이터를 순서대로 사용할 경우

# 범위의 값을 이용한 반복 range(최소값 , 최대값)  range(최대값)
# for문은 기본적으로 1씩 증가
# 구구단 출력 
for i in range(2,10) :
    for j in range(1,10) :
        r = i*j 
        print('i : {}'.format(r))

for i in range(len(bit)) :
    print(bit[i], end = '')
print('')

for i in bit :
   print(i, end = '') 
print('')

data = ['BCM001', '홍길동' , '대전 서구 탄방동 113 - 32']
for i in data :
    i = 0
    print(i)
print(data)
for i in range(len(data)) :
    data[i] = 0
    print(data[i])






    
