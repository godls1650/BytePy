# 과팅 어플
# 함수화 시킨다
# 정의 되어있어야 사용할 수 있다.
# 한 동작을 설계해야한다.
# 이름만으로 어떤 동작인지 알아야한다.

def inputMyBirth(Cnt) : # 입력받은 주민번호 정보를 생년월일과
    print("과팅 어플 (%d회 검색)"%Cnt)
    inputed = input('생년월일을 입력(xxxxxx-n) > ').split('-')
    inputed[1] = int(inputed[1])
    Cnt += 1
    return inputed, Cnt

def membersLook(MemParam, myInfo) :
    for m in MemParam :
        if myInfo[1] % 2 is m[4] %2 :
            pass
        else :
            print(m[1],m[2])
    return None
    

members = [[20190123, '이민희', '경영학과', '001221',4],[20200123, '김지연', '영문학과','010304', 4],
           [20160123, '강민수', '정보통신학과', '970604',1],[20190123, '최선희', '경영학과','010304', 2]]
Count = 0# 입력 횟수 

myBirth, Count = inputMyBirth(Count)
membersLook(members, myBirth)

# 내 성별을 기준으로 members에서 나와 다른 성별만 출력한다.





        
