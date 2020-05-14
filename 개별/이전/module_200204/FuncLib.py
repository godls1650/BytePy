#FuncLib.py
#파일 입출력
def fileLoad(FileName) :
    MemberDict = dict()
    f = open(FileName, 'r')
    temp = f.readlines()
    for i in range(len(temp)) :
        MemberDict[i+1] = temp[i].split('\t')
        MemberDict[i+1][2] = int(MemberDict[i+1][2])
    f.close()
    return MemberDict
def MemberAppend(dic):
    name = input('회원 이름 : ')
    address = input('주소 : ')
    age = int(input('나이 : '))
    dic[len(dic)+1] = [name,address, age]
    
