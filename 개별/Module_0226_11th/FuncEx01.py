#------정의부분--------------------------
def add(x , y) :
    r = x + y
    return r

def prt(x,y) :
    print(x, y)
    return None

def isOdd(x) :
    if x % 2 == 1 :
        return True
    else :
        return False

def SumAndMul(x,y):
    return x+y , x*y


#--------실행부---------------------------
A = True
B = False

result = (A or B) - (A and B)

var = add(10,20)
print(var)


prt(10,20) # None 값을 입력받지 않는다.
# 홀짝 구분
var = int(input('number > '))
if(isOdd(var)) :
    print("홀수")
else :
    print("짝수")

