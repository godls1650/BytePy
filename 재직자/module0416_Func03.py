#함수 작성
# def 함수명 ( 매개변수 ) :
# [tab] 함수내용
# [tab] 함수내용
# [tab] 함수내용
# .....
# [tab] 함수반환값 (return)

# 기본함수형태
# 반환값이 있을 떄 , 없을 경우
# 매개변수의 값을 미리 지정하는 경우
# 매개변수의 값을 지정하여 호출
# 매개변수의 갯수가 미정
# 키워드 파라미터 

# 전역영역 : 실행을 위한 코드 / 함수의 선언
# 함수 블록 --> 지역 영역 : 함수내부에서 사용하고 없어질 변수를 선언하고 함수 내용이 들어있는 공간


# 로그인
# 계정 목록 (관리자 계정목록 , 사용자계정 목록)을 조회한다.

# [????]계정목록에 ID가 있으면 True 리턴 없으면 False 리턴

def SearchAcc(accList , idParam ) :
    temp = [i[0] for i in accList]
    if idParam in temp :
        return True
    else :
        return False
    

#------------------------------------------------------------------------------------------------------#

# 프로그램의 바탕에서 사용될 데이터 
AdminAcount = [['admin', '1234'],['tiger', '4234']]
CsmAcount = [['cat', '1234']]
#사용자가 입력해서 변경할 데이터 
ID = input('ID > ')
PW = input('PW > ')
# 시퀀스 타입 in

if SearchAcc(AdminAcount, ID) :
    pass
else :
    if SearchAcc(CsmAcount, ID) :
        pass
    else :
        print('ID가 없습니다.')


temp = [i[0] for i in AdminAcount]
bThere = ID in temp
if bThere : # 관리자 ID인 경우

    pass
else :
    temp = [i[0] for i in CsmAcount]
    bThere = ID in temp
    if bThere : # 사용자 ID인 경우









# if 해당 ID가 관리자 계정목록에 있는가 :
#   비번 확인 후 로그인 성공시 관리자용 화면 출력
# else :
#   if 사용자 계정목록에 해당 ID가 있는지 확인한다. : 
#      비번 확인 후 로그인 성공시 소비자용 화면 출력












