def onclickCheck() :
    hardCheck()
    memoryCheck()
    initialize()

menu = int(input('1.원클릭 2. 하드검사 3. 메모리검사 4. 최적화'))

if(menu == 1) :
    onclickCheck()
elif(menu == 2) :
    hardCheck()
elif(menu == 3) :
    memoryCheck()
elif(menu == 4) :
    initialize()
