#MainApp2.py
#문자열 포매팅 : 문자열에 출력 형식과 다른 변수를 사용해서 문자열의 형태를 완성
# 위치에 서식문자를 넣는다.
"""
 % + s  %s : String
 % Decimal : 10진수 출력 --> %d

"""
# 사용자 입력: input(입력시 보여줄 글자 )
#ID = input('ID 입력 > ') # 'godls1650'
"""
seq1 = input('숫자 입력 ')
print(seq1)
print('seq1의 타입 : ',type(seq1))
seq2 = int(input('숫자 입력 ')) # int('123') ==> 123
print('seq2의 타입 : ',type(seq2))
print(seq2)
"""
sName = input('이름입력 > ')
sAddr = input('주소입력 > ')
s_age = input('나이입력 > ')
n_Age = int(s_age)
form = '이름 : %s\n주소 :%s\n 나이 : %d'%(sName,sAddr, n_Age)

print(form)
print('%s(%d)\n%s'%(sName,n_Age, sAddr))


"""
address = '대전 서구 갈마동 271-11'
age = int(input('나이 입력 > ')) # int('22')
test = '주소는 %s 입니다.'%address
print(test)




fm = '주소는 %s 입니다.\n나이는 %d살 입니다.'%(address,age)
print(fm)

print('나이는' ,age, '세 입니다.')
"""
