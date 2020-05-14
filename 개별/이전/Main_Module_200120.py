#var = int(input('정수 입력 > '))
# 프로그래밍 언어의 함수 : 매개변수, 결과값 -> ''
# 정수 입력 > 33
#키보드로 입력한 값을
#pi = 3.141592
#result =  pi * var * var
#print('입력한 정수는 ',var,'입니다.')
#print('반지름이',var,'인 원의 넓이는',result,'입니다.')
# 제곱 (+ - * / ** ,
# / : 나눗셈
# // : 몫
# % 나머지



side = int(input('정사각형의 변의 길이를 입력하세요 > '))#길이 값을 입력한다.
square = side ** 2#사각형의 넓이를 구한다.
print('변의 길이가',side,'인 정사각형의 넓이는', square, '입니다.')# 형식에 맞게 출력한다.
triangle = (side ** 2) / 2
print(type(triangle))
print('변의 길이가',side,'인 정삼각형의 넓이는', triangle, '입니다.')# 형식에 맞게 출력한다.

triangle = (side ** 2) // 2
print(type(triangle))
print('변의 길이가',side,'인 정삼각형의 넓이는', triangle, '입니다.')# 형식에 맞게 출력한다.


money = 32200
print(money//1000,',',money%1000)
print(str(money//1000)+','+str(money%1000))# '32'+ ','+'200' -> '32,200'

  

