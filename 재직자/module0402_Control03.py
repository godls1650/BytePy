#New game(n)
#Load game(l)
#Save game(s)
#Exit(e)
# CLI  : Command Line Interface

# 기본 동작을 구현  세부항목 구현 , 각 항목에대한 예외상황 처리 구현 
bError = False
for i in range(5) :
    if bError :
        print('retry(%d / 5)'%i, end = ' ')
        bError = False
    ID = input('ID : ')
    PW = input('PW : ')
    if ID not in IDList :
        print('ID not found')
        bError = True
        continue
    else :
        bError = False
        if PW is not ACCOUNT.getPW() :
           print('Pw Error')
            bError = True
            continue
        else :
            bError = False
    if not bError :
        print('log in Success')
        break
    

while True :
    print("""New game(n)
Load game(l)
Save game(s)
Exit(e)""")
    menu = input('>>>')
    if menu == 'n' or menu == 'N' :
        print('play new Game')
    elif menu == 'l' or menu == 'L' :
        print('Load Game File list')
    elif menu == 's' or menu == 'S' :
        print('Save file')
    elif menu == 'e' or menu == 'E' :
        print('save state...')
        print('program exit')
        break# 보조제어문 
    else :
        continue# 보조 제어문 
exit()
