#회원가입 테스트

# 어디까지 하나의 동작으로 구현 할것인가.
# 함수 이름을 뭐로 할건지
# 그래서 그 동작에 필요한 초기데이터는 뭔지 -> 매개변수로 뭐 쓸꺼냐 
# 동작을 구현
# 변경됬거나 새로 생긴 데이터 를 반환 한다.

#메타데이터 : 초기 데이터
def isNameNotExist(pAccoutList) :
    global Name
    Name = input('이름 > ')
    for ac in pAccoutList :
        if ac[0] is Name :
            return False
        else :
            continue
    return True

def createAccout() :
    global Name
    global ID
    global PW
    print('이름 : %s'%Name)
    ID = input('ID : ')
    PW = input('PW : ')
    return [Name, ID, PW]

# --------------------------------------------전체 동작 구현 코드-------------------------------------------
AccountList = [['홍길동','admin','1234'], ['호랑','tiger','tiger1234'], ['테스터','tester','4442']]
Name = str()
ID = str()
PW = str()
newAcc = list()

while True :
    menu = int(input('1. 로그인\n2.회원가입\nselect>'))
    if menu == 1 :
        pass
    elif menu == 2 :
        if isNameNotExist(AccountList) == True :
            newAcc = createAccout();
            AccoutList.append(newAcc)
        else :
            print('이미 가입 된 계정이 있습니다.')
            continue
    else :
        print('메뉴 입력 오류')



