
def hashf(_source) :
    _hash = 0;
    for i in _source : 
        _hash += ord(i)
    _hash = _hash % 3

    return _hash

def palindrome(_source) :
    index = len(_source) // 2
    bPalind = False
    j = len(_source) - 1
    i = 0
    while True:
        if(_source[i] == _source[j - i]) :
            bPalind = True
        else :
            return False
        i+=1
        
    return bPalind
    

if __name__ == '__main__' :
    dataList = ['hello world', 'python', 'korea', 'hommer simpson', 'smith', 'bear' , 'chicken']
    for i in dataList :
        print('원본 문자열 : %s --> hash()값 : %d'%(i, hashf(i)))
    print('{} 는 회문입니까 > {}'.format('다시합창합시다', palindrome('다시합창합시다')))
    print('{} 는 회문입니까 > {}'.format('level', palindrome('level')))
    print('{} 는 회문입니까 > {}'.format('hello', palindrome('hello')))


"""
회문 검사 알고리즘을 설계부터 구현

다시합창합시다.
level
고기가가가기고
"""
    
