# 여러 조건을 하나로 합치는 경우
age = int(input('몇살이니 ?'))
grade = int(input('신검 등급 > '))

bGotothehell = age >= 20 and grade <= 2
if bGotothehell :
    print('군대 영장 내인생의 위기')

if bGotothehell is not False :
    print('이의있소 !!!!!!')

#height = float(input('기린앞에 가봐 '))

# 키가 150보다 작거나 나이가 8세 이하면 T익스 못탑니다.
# 논리연산자 : or 
#if age <= 8 or height <= 150.0 :
#    print('돌아가세요')

#false or false --> false
# true  or false => true
# false or True ==> true
# true  or true ==> true


"""
print("가방검사...")
var = list()
var.append(input('소지품 > '))
var.append(input('소지품 > '))
var.append(input('소지품 > '))
var.append(input('소지품 > '))
var.append(input('소지품 > '))



if '담배' in var :
    print('진실의 방으로..')
else :
    pass
"""
