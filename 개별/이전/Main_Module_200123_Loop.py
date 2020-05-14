# 반복 제어 : 조건을 만족하면 범위의 코드를 재실행 -> while 조건식 :
# 정수를 입력합니다.
# 입력된 정수값을 이용해서 2진수로 변환한 결과를 출력합니다.

if __name__ == '__main__' :

    dec = int(input('정수를 입력하세요 > '))
    bitList = []

    temp = dec

    while dec != 1 :
        bitList.append(dec % 2)
        dec //= 2
    bitList.append(dec)
    print(bitList)
    bitList.reverse()
    print(bitList)
    strForm = ""
    index = 0
    while index != len(bitList) :
        strForm += str(bitList[index])
        index += 1
    print('{} 는 이진수로 -> {} 입니다.'.format(temp,strForm))    






if __name__ == 'MAIN' :
    treeHit = 0
    while treeHit != 10 :
        treeHit += 1 # treeHit = treeHit + 1
        print('{}번 찍었습니다.'.format(treeHit))
    print('나무가 넘어갑니다.')

    while (select != 4):
        select = int(input('1.새로만들기 2.불러오기 3. 저장하기 4. 종료 > '))
        if select == 1 :
            pass
        elif select == 2 :
            pass
        elif select == 3 :
            pass
        elif select == 4 :
            pass
        else :
            print('not exist menu')
