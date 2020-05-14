# 모듈 추가 
import random as rd# random을 추가하는데 명칭을 rd로 바꾼다  

# setBoard 함수 구현
def setBoard(board) :
    global minimum
    global maximum
    global storage
    x = 0
    check = set() 
   
    while len(check) < 25 : 
        x = rd.randrange(10, 50)
        check.update(set((str(x), )))

    storage = [int(i) for i in check]

    for i in range(5) : # i : 0,1,2,3,4
        board.append(storage[i*5 : (i+1)*5])
    return board



# 보드판 출력 구현
def printBoard(board, board2) :
    for i in range(5) :
        for j in range(5) :
            print("%2d"%board[i][j],end = ' ')
        print(end = '\t\t')
        for j in range(5) :
            print("%2d"%board2[i][j],end = ' ')
        print()



# 컴퓨터가 숫자를 부를 때
def comChoice(board) :
    index = rd.randrange(0,5)
    data = rd.sample(comBoard[index] , 1) 
    data = data[0]
    while data == 0 :
            index = rd.randrange(0,5)
            data = rd.sample(comBoard[index] , 1)
            data = data[0]
    return data




# 보드의 숫자 체크
def checkBoard(board, value) :
    for i in range(5):
        for j in range(5):
            if value == board[i][j] :
                board[i][j] = 0
                return board
    return board


def countLine(board) :
    line = 0
    c = 0
    for i in range(5) :  # 가로
        for j in range(5) :
            c += board[i][j]
        if c == 0 :
            line += 1
        c = 0

    for i in range(5) :   # 세로
        for j in range(5) :
            c += board[j][i]
        if c == 0 :
            line += 1
        c = 0
        
    for i in range(5) :   # 대각선
        c += board[i][i]
    if c == 0 :
        line += 1        
    c = 0
    for i in range(5) :
        c += board[i][4-i]
    if c == 0 :
        line += 1
    return line



# 프로그램 동작 부분 : 변수 선언 
# 글로벌 변수 선언
minimum = 10
maximum = 50
storage = list()
userBoard = list() # 두 Board 변수를 2차원 리스트로 만든다.
comBoard = list()
data = 0

userLine = 0
comLine = 0





# 빙고 판 setting
userBoard = setBoard(userBoard)
comBoard = setBoard(comBoard)
myTurn = True
index = 0
printBoard(userBoard, comBoard)



# 빙고 동작을 구현
while True :
    
    #내가 선택
    if myTurn :
        data = int(input('숫자 선택 > '))
    #컴퓨터 선택
    else :
        data = comChoice(comBoard)
        print('com :',data)
        
    myTurn = not myTurn

    # 각 리스트의 값을 조회해서
    # data와 같은 값이 있으면 0으로 바꾼다
    userBoard = checkBoard(userBoard,data)
    comBoard = checkBoard(comBoard,data)
    printBoard(userBoard, comBoard)

    
    # 라인 세기 
    userLine = countLine(userBoard)
    comLine = countLine(comBoard)    
    print("내 라인수 : %d \n com 라인수 %d\n"%(userLine,comLine))
    if userLine >= 5 or comLine >= 5 :
        break
if userLine > comLine :
    print("You Win")
elif userLine < comLine :
    print("You Lose")
else :
    print("Draw")

