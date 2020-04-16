# Module0312.py
# 문자열 자료형 / print
text = "'19년도"
print(text)
print('20' + text)
# 엔터 주변의 한화(W)는 글자 서식에 따라서 '\'으로 사용된다.
# / : 슬래시  \ : 리버스슬래시 (역슬래시)
# 역슬래시 + 문자 : 이스케이프 시퀀스
# \ n : 다음 라인으로 이동 시킨다. : Next line (eNter)
# \ a : 시스템 경고음 출력 : Alarm
# \ t : 지정 간격(tab) 만큼 간격을 출력
# \ b : Back Space 

timelog = '9:\'50 :\"25'
# '9:' + "'50 :" + '"25'

# 문자열의 연산  : 문자열을 합친다. 문자열을 반복시킨다.
print('='*60) # =를 20번 반복시킨 문자열
print(' Windows Hack Program ')
print('='*60)

used = 10 # 기존 변수
update = 3 # 추가시킬 값


used = used + update # used라는 공간에 기존 used의 값과 update의 값을 더하고 그 후 입력 시킨다.
# STACK 처리 1) Used에 우측 항(13)을 입력해라
#                      ㄴ2) used값(10)과 update 값(3)을 더해라
# 프로그래머 특징 : 귀찮은 작업은 싫어한다. 간단한 코드를 여러번 쓴다던가. 

# used = 
# used + update
# used += update  --> 복합 연산 ( 산술 연산 또는 비트연산의 결과값과 입력연산을 합친 연산자) : 누적

# 문자열을 합친다 : Concatenation
#  A + B (X)  A += B (O)

text1 = 'hello'
text2 = 'world'
text1 += text2
print(text1) # python은 결합 (X)
text2 = 'new'
text1 += text2
print(text1)
print(text2)










