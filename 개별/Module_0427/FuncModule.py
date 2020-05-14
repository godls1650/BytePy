# 자료별 추가 연산 모듈

def strUpper(lines) :
    line = list(lines)
    rt = str()
    asc = 0
    n = 0
    for i in range(len(line)) :
        asc = ord(line[i])
        if asc >= ord('a') and asc <= ord('z') :
            asc -= 32
        else :
            pass
        rt += chr(asc)
    
    return rt

class Book :
    def __init__(self) :
        self._sTitle = str()
        self._sAuthor = str()
        self._sCompany = str()
        self._nPrice = int()
    def loadFile(self) :
        global f
        if f == None :
            return
        load = f.readline().split('\t')
        self._sTitle = load[0]
        self._sAuthor = load[1]
        self._sCompany = load[2]
        self._nPrice = int(load[3])

class Gossip(Book) :
    def __init__(self) :
        self.__month
    
    









        
        
    
