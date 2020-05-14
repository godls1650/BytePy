#OOP_200210/ClassEx.py
class Cat :
    pass
class Tamer :
    def __init__(self) :
        pass
    def feed(self, dog) :
        var = dog.getName()
        print('사육사가 ', var, '에게 사료를 줍니다.')

class Dog :
    # 인스턴스의 속성을 만들 때
    # 초기화 (initialize)
    # __init__() 함수(메서드)로 속성을 추가  
    def __init__(self, n = '', k = '', a = 0, w = 0.0) : # 생성자 
        self.name = n #밖에서 자유롭게 바꿀 수 있다.
        self.__kind = k # 외부에서 조회가 안됨
        self.age = a
        self.weight = w
    # 객체 이름을 문자열로 사용하는경우
    # 대표적인 경우 print() 의 매개변수
    def __str__(self) :
        return '{}({})_{}살 {}kg'.format(self.name,self.__kind,
                                        self.age,self.weight)
    def __repr__(self) :
        return '[{},{},{},{}]'.format(self.name,self.__kind,
                                        self.age,self.weight)
    def howl(self, sound) :
        print(self.name, '이 짖습니다.')
        print(sound)
    # 값을 가져오거나 변경하는 메서드 getter / setter
    def getName(self) :
        return self.name
    


        
 
        
