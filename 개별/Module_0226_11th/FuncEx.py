#함수 입력값(매개변수) 를 이용해서
# 복합 연산 (동작)을 수행하고
# 결과값을 출력(반환) 하는
# 이름지어진 블록

def inputPerson() :
    name = input('이름 : ')
    address = input('이름 : ')
    phone = [int(i) for i in input('연락처 : ').split('-')]

    return [name, address, phone]

def viewPersonList(target) :
    print('이름 : {}\n주소 : {}'.format(target[0], target[1]))
    print('%03d-%04d-%04d'%(target[2][0],target[2][1],target[2][2]))


PersonList = list()
menu = 0

while True :
    menu  = int(input('1.정보 출력\n 2.정보 추가\n 3. 정보 삭제\nSelect >'))
    if menu == 1 :
        for i in PersonList :
            viewPersonList(i)
    elif menu == 2 :
        PersonList.append(inputPerson())
                
    elif menu == 3 :
        pass
    else :
        pass
