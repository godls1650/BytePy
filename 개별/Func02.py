import random as rd
# 리스트에 난수를 세팅해주는 기능을 하는 함수
def setRandList() :
    global List
    global Size
    global Minimum
    global Maximum
    global bCollision # True 중복허용  False 중복 X
    
    temp = 0
    while len(List) != Size :
        temp = rd.randrange(Minimum, Maximum)
        if bCollision :
            List.append(temp)
        else :
            if temp not in List :
                List.append(temp)

def setRandList2(List,Size = 10 ,Minimum = 1, Maximum = 100 ,bCollision = False) :
    temp = 0
    while len(List) != Size :
        temp = rd.randrange(Minimum, Maximum)
        if bCollision :
            List.append(temp)
        else :
            if temp not in List :
                List.append(temp)
    return List


def func(n):
    return n * func(n-1) if (n != 1) else n

                
#NULL --> None 
if __name__ == '__main__' :
    List = list()
    Size = 10
    Minimum = 1
    Maximum = 100
    bCollision = False
    setRandList()
    SecondList = setRandList2(list(), 20, 10, 50, False)





    
    
                
    
