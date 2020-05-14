# 함수 : 특정 과정에 필요한 동작을 하나로 묶어서 호출 , 실행 , 결과 반납 의 과정으로 처리
# 반복코드를 줄일 수 있다.
# 모듈화 시켜서 다른 파일에 있는 코드를 불러와서(Load) 해서 사용한다.
# 함수이름 , 매개변수를 정의 하고 동작을 작성  
def printMember(D, K) :
    print('회원번호 : ' ,  K)
    print('이름 : ', D[K][0])
    print('주소 : ', D[K][1])
    print('차량 : ', D[K][2])

def add(x, y) :
    return x + y
def SetRangeList(start, end) :
    return list(i for i in range(start, end))
def Minimum(L) :
    x = L[0]
    for i in L[1: ]:
        if x > i :
            x = i
    return x
        
#--------------------------------------------------
num1 = SetRangeList(0,100)
num2 = SetRangeList(100,200)

lst = [3465,23445,234,345,213,67,234,14,8765,12,544,67,87,78654]
# 정수가 입력된 리스트에서 가장 작은 값을 반환하는 함수 작성

m = Minimum(lst)
print('lst의 최소값 : ', m)

"""
var = add(1001, 2022)
print(var)

dic = {'MEM1020' : ['홍길동', '대전 서구 둔산로 1723 402호',3250],
       'MEM7555' : ['남상민', '대전 동구 새울로 1803 1212호',7640],
       'MEM1460' : ['강민수', '대전 중구 대전역로 1522 303호',3440]}
keyList = list(dic.keys())

printMember(dic, keyList[0])
printMember(dic, keyList[1])
printMember(dic, keyList[2])
"""



