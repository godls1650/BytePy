#Monster
class monster :
    def __init__(self,name = '', hp = 50, mp = 50, atk = 10, deff = 12):
        self.__Name = name
        self.__HP = hp
        self.__MP = mp
        self.__ATK = atk
        self.__DEF = deff
    def __str__(self):
        form = '이름 : %s\nHP : %d  MP : %d'%(self.__Name, self.__HP, self.__MP)
        return  form

    def Attack(self):
        return self.__ATK
    def Defence(self):
        return self.__DEF
    def SKILL(self) :
        self._MP -= 10
        return int(self.__ATK*1.20)



