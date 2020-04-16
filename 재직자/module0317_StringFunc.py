#StringFunc.py
#문자열 관련 함수 : 문자열 변수나 상수 뒤에 .(dot) 을 붙인 다음 함수를 호출
text = 'hobby'
print(text.count('b')) # 문자열에 특정 문자가 몇개 있는지 조회
# 위치 조회
mail = 'godls1650@naver.com' # 이메일을 저장한 변수
print(mail.find('@')) # find : 찾는다.
print(mail.find('!')) # find : 찾는다.
print(mail.index('@')) # index : 인덱스 값을 반환
#print(mail.index('!')) # index : 인덱스 값을 반환

# 위치조회를 이용하는 경우
subLocate = mail.find('@') # 문자@ 의 위치값을 저장
account = mail[ : subLocate] # mail의 첫 글자 부터 '@'앞 까지 슬라이싱
domain = mail[subLocate + 1: ]
print('ID : ', account)
print('Service : ', domain)
# 문자열 삽입 : JOIN

print(','.join(text))
lst = ['dog','cat','bird']
print(lst)
print('\n'.join(lst))
menu = ['update', 'print', 'insert']
print('\n'.join(menu))

# 대문자 -> 소문자 lower()  소문자 -> 대문자 : upper()
print(text.upper()) # 문장의 첫 글자를 대문자로 자동 변경
print(text[0].upper() + text[1: ])

# ' 동해물과 백두산이 마르고 닳도록 ' 불필요한 여백이 발생했을 경우 : 공백 지우기 strip()
sample = ' 동해물과 백두산이 마르고 닳도록 '
print(sample)
print(sample.lstrip()) # 왼쪽 여백 제거
print(sample.rstrip()) # 오른쪽 여백 제거
print(sample.strip())  # 양쪽 여백 제거

# 문자열 대체 : replace
print(text.replace('obb','app'))
# 분할 , 포메팅

sample = sample.strip()
# 분할 : split() : 매개변수 = 기준이 될 문자
print(sample.split(' '))
# format 메서드 : 문장에 {}
showData = 'ID : {1:20} \nPW : {0}'.format(account, domain,text,sample)
print(showData)
print('ID : %20s \nPW : %s'%(account,domain))


print('{0}\n{0}'.format('hello world!'))
print('%s\n%s'.%('hello world!','hello world!'))
print('hello world!','hello world!',sep = '\n')
# 10종
# 5 x 10 행렬  10개 나열


#user1 [ 1 1 1 1 1 1 1 1 1 1]   -
#user2 [ 1 1 1 1 1 1 1 1 1 1]   100
#user3 [ 1 1 1 1 1 1 1 1 1 1]   10
#user4 [ 2 0 1 1 0 1 1 0 0 1]   40
#user5 [ 1 1 1 0 1 1 0 0 1 0]   150
                                .
                                .
                                .
                                .
                                .
                                .
                                




#                                -






