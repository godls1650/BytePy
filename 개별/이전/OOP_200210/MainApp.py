#OOP_200210/MainApp.py
from ClassEx import Dog
from ClassEx import Cat
from ClassEx import Tamer
if __name__ == '__main__' :
    bori = Dog('보리','시츄',2, 3.6) # 인스턴스
    Sion = Dog('시온','푸들',5,5.7)
    temp = Dog(k ='허스키')
    na = Tamer()
    na.feed(bori)
    

    bori.name = '니네집 개 아님'
    print(bori)
    print(bori.name)
    print(bori.__kind)

    
    
    print(Sion)
    print(temp)
    bori.howl('왕왕')
    Sion.howl('왈 왈')
    temp.howl('컹컹ㅋ어컼엌엌컹')

    load = [['보리','시츄',2, 3.6],
            ['시온','푸들',5,5.7]]
    
    print('{}({})_{}살 {}kg'.
          format(load[0][0],load[0][1],load[0][2],load[0][3]))
    print('{}({})_{}살 {}kg'.
          format(load[1][0],load[1][1],load[1][2],load[1][3]))
