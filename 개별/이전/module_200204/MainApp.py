#MainApp.py
from FuncLib import * 
# 도서 정보 5권을 입력해서 지금 이 프로그램의 이 부분까지만 구현 
if __name__ == '__main__' :
    Member = fileLoad('..//..//resource//MemberData.txt') # 프로그램 실행 후 데이터 세팅
    select = 0
    while True :
        select = int(input("""1. 회원정보 추가
2. 회원정보 삭제
3. 회원정보 출력
4. 프로그램 종료
select > """))
        if select == 1 :
            MemberAppend(Member)
            
        elif select == 2 :
            continue
        elif select == 3 :
            continue
        elif select == 4 :
            continue
        else :
            continue
        
    
