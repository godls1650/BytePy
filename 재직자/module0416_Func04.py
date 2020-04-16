#random 모듈 사용
import random as rd # random 모듈을 rd로 명칭변환하여 사용

# randrange(start, end = None, _int(class 'int'),..)
# start : 랜덤값의 시작 값
# end   : 랜덤의 끝 값


# 정수를 매개변수로 하는 함수 : 기본값 10
# 전역에 있는 리스트변수를 매개변수로 한다.
# 1 ~ 47 사이의 랜덤값을 리스트에 입력하는 함수
# 리스트의 길이가 정수 매개변수가 되면 종료하고 리스트를 반환

def InputList(l, size = 10) :
    for i in range(size) :
        l.append(rd.randrange(1, 47))
    return l

def collisionRemove(l) :
    temp = set(l)
    return list(temp)

a = list()
s = 12
a = InputList(a, s)
print('       a 리스트의 원소      ', a)
a = collisionRemove(a)
print('중복이 제거된 a 리스트의 원소', a)
