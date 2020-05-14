# map --> map(x)  mapping()
# 파이썬 map 함수 --> 원래 데이터 집합이 있고 -> 변환시키는 경우
# map 함수
# 시퀀스 (map( 일괄 연산 함수명 , 리스트나 튜플))
# 기존 원소의 값을 일괄적으로 동일한 연산을 하는 경우
# for 반복 대신 사용

# map / filter / Reduce
# 람다식 



import random as rd

def func1(var) :
    global choice 
    if var > choice :
        True
    else : False

def priceUp(var) :
    return int(var * 1.8)


product = {'바나나' : 3600, '사과' : 1400, '배' : 2500}


"""
a = list()
for i in range(10000) :
    a.append(rd.random() * 100);

choice = float(input('숫자'))

b = list(map(func1, a))
c = list()
for i in range(10000) :
    if b :
        c.append(a[i])
    else :
        pass

"""




