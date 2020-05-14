# 함수안의 변수의 효력 범위
# GLOBAL VARIABLE : 0개


def func(x, y) :
    global var
    var = var + 1

def func2(x) :
    x = x + 1
    return x
    
def mypow(x = 2, y = 2) :
    return x ** y

def testPrinting():
    global test # 외부의 변수에대한 바로가기
    print(test)

