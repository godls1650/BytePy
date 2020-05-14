# 문자열 (STRing)
# 초기화
# \n -> enter 값

# 절차지향 방식

# 객체지향 프로그래밍 언어
#  --> 사물 개념의 동작에 초점을 맞춘 프로그램 방식


sName = ''
sAddress = str()
sName = "애'국'가"
sAddress = """동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이보전하세"""
enter = "동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라만세\n무궁화 삼천리 화려강산\n대한사람 대한으로 길이보전하세"

#indexing
#slicing 나열변수[1 : 5]
#문자열 객체의 함수

#특정 글자로 분할 ( 문자열 .split(기준))

text =enter.split(' ')
# 출력 서식 (문자열 상수 . format(나열 할 값)
height = 150
age = 13
name = '잼민이'

print(height, end = '----')
print(age, end = '\t')
print(name)

form = '키 : {} 나이 : {} 이름 : {}'.format(height, age, name)
print(form)
print('키'+str(height)+' 나이 : '+str(age)+' 이름 : '+name)

# 150 ==> str () ==? '키 :'+'150'

print(sName)







