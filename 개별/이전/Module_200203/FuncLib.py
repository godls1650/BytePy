#FuncLib.py
# 매개변수와 인수   f(x) = y x: 매개변수 parameter
#                           y: 인수 (결과값)
# 함수의 매개변수나 함수 내부에서 사용되는 변수
# 들은 전부 Local 변수 라고한다.
cnt = 0 # global 변수 

    
def func() :
    global cnt
    cnt = cnt + 1
    print('test', cnt)

def add(x, y) : # 매개변수 : x, y
    global cnt
    cnt = cnt + 1
    return x + y  # 인수 : x+y
def calc(x,y) :
    global cnt
    cnt = cnt + 1
    if y == 0 :
        return
    dic = {'+' : x+y,'-' :  x-y,
           '*' : x*y,'//' : x//y}
 
    return dic
def mypow(x , y=2) :
    
    return x ** y

def isOdd(x) :
 
    if x % 2 == 1 :
        return True
    else :
        return False
print(cnt)
if __name__ == '__main__' :
    pass
