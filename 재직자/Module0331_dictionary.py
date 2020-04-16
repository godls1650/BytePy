#Module0331_dictionary.py
# 사전형의 메소드 --> DICT.function()
# 알바생 정보  이름 , 시급, 근무조 , 총 근무시간 , 연락처  다섯명 
"""
근무조 = [('A','P','O','C','F'),('C','F','A','P','O'),('A','C','F','P','O')]
알바생명단_고정 = [['홍길동',근무조[0],'010-1234-1234'],
                  ['아무개',근무조[1],'010-4234-1224'] ]

알바생명단_사전형버전 = {'010-1234-1234':['홍길동',근무조[0]] ,
                        '010-4234-1224':['아무개',근무조[1]]    }


알바생명단_고정[0][2]
알바생명단_고정[1][2]

# key값 만 조회하는 경우 
a = 알바생명단_사전형버전.keys() # 해당 딕셔너리의 키만 묶은 타입 dict_keys type --> not list 

# value만 조회하는 경우 values()

# 해당 딕셔너리의 원소를 조회    items()
# 딕셔너리 타입의 일반사용


dictionary = {'a' : [10,20,30,40,50], 'b' : [100,200,300,400,500], 'c' : [1000,2000,3000,4000,5000]}
# keys를 사용해서 반복할 경우 
keys = list(dictionary.keys())
for i in range(len(keys)) :
    dictionary[keys[i]] = 0
    print(dictionary[keys[i]])

# items를 사용한 경우
test = list(dictionary.items())
for i in range(len(test)) :
    test[i][1] = 0
    print(test[i][1])
"""
# 참거짓 타입
ComPwrButton = False
# 데이터 처리 : 마스킹 --> 비트연산 
SignalSet = (bin(1),bin(2),bin(4),bin(8))
SigOper = {1 : 'powerOn' , 2 : 'powerDown', 4 : 'Right On', 8 : 'Right OFF'}
Signal = bin(2 ^ 4) # 00001100
  # 00001000  --> 00001000 not Zero --->
#print(SigOper[Signal & SignalSet[0]])










