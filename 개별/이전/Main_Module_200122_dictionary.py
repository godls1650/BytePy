# dictionary  사전형데이터
var = ['홍길동', 24, '325-5574']
print('이름 : {} \n나이 : {}\n연락처 : {}'.format(var[0],var[1],var[2]))
# dictionary 타입 데이터 -> {}
# 하나의 값을 정할 때 key : value   이름 : 홍길동

var2 = {'이름': '홍길동' , '나이': 24, '연락처' : '324-5574'}
n = {0:14 ,1:10, 2: 20, 3:30}

#딕셔너리의 인덱싱  key값을 인덱스로
print(var2['이름'])
print(var2['나이'])
print(var2['연락처'])
print('n의 타입 {}'.format(type(n)))
print('n[0] -> ',n[0])
print('n[1] -> ',n[1])
# 딕셔너리에 쌍 을 추가
print(var2)
var2['회원번호'] = 1
print(var2)
