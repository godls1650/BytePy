#class
# 객체지향 프로그래밍 : simula -> 시뮬레이션 특화 프로그래밍언어
# 사물, 개념 --> 컴퓨터에 입력
# 어떤 사물인지에 대한 데이터
# 이 사물에 동작
# TV : 모델명 , 제조사, 인치수 , 효율 , 가격  : 객체의 속성 
#    채널버튼을 눌렀을 때 음량 버튼을 눌렀을 때 : 객체의 동작 
#    옵션버튼을 눌렀을 때  전원 버튼을 눌렀을 때
# 속성 : Attribute , member 변수 
# 동작 : Method
 # 리스트 클래스 
# <데이터를 나열해서 묶어>놓은것 : 리스트
# 여러개의 데이터를 나열할 공간
# 데이터를 추가할 경우
# 데이터를 보여줘야 할 경우
# 데이터를 삭제할 경우
# 나열된데이터 중 하나의 순번을 확인해야하는 경우
# 어느 순서에 어떠한 데이터가 있는지 조회 하는 경우
# 몇개 가 있는가

# 사람 정보 클래스  ---> 홍길동 객체
#                 ---> 아무개 객체

# class 명령어
# 기존에 있는 함수를 명칭을 유지한 채로 덮어쓸 수 있다.  
# 객체지향 3원칙  : 1. 다형성  2. 상속성 3. 정보은닉 
# 

class TV :
    #속성 : magic Method : __init__() 메서드에
    #      이 클래스의 속성 값들을 나열한다 .
    # 생성자 
    def __init__(self,modelname = '',price = 0) :  # 객체 자신이라는 의미로 : self
        self.__ModelName = modelname
        self.__Price = price
        self.__Channel = 0
        self.__Volume = 0
        self.__PowerBtn = False
    def __str__(self) :
        form = "모델명 : %s가격 : %d원"%(self.ModelName, self.Price)
        return self.__ModelName
    
    def __repr__(self) :
        return self.__str__()
    def PushPowerBtn(self) :
        self.__PowerBtn = not self.__PowerBtn
        if self.__PowerBtn :
            print('전원을 켰습니다.')
        else :
            print('전원을 껐습니다.')

    def PushChUpBtn(self) :
        if self.__Channel == 13 :
            self.__Channel = 1
        else :
            self.__Channel += 1 
    def PushChDownBtn(self) :
        if self.__Channel == 1 :
            self.__Channel = 13
        else :
            self.__Channel -= 1 
    def PushVolUpBtn(self) :
        if self.__Volume == 10 :
            pass
        else :
            self.__Volume += 1 
    def PushVolDownBtn(self) :
        if self.__Volume == 0 :
            pass
        else :
            self.__Volume -= 1

    def DisplayInfo(self)  :
        if self.__PowerBtn :
            print('Channel : %d\n Volume : %d'%(self.__Channel,self.__Volume))
        else :
            pass
        
        
    
# 정보은닉 : 어떤 객체의 내부 멤버변수는
#           그 객체의 클래스에 정의되어있는 함수로만 변경 할 수 있다.

    

    


if __name__ == '__main__' :
    SmNewTv = TV('samsung smart tv' , 1258000) 
    sampleTv = TV()
    while True :
        menu = int(input('1.Channel Up  2.Channel Down 3.VolumeUP 4.VolumeDown 5.Power \n>>'))
        if menu == 1 :
            SmNewTv.PushChUpBtn()
        elif menu == 2:
            SmNewTv.PushChDownBtn()
        elif menu == 3 :
            SmNewTv.PushVolUpBtn()
        elif menu == 4:
            SmNewTv.PushVolDownBtn()
        elif menu == 5:
            SmNewTv.PushPowerBtn()
        SmNewTv.DisplayInfo()



















