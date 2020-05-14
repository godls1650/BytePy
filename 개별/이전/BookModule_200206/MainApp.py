#src\BookModule_200206\MainApp.py
from BookFuncLibrary import *

if __name__ == '__main__' :
    BookDict = dict()
    selector = 0
    BookDict = BookLoad('..\\..\\resource\\BookData.txt')
    while True :
        selector = int(input("""1. 도서 정보 추가\n2. 도서 정보의 삭제
3. 도서 정보 출력\n4. 프로그램 종료\nselect > """))
        if selector == 1 :
            BookAppend(BookDict)
        elif selector == 2 :
            deleteBook(BookDict)
        elif selector == 3 :
            viewBookList(BookDict)
        elif selector == 4 :
            ExitProgram(BookDict,'..\\..\\resource\\BookData.txt')
            break
        else :
            print('메뉴 정보가 잘못 됬습니다.')









            
    
"""
    <<의사 코드>>
Load() : 데이터를 불러온다. (O)

while :
    Select() : 메뉴를 고른다.
    if :
        정보 추가() 
    elif :
        정보 삭제()
    elif :
        정보 출력()
    elif :
        프로그램 종료()
    else :
        재입력 

"""
