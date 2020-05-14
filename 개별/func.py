import random as rd

Lotto = list()
pay = 7500
count  = 0
re = 0

def calcCount() :
    global pay
    global count
    global re
    
    if pay > 5000 : 
        re = pay - 5000
        pay = 5000
    count = pay // 1000
    
def setLotto():           # Lotto, count : 함수 종료 후에도 남아야 하는 값 / 함수 외부에서 가져온 변수   , 매개변수로 불러올 수 있다.    
    global Lotto
    global count         #  temp,  n : 함수 동작에 필요한 변수 , 함수가 종료된 후엔 사용 안하는 변수  : 함수의 지역변수 함수와 함께 종료 
    
    for i in range(count) : 
        n = 0
        temp = list()
        while(len(temp) != 6) :
            n = rd.randrange(1,46)
            if n not in temp :
                temp.append(n)
        Lotto.append(temp)

def setLotto2(pLotto, pCount):           # Lotto, count : 함수 종료 후에도 남아야 하는 값 / 함수 외부에서 가져온 변수   , 매개변수로 불러올 수 있다.    
    #global Lotto
    #global count         #  temp,  n : 함수 동작에 필요한 변수 , 함수가 종료된 후엔 사용 안하는 변수  : 함수의 지역변수 함수와 함께 종료 
    
    for i in range(pCount) : 
        n = 0
        temp = list()
        while(len(temp) != 6) :
            n = rd.randrange(1,46)
            if n not in temp :
                temp.append(n)
        pLotto.append(temp)
    return pLotto
        

def myPow(under, up) :   # x = up = 10
    temp = under
    result = 1
    x = up
    for i in range(x) :
        result *= temp
    return result
    



#----------------------------------------exe------------------------
calcCount()
setLotto()
print(Lotto)
Lotto = setLotto2(Lotto, count)
x = x + 1

r = myPow(2,10)








