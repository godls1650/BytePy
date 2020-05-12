
def palindrome(_src) :
    l = len(_src)//2
    bpalin = False
    for i in range(l) :
        if(_src[i] == _src[-(i+1)]) :
            bpalin = True
        else :
            return False
    return bpalin
            
        
def hashf(_src) :
    hashvalue = 0
    for i in _src :
        hashvalue += ord(i)
    return hashf % 4


    

if __name__ == '__main__' :
    storage = ['level', '고기가가가기고','MADAM','20200202','다시합창합시다','주유소의소유주','통술집술통']
    
