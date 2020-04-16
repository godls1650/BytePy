#Module0312_StringSequential.py
#나열된 형태로의 문자열
text = 'apple pie'
print('='*50)
print('문자열의 인덱싱 & 슬라이싱')
print('='*50)
#나열된 데이터의 갯수 : len() 매개변수 : 길이가 있는 데이터
l = len(text)
print('%s의 길이 : %d'%(text,l))
#text에 저장된 글자를 하나씩 따로 사용할 경우
#나열된 데이터를 분할(INDEX) 해서 따로 사용한다. --> 인덱싱
# 인덱싱 사용 : 나열형변수명 + [ 번호 ]
# 나열형 변수의 인덱스는 0번 부터 시작 
print('text의 1번 데이터 > ', text[1])
print('text의 2번 데이터 > ', text[2])
print('text의 3번 데이터 > ', text[3])

print('text의 첫번째 글자 > ',text[0])
print('text의 마지막 글자 > ',text[8])
# 문자열의 인덱스 : 0 ~ 길이-1
# 문자열의 인덱스에 길이 이상의 값을 사용할 때
print('text의 -1번 데이터 > ', text[-1])
print('text의 -2번 데이터 > ', text[-2])
print('text의 -3번 데이터 > ', text[-3])
# 특정 범위만큼으로 부분 편집해서 사용 : 슬라이싱 [시작인덱스 : 마지막 + 1]
# apple pie    --> apple    / pie
print('-'*50)
print('문자열의 슬라이싱')
print('-'*50)
print(text[0 : 5])
print(text[6 : 9])
print(text[0 : l])
# 슬라이싱의 값이  0번이나 마지막 인덱스인 경우 : 값을 안쓰고 생략 가능 

print(text[-1: -5])
print(text[6 : ])
print(text[ : ])














