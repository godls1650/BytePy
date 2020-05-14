#MainApp.py
from FuncLib import *
from FuncLib import cnt
# 내부의 모든 정보를 불러온다
# 함수적 프로그래밍 방식 변수에 동작을 저장
# lambda 매개변수, 매개변수 : 매개변수를 이용한 표현식
if __name__ == '__main__' :
    ADD = lambda x, y :x+ y
    CircleSize = lambda r : 3.141592 *2*r
    CircleArea = lambda r : 3.141592 * (2**r)
    result = CircleArea(4)
    result = 100+ 200
    print(result)

    POW = lambda x,y = 2: x ** y
    ISODD = lambda x : True if x % 2 else False
    test = lambda x : list(range(x))
    print(type(test))
    t = test(10)
    print(t)
    
    print(POW(10))
    print(ISODD(10))
    
    x = 1
    y = 2
    print(x,y,add2())
    
    func()
    func()
    func()
    print('10 + 20 = {}'.format(add(10,20)))
    print('3 ** 2 = {}'.format(mypow(3)))
    print('2 ** 10 = {}'.format(mypow(2,10)))
    num = 2003
    print('{} 은'.format(num) , end = ' ')
    if isOdd(num) :
        print('홀수 입니다.')
    else :
        print('짝수 입니다.')
    var = calc(10,3)
    print(var['+'])
    print(var['-'])
    print(var['*'])
    print(var['//'])
    print('cnt --> ', cnt)
    
    
