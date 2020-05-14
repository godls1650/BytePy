#calculator
class Integer :
    def __init__(self, buf = '86') :
        self.storage = 0
        if len(buf) > 1 :
            l = len(buf)
            for i in range(l) :
                self.storage += (ord(buf[i]) - ord('0'))*pow(10,(l-1)-i)
        else :
            self.storage = ord(buf)- ord('0') # 문자값을 코드번호로 교환 
        #               49  - 48 = '0' - '0' --> 0
        #
    def __str__(self) :
        temp = self.storage
        form = str()
        while temp != 0 :
            ic = temp  % 10
            #6 --> '6'
            ic = chr(ic + ord('0'))
            form = ic + form # '8'+'6'
            temp //= 10
            
        return form
    def __repr__(self) :
        return self.__str__()
    def __add__(self, rParam) :
        return self.storage + rParam.storage

    def isOdd(self) :
        return True if self.storage & 1 else False
    def isEven(self):
        return not self.isOdd() # <  , >=   !=  ==  >  <=

        
        
