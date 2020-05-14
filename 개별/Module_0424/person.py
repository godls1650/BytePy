# 사람의 모든 정보와 그 정보를 활용할 동작을 구현해서 사용하자
# --> 하나의 객체를 정보화시킨 구조 : 클래스
# 언어의 사용자가 필요하기 때문에 직접 만든 데이터 타입

# 계산기 연산자 버튼 ~~~ : 메서드(method),
#출력창 : 계산기가 가지는 정보 (속성 : Attribute)
# 클래스 : 속성과 동작을 모두 갖는 타입  --> 만들어야 되는거 

class person :
    # 속성(attribute) : 이 클래스로 객체를 생성 했을 때
    #                  메모리에 필요 데이터를 생성한다.
    #                   __init__(self)
    # 객체가 사용하는 메서드 -> self 
    def __init__(self) :
        # self.변수이름 : person 클래스로 만들어진 객체의 속성 
        self.name
        self.mail
        self.phone
        self.company
        
    #. 동작(method) 
    
