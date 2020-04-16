import random as rd
#global 변수 선언부분
pay = 0
count = 0
Lotto = list()

#함수작성
def inputPay() :
    global pay
    pay = int(input('금액 입력 > '))

def setCount() :
    global pay
    global count
    count = pay // 1000

def setLotto() :
    global count #로또 갯수를 가져온다.
    global Lotto #로또 리스트를 가져온다.
    
    for i in range(count) :
        temp = list()
        while len(temp) != 6 :
            n = rd.randrange(1,46)
            if n in temp :
                continue
            else :
                temp.append(n)
        Lotto.append(temp)
            
def printLotto():
    global Lotto
    for i in Lotto :
        print('%d '%(Lotto.index(i) + 1),end = ' ')
        for n in i[ : 5] :
            print('%2d'%n, end=' ')
        print('  %2d'%i[5])
        


    
#동작부분
inputPay() # 금액을 입력한다.
setCount() # 로또 횟수를 구한다.
setLotto()
printLotto()








