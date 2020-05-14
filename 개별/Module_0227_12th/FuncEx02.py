# from
# import


# from : 파일 명
# import : 필요한 함수나 클래스
# from이 필요 없는 경우 : 기본경로가 지정된 파일들
#특정 파일에 있는 모든 내용을 가져올 경우

import random

# 사용자

var = set() # 중복이 안되는 타입 , 숫자 집합  --> 정렬한다.  빙고 --> 정렬 할 필요 없음
while len(var) != 25 :
    var .update((str(random.randrange(1,50)),))

temp = list(var)

data = [int(i) for i in temp]

userboard = list()
for i in range(5) :
    userboard.append([j for j in data[i*5 : i*5+5]])
for i in range(5):
    for j in range(5) :
        print("%2d "%userboard[i][j], end = '')
    print()

    
#컴퓨터

var = set() # 중복이 안되는 타입 , 숫자 집합  --> 정렬한다.  빙고 --> 정렬 할 필요 없음
while len(var) != 25 :
    var .update((str(random.randrange(1,50)),))

temp = list(var)

data = [int(i) for i in temp]

comboard = list()
for i in range(5) :
    comboard.append([j for j in data[i*5 : i*5+5]])



for i in range(5):
    for j in range(5) :
        print("%2d "%comboard[i][j], end = '')
    print()






