# 시퀀스 타입
# 길이 len
# 문자열 관련 함수
test = " HeLlO wOrLd "
# 문자 갯수 .count()
# 문자 위치 .find()  
mail = 'godls1650@gmail@.com'
index = mail.find('@')
index = mail.index('@')

print((test.upper()))
print((test.lower()))

# 문자열에 데이터 삽입
a = ','
print(a.join('abcd'))
# 여백 지우기
print(test.strip())
print(test.lstrip())
print(test.rstrip())

# 문자열을 변경 .replace 

print(test)
print(test.replace('wOrLd', 'test line'))

print('@의 위치 : ',index)
m_id = mail[:index]
m_domain = mail[index + 1 : ]



msg ='100110001101110001100010001011001'
# 패리티 비트 : 1의 갯수가 짝수개면 1  홀수 개 : 0
cnt = msg[ : len(msg)-1].count('1')
cnt % 2
#msg[len(msg)] == '0'


"""

print('{0}'.format('hi'))
print('{0: >10}'.format('hi'))
print('{0: <10}'.format('hi'))
print('{0:!>10}'.format('hi'))
print('{0:!<10}'.format('hi'))
print('{0:_^10}'.format('hi'))
pi = 3.1415926535

print('pi = %010.2f'%(pi))
print('pi = {0:^10.2f}'.format(pi))


name = input('이름 : ')
school = input('학교 : ')
age = int(input('나이 : '))
print('%-10s학생의 정보 조회\n이름 : %s\n나이 :%d\n학교 : %s'%(name, name, age, school))
# [name ,age , school]
print('{0: <10}학생의 정보 조회\n이름 : {0} \n나이 : {1} \n학교 : {2}'.format(name, age, school))
"""
